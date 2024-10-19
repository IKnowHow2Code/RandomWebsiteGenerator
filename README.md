# Random Website Generator

This Python project generates random websites and checks if they are reachable and contain meaningful content. It uses a graphical user interface (GUI) to display the first valid website found. The script leverages asynchronous processing and web scraping techniques to validate the website content before showing it to the user.

## Features
- **Random URL Generation**: Generates random website URLs with popular TLDs like `.com`, `.net`, `.org`, `.io`, `.co`.
- **Content Validation**: Uses web scraping to check if the website contains meaningful content (not just placeholder pages).
- **Asynchronous Requests**: Uses `aiohttp` and `asyncio` for fast and efficient URL checking.
- **User-Friendly GUI**: Built using `tkinter` to provide an interactive experience.
- **Manual Website Opening**: Allows the user to open valid websites manually after they are confirmed.

## Prerequisites
- **Python 3.7+**
- **Libraries**:
  - `aiohttp`: For asynchronous HTTP requests.
  - `beautifulsoup4`: For HTML content parsing.
  - `tkinter`: For creating the graphical user interface.
    
## License
Do whatever you want with this, I do not care.

To install the required libraries, run:
```bash
pip install aiohttp beautifulsoup4
