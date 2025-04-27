from InquirerPy import inquirer
from auth import Authenticator
from courses import fetch_courses
from lectures import fetch_lectures


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
    choices = [{"name": course["title"], "value": course} for course in courses]

    # UI
    select_c = inquirer.select(
        message="Select Course to get lecture information:",
        choices=choices,
        pointer="💨",
        instruction=" Arrow keys ⬆️⬇️ or Navigate keys and Press ENTER for selection"
    ).execute()

    # showcase
    print(f"\nyou selected {select_c["title"]} \n url is {select_c["url"]}")

    # let's get lectures
    lectures = fetch_lectures(session, select_c["url"])

    # showcase of lectures
    print("\n Lecture Topics:")
    if lectures:
        lecture_choices = [
            {
                "name": f"🗿 [{topic['title']}] - {topic['Number_of_sessions']} | {topic['total_time']}",
                "value": topic
            }
            for topic in lectures
        ]
        select_l = inquirer.select(message="\nChoose a lecture to view details:",
                                   choices=lecture_choices,
                                   pointer="💨",
                                   instruction=" Arrow keys ⬆️⬇️ or Navigate keys and Press ENTER for selection"
                                   ).execute()

        print(f"\n You selected: {select_l["title"]}")
        print(f" 📁 Lectures: {select_l["Number_of_sessions"]}")
        print(f" ⏳ Duration: {select_l["total_time"]}")
    else:
        print("\n No lectures was found")


if __name__ == "__main__":
    main()
