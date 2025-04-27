from typing import Any

import requests
from bs4 import BeautifulSoup


def fetch_lectures(session: requests.Session, course_url: str) -> RuntimeError | list[Any]:
    """
    Fetch the course syllabus total topic and total number of classes and time of each session.
    :param session: Session of the login.
    :param course_url: Select the course details url
    :return: -> list[dict]
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.50 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Referer": "https://learn.datamites.com/",
    }
    if not course_url.startswith("https"):
        return RuntimeError("Unable to fetch Url of the course")
    try:
        response = session.get(course_url,headers=headers,timeout=15)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        return RuntimeError("Something is wrong with connection")
    soup = BeautifulSoup(response.text, "html.parser")
    group_lectures = soup.find_all("div", class_="lecture-group-wrapper")
    # getting each topic
    topics = []
    what_if_no_data = lambda param_, param_m: param_.get_text(strip=True) if param_ else param_m
    for group in group_lectures:
        title_ = group.find("div", class_='lecture-group-title')
        total_ = group.find("span", class_='total-lectures')
        time_ = group.find("span", class_='total-time')
        topic = {
            "title": what_if_no_data(title_, "No title found"),
            "Number_of_sessions": what_if_no_data(total_, "0 lectures"),
            "total_time": what_if_no_data(time_, "0h 0m")
        }
        topics.append(topic)
    return topics
