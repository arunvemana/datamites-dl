from InquirerPy import inquirer
from auth import Authenticator
from courses import fetch_courses
from lectures import fetch_lectures
from download import download_video

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

        # showcase of individual session of the lecture group.
        indiv_select_l = [
            {"name": f"🗿 {lec['lecture_title']} - ⌛ {lec['duration']}", "value": lec}
            for lec in select_l["lectures"]
        ]
        select_video = inquirer.select(message="\n Choose a lecture video",
                                       choices=indiv_select_l,
                                       pointer="💨",
                                       instruction=" Arrow keys ⬆️⬇️ or Navigate keys and Press ENTER for selection"
                                       ).execute()
        # final detail show to download
        print(f"selected lecture is {select_video['lecture_title']}")
        print(f"video url is {select_video['url']}")
        print(f"video duration is {select_video['duration']}")

        # download
        download_video(select_video['url'],filename=select_video['lecture_title'])
    else:
        print("\n No lectures was found")


if __name__ == "__main__":
    main()
