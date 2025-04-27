# Stealth-Fetch Datamites Video Downloader

**Authentication required. Educational use only — use at your own risk. No warranty; respect content ownership and platform policies.**

---
## Structures
Here's is the coming up structure for the Datamites lectures video Downloader project:

```
datamites-video-downloader/
├── README.md                # Project overview and instructions
├── LICENSE                  # MIT License
├── requirements.txt         # pip dependencies (requests, tqdm, click)
│
├── config.py                # Stores USERNAME and PASSWORD (imported by auth)
├── auth.py                  # Handles login, session creation, and authentication
├── courses.py               # Fetches and parses list of available courses
├── lectures.py              # Retrieves lecture lists and extracts video URLs
├── downloader.py            # Streams and downloads a given video URL with progress UI
├── cli.py                   # Command‑line interface using click or argparse
│
├── tests/                   # Unit and integration tests
    ├── test_auth.py
    ├── test_courses.py
    └── test_downloader.py
```

**Module Responsibilities**

- **config.py**: Define and load credentials securely (environment variables or file-based).
- **auth.py**: Create a session, perform login with credentials, handle CSRF or cookies.
- **courses.py**: Use the authenticated session to fetch the dashboard or courses endpoint, parse available courses.
- **lectures.py**: After a course is selected, fetch its lecture list and extract direct video URLs.
- **downloader.py**: Given a URL, download in chunks with live progress (MB or percentage), optional tqdm bar.
- **cli.py**: Glue everything together in a user‑friendly CLI: prompt for login (or read from config), list courses, select, list lectures, select lecture(s), download.
- **tests/**: Write tests for each component using pytest; mock HTTP responses.


## ⚙️ Features

- Built with Python `requests` and optional `tqdm` integration for a progress bar.
- Supports authenticated sessions with username/password credentials.

## 🛠️ Requirements

- Python 3.7 or higher
- [requests](https://pypi.org/project/requests/)
- Optional: [tqdm](https://pypi.org/project/tqdm/) for enhanced progress bars

## 🚀 Installation

1. Clone.
2. (Optional) Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```
3. Install required packages:
```bash
pip install -r requirements.txt
```

## 📥 Usage

1. Update `auth.py` with your Datamites credentials:
   ```python
   USERNAME = "your.email@gmail.com"
   PASSWORD = "supersecret"
   ```
## 👷 Development resources:

1 . icons are copied from https://gist.github.com/nicolasdao/8f0220d050f585be1b56cc615ef6c12e

## ⚠️ Disclaimer

- This tool is provided **"as is"** with **no warranty** or guarantee of functionality.  
- Use this downloader **at your own risk**.  
- You must have valid access to Datamites content, and you agree to abide by their Terms of Service.  
- This script is intended for **personal educational use only**.  

## 📜 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

*Built with ♥ for hackers by hackers.*

