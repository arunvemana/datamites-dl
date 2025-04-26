from InquirerPy import inquirer
from auth import Authenticator
from courses import fetch_courses


def main():
    """
    Main Function where the application starts
    :return:
    """
    auth = Authenticator()
    session = auth.login()

    # Fetch course details which you purchased.
    courses = fetch_courses(session)

    # Creating the UI
    choices = [{"name":course["title"],"value":course} for course in courses]

    # UI
    select_c = inquirer.select(
        message= "Select Course to get lecture information:",
        choices= choices,
        pointer="💨",
        instruction=" Arrow keys ⬆️⬇️ or Navigate keys and Press ENTER for selection"
    ).execute()

    # showcase
    print(f"\nyou selected {select_c["title"]} \n url is {select_c["url"]}")

if __name__ == "__main__":
    main()