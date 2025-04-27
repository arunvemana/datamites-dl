from functools import wraps
from yaspin import yaspin
from yaspin.spinners import Spinners

def loading_spinner(text="Loading...", spinner=Spinners.line):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with yaspin(text=text, spinner=spinner) as spin:
                result = func(*args, **kwargs)
                spin.ok("✅")
            return result
        return wrapper
    return decorator