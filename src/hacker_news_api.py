import concurrent.futures
import requests
import urllib.parse
import json

import time

from src.util import is_valid_story, format_story, slice_list

base_url = "https://hacker-news.firebaseio.com/v0/"


def call_top_stories(count):
    story_list_url = urllib.parse.urljoin(base_url, "topstories.json")
    res = requests.get(story_list_url).json()
    id_list = slice_list(list(res), count)
    return get_stories(id_list)


def call_top_ask_stories(count):
    story_list_url = urllib.parse.urljoin(base_url, "askstories.json")
    res = requests.get(story_list_url).json()
    id_list = slice_list(res, count)
    return get_stories(id_list)


def call_top_show_stories(count):
    story_list_url = urllib.parse.urljoin(base_url, "showstories.json")
    res = requests.get(story_list_url).json()
    id_list = slice_list(res, count)
    return get_stories(id_list)


def call_story(id):
    res = get_story(id)
    if is_valid_story(res):
        return format_story(res)
    return None


def get_stories(id_list):
    with concurrent.futures.ThreadPoolExecutor() as executor:  # optimally defined number of threads
        future_to_url = {executor.submit(get_story, id): id for id in id_list}
        stories = []
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                res = future.result()
                if is_valid_story(res):
                    stories.append(format_story(res, id_list.index(future_to_url[future]) + 1))
            except Exception as exc:
                print("generated an exception %s", exc)
        return stories


def get_story(id):
    url = urllib.parse.urljoin(base_url, "item/{}.json".format(id))
    return requests.get(url).json()
