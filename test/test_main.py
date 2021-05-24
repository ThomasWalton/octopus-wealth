import json
import pytest

from src.hacker_news_api import call_top_stories, call_top_ask_stories, call_top_show_stories
from src.util import is_valid_story, format_story, slice_list


def test_top_stories(client, requests_mock):
    expected = [
        {
            "by": "phonebucket",
            "comments": 8,
            "id": 27261348,
            "rank": 1,
            "score": 37,
            "title": "Claude Shannon: Tinkerer, Prankster, and Father of Information Theory (2016)",
            "url": "https://spectrum.ieee.org/tech-history/cyberspace/claude-shannon-tinkerer-prankster-and-father-of-information-theory"
        }
    ]
    requests_mock.get('https://hacker-news.firebaseio.com/v0/topstories.json',  json=[27261348])
    requests_mock.get('https://hacker-news.firebaseio.com/v0/item/27261348.json', json=first_mock)

    res = client.get('/api/top-stories/1')

    assert res.status_code == 200
    assert expected == res.json


def test_top_stories_ask(client, requests_mock):
    expected = [
        {
            "by": "phonebucket",
            "comments": 8,
            "id": 27261348,
            "rank": 1,
            "score": 37,
            "title": "Claude Shannon: Tinkerer, Prankster, and Father of Information Theory (2016)",
            "url": "https://spectrum.ieee.org/tech-history/cyberspace/claude-shannon-tinkerer-prankster-and-father-of-information-theory"
        }
    ]
    requests_mock.get('https://hacker-news.firebaseio.com/v0/askstories.json',  json=[27261348])
    requests_mock.get('https://hacker-news.firebaseio.com/v0/item/27261348.json', json=first_mock)

    res = client.get('/api/top-stories/ask/1')

    assert res.status_code == 200
    assert expected == res.json


def test_top_stories_show(client, requests_mock):
    expected = [
        {
            "by": "phonebucket",
            "comments": 8,
            "id": 27261348,
            "rank": 1,
            "score": 37,
            "title": "Claude Shannon: Tinkerer, Prankster, and Father of Information Theory (2016)",
            "url": "https://spectrum.ieee.org/tech-history/cyberspace/claude-shannon-tinkerer-prankster-and-father-of-information-theory"
        },
        {
            'by': 'morsanu',
            'comments': 69,
            'id': 27261399,
            'rank': 2,
            'score': 205,
            'title': 'A Japanese company cut 80% of the time needed to manually count pearls',
            "url": 'https://countthings.com/case-studies/0001'
        }
    ]
    requests_mock.get('https://hacker-news.firebaseio.com/v0/showstories.json',  json=[27261348, 27261399])
    requests_mock.get('https://hacker-news.firebaseio.com/v0/item/27261348.json', json=first_mock)
    requests_mock.get('https://hacker-news.firebaseio.com/v0/item/27261399.json', json=second_mock)

    res = client.get('/api/top-stories/show/2')

    assert res.status_code == 200
    assert expected[0] == res.json[0]
    assert expected[1] == res.json[1]


def test_story(client, requests_mock):
    expected = {
        "by": "phonebucket",
        "comments": 8,
        "id": 27261348,
        "score": 37,
        "title": "Claude Shannon: Tinkerer, Prankster, and Father of Information Theory (2016)",
        "url": "https://spectrum.ieee.org/tech-history/cyberspace/claude-shannon-tinkerer-prankster-and-father-of-information-theory"
    }
    requests_mock.get('https://hacker-news.firebaseio.com/v0/item/27261348.json', json=first_mock)

    res = client.get('/api/story/27261348')

    assert res.status_code == 200
    assert expected == res.json


first_mock = {
    "by": "phonebucket",
    "descendants": 8,
    "id": 27261348,
    "kids": [
        27262145,
        27262153,
        27262444,
        27262310
    ],
    "score": 37,
    "time": 1621834228,
    "title": "Claude Shannon: Tinkerer, Prankster, and Father of Information Theory (2016)",
    "type": "story",
    "url": "https://spectrum.ieee.org/tech-history/cyberspace/claude-shannon-tinkerer-prankster-and-father-of-information-theory"
}


second_mock = {
    "by": "morsanu",
    "descendants": 69,
    "id": 27261399,
    "kids": [
        27261685,
        27261764,
        27262075,
        27262146,
        27261706,
        27261638,
        27261883,
        27261951,
        27261635,
        27262174,
        27261800,
        27262281,
        27262044,
        27261746,
        27261636,
        27262419
    ],
    "score": 205,
    "time": 1621835056,
    "title": "A Japanese company cut 80% of the time needed to manually count pearls",
    "type": "story",
    "url": "https://countthings.com/case-studies/0001"
}
