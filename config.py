import os


# Environment variables
os.environ['ENV_USR'] = 'arunvemana@outlook.com'
os.environ['ENV_PASS'] = 'Welcome3#'

USERNAME = os.getenv('ENV_USR')
PASSWORD = os.getenv('ENV_PASS')

if not USERNAME and PASSWORD:
    raise  EnvironmentError(
        f"Missing credentials , OF BOTH ENV_USR AND ENV_USR: {USERNAME} AND {PASSWORD}"
    )