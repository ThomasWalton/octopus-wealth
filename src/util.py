import re

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


def format_story(story, rank=None):
    story_dict = {
        "id": story["id"],
        "score": story["score"] if "score" in story else 0,
        "comments": story["descendants"] if "descendants" in story else 0,
        "by": story["by"],
        "title": story["title"],
    }
    if rank:
        story_dict["rank"] = rank

    if "url" in story:
        story_dict["url"] = story["url"]
    return story_dict


def is_valid_story(story):
    valid_by = is_valid_string(str(story["by"]))
    valid_title = is_valid_string(str(story["title"]))
    valid_url = "url" not in story or re.match(regex, story["url"])
    valid_score = "score" not in story or is_valid_int(story["score"])
    valid_descendants = "descendants" not in story or is_valid_int(story["descendants"])
    return valid_by and valid_title and valid_url and valid_score and valid_descendants


def is_valid_string(s):
    return s and len(s) <= 256

def is_valid_int(i):
    return isinstance(i, int) and i >= 0

def slice_list(list, count):
    if count > 0:
        slice = count
        if len(list) < count:
            slice = len(list)
        list = list[:slice]
    return list

