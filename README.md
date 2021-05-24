# **Octopus Wealth Kata - Tom Walton**

Implemented all four endpoints. Put in a unit test for each, I would normally have made a few more cases but decided to keep things simple.
I would also normally look at setting up a simple build command, with something like make. However, due time constraints Ill just list what i've used.

I made a slight assumption with the fields being returned. The ASK endpoint doesn't return any URLs, as the hacker news api doesn't include them.


You'll need to have python installed, I believe any version 3+ will work.

I used Flask as a simple api toolkit, and the requests library to make simple requests

To install, it should work with:

`pip install -r requirements.txt`

And then to run:

`export FLASK_APP=src/main.py `

`flask run`

And for testing:

`pytest`

I haven't had much time to test the devops, so you may also need to do a pip install for Flask, requests and pytest; if they didn't install properly.
