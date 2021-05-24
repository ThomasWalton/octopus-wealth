from flask import Flask, jsonify
from src.hacker_news_api import call_story, call_top_stories, call_top_ask_stories, call_top_show_stories

app = Flask(__name__)

@app.route("/api/top-stories", defaults={'count': None,})
@app.route("/api/top-stories/<int:count>")
def top_stories(count):
    return jsonify(call_top_stories(count))


@app.route("/api/top-stories/ask", defaults={'count': None,})
@app.route("/api/top-stories/ask/<int:count>")
def top_stories_ask(count):
    return jsonify(call_top_ask_stories(count))


@app.route("/api/top-stories/show", defaults={'count': None,})
@app.route("/api/top-stories/show/<int:count>")
def top_stories_show(count):
    return jsonify(call_top_show_stories(count))


@app.route("/api/story/<int:story_id>")
def story(story_id):
    return jsonify(call_story(story_id))
