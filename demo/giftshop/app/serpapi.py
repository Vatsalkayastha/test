from serpapi import GoogleSearch
from .config import Config
import logging

serpapi_key = Config.get_serpapi_key()

def get_book_course_suggestions(topic):
    params = {
        "api_key": serpapi_key,
        "engine": "google",
        "google_domain": "google.com",
        "q": f"best {topic} books and courses",
        "hl": "en",
        "gl": "us",
        "num": 2  # You can adjust the number of results you want
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    logging.info(results)

    # Return the search results for books and courses related to the topic
    out = results.get('course_results', [])
    logging.info(out)

    return out
