import re
from typing import Any

import requests
from bs4 import BeautifulSoup
from util import loading_spinner


@loading_spinner(text="Fetching the lectures....")
def fetch_lectures(session: requests.Session, course_url: str) -> RuntimeError | list[Any]:
    """
    Fetch the course syllabus total topic and total number of classes and time of each session.
    :param session: Session of the login.
    :param course_url: Select the course details url
    :return: -> list[dict]
    """
    # general headers to simulate request coming from browser.
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
        response = session.get(course_url, headers=headers, timeout=15)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        return RuntimeError("Something is wrong with connection")
    soup = BeautifulSoup(response.text, "html.parser")
    group_lectures = soup.find_all("div", class_="lecture-group-wrapper")
    # getting each topic
    topics = []
    what_if_no_data = lambda param_, param_m: param_.get_text(strip=True) if param_ else param_m
    for group in group_lectures:
        title_ = group.find("div", class_='lecture-group-title').find("div", class_="title")
        total_ = group.find("span", class_='total-lectures')
        time_ = group.find("span", class_='total-time')
        topic = {
            "title": what_if_no_data(title_, "No title found"),
            "Number_of_sessions": what_if_no_data(total_, "0 lectures"),
            "total_time": what_if_no_data(time_, "0h 0m")
        }
        # get an individual lectures link in the group
        lecture_list = []
        lecture_objs = group.find_all("li",class_="lecture has-preview")
        for lecture in lecture_objs:
            span_ = lecture.find("span",class_="lecture-title")
            span_time = lecture.find("span",class_="lecture-time")
            if span_ and span_.has_attr('onclick'):
                click_value = span_['onclick']
                # get a link to download
                match = re.search(r"showVideo\('([^']+)'\)",click_value)
                if match:
                    url = match.group(1)
                    l_title = span_.get_text(strip=True)
                    lecture_list.append({'lecture_title':l_title,
                                         'url':url,
                                         'duration':span_time.get_text(strip=True)}
                                        )
        topic["lectures"] = lecture_list

        topics.append(topic)
    return topics
