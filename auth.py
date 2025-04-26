from config import USERNAME, PASSWORD
import requests

class Authenticator:
    LOGIN_PAGE ="https://learn.datamites.com/home/login"
    LOGIN_API = "https://learn.datamites.com/login/validate_login/user"

    def __init__(self):
        self.session = requests.Session()

    def login(self)-> requests.Session:

        # Just incase any cookies required
        resp = self.session.get(self.LOGIN_PAGE)
        resp.raise_for_status()
        payload = {
            "email":USERNAME,
            "password":PASSWORD,
        }
        headers = {
            "Host":"learn.datamites.com",
            "Origin":"https://learn.datamites.com",
            "Referer": self.LOGIN_PAGE,
            "User-Agent": "datamites-downloader/1.0",
            "Content-Type": "application/x-www-form-urlencoded",
            # "Connection": "close"
        }
        # post call
        try:
            post_ = self.session.post( self.LOGIN_API, data=payload, headers=headers)
            post_.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 421:
                print(f"🚩 check the username and password{e}")

        # verify the login

        home = self.session.get("https://learn.datamites.com/home")
        home.raise_for_status()
        if home.url.endswith('/home/login'):
            raise RuntimeError("Login Failed: May be username and password")

        return self.session

if __name__ == "__main__":
    auth = Authenticator()
    session = auth.login()
    print("✅ Authenticated successfully")
