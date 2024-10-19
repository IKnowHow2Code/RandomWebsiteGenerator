import asyncio
import aiohttp
import random
import string
import tkinter as tk
import webbrowser
from bs4 import BeautifulSoup

def generate_random_string(length=5):
    """Generate a random string of lowercase letters."""
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_random_url():
    """Generate a random website URL with a popular TLD."""
    random_domain = generate_random_string(random.randint(5, 10))
    # Focus on popular and likely valid TLDs
    tlds = ['.com', '.net', '.org', '.io', '.co']
    random_tld = random.choice(tlds)
    return f"https://{random_domain}{random_tld}"

async def scrape_website(url, session):
    """Check if a website is reachable and scrape it to ensure it has meaningful content."""
    try:
        async with session.get(url, timeout=3) as response:
            if response.status == 200:
                # Read the full content but limit the bytes for efficiency
                content = await response.text()
                soup = BeautifulSoup(content, 'html.parser')

                # Get the title and clean it up
                title = soup.title.string.strip() if soup.title and soup.title.string else ""

                # Check for meaningful title and exclude common placeholders
                if title and len(title) > 5 and "coming soon" not in title.lower() and "not found" not in title.lower():
                    return title, url
    except Exception:
        pass
    return None

async def generate_and_show_website():
    """Generate and show the first valid website URL."""
    async with aiohttp.ClientSession() as session:
        while True:  # Keep generating until a valid URL is found
            urls = [generate_random_url() for _ in range(100)]  # Generate a larger batch of URLs
            tasks = [scrape_website(url, session) for url in urls]

            for task in asyncio.as_completed(tasks):
                result = await task
                if result:
                    title, valid_url = result
                    # Update the label with the valid URL and title but don't open it automatically
                    url_label.config(text=f"Title: {title}\nURL: {valid_url}")
                    open_button.config(state=tk.NORMAL)  # Enable the button to open the URL
                    return

def open_website():
    """Open the displayed URL in the default web browser."""
    text = url_label.cget("text")
    url = text.split("URL: ")[-1]
    if url and url.startswith("http"):
        webbrowser.open_new(url)

def start_generating():
    """Start the URL generation process."""
    open_button.config(state=tk.DISABLED)  # Disable the button initially
    asyncio.run(generate_and_show_website())

# GUI setup using tkinter
window = tk.Tk()
window.title("Random Website Generator")
window.geometry("600x300")

# Label to display the generated URL
url_label = tk.Label(window, text="Click the button to generate a random website!", font=("Arial", 14), wraplength=550)
url_label.pack(pady=20)

# Button to generate and show the random website
generate_button = tk.Button(window, text="Generate & Find Website", command=start_generating, font=("Arial", 12))
generate_button.pack(pady=10)

# Button to open the generated website manually
open_button = tk.Button(window, text="Open Website", command=open_website, state=tk.DISABLED, font=("Arial", 12))
open_button.pack(pady=10)

# Start the GUI event loop
window.mainloop()
