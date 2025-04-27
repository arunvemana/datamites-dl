import requests
from bs4 import BeautifulSoup
from auth import Authenticator
from typing import Dict,List
from util import loading_spinner

@loading_spinner(text="fetching Courses")
def fetch_courses(session:requests.Session) -> List[Dict]:
    """
    Get the list of courses details from the course page
    :param session: From Authenticator session
    :return: Dict of course details.
    """
    courses_url = "https://learn.datamites.com/home/my_courses"
    response = session.get(courses_url)
    response.raise_for_status()
    # Parse
    soup = BeautifulSoup(response.text, "html.parser")
    course_elements = soup.find_all("div", class_="course-details")
    courses = []
    for course in course_elements:
        # Skip if 'style' attribute is present because in the course box, duplicate of the same class with info
        if course.has_attr("style"):
            continue

        anchor = course.find("a", href=True)
        title_tag = course.find("h5")

        if anchor and title_tag:
            course_info = {
                "title": title_tag.get_text(strip=True),
                "url": anchor["href"]
            }
            courses.append(course_info)

    return courses


if __name__ == "__main__":
    # Authenticate and fetch courses
    auth = Authenticator()
    session = auth.login()
    courses = fetch_courses(session)

    # Display the courses
    for idx, course in enumerate(courses, start=1):
        print(f"{idx}. {course['title']}")
        print(f"   URL: {course['url']}\n")