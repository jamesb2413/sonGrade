# Nick Barna SonGrade Web App
import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///songrade.db")

# Merge_sort algorithm (used to rank the songs) source: https://www.tutorialspoint.com/python/python_sorting_algorithms.htm


def merge(left_half,right_half):
    """Merge the sorted halves"""

    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0]["avgRate"] < right_half[0]["avgRate"]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res

def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
# Find the middle point and divide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))


@app.route("/")
def index():
    """Homepage of song rankings"""

    # Get values from topRate SQL table
    topRateList = db.execute("SELECT * FROM topRate")

    if not topRateList:
        return redirect("/rate")

    else:
        # Sort (rank) songs in ascending order from lowest to highest ranking
        rankedList = merge_sort(topRateList)

        # Sort songs in reversed (descending) order
        revList = []
        for i in reversed(range(len(rankedList))):
            revList.append(rankedList[i])

        # Render index with lists for jinja
        return render_template("index.html", listDict=revList, worstDict=rankedList)


@app.route("/search", methods=["GET", "POST"])
def search():
    """Allow users to search songs to rate"""

    # Forget any stored song_id
    session.clear()

    # User reached route via POST
    if request.method == "POST":

        # See if song is in database
        songs = db.execute("SELECT * FROM allSongs WHERE title = :title AND artist = :artist",
                           title=request.form.get("song"), artist=request.form.get("artist"))

        #  If song doesn't exist in database, save song id and insert song
        if not songs:
            entry = db.execute("INSERT INTO allSongs (title, artist) VALUES(:title, :artist)",
                               title=request.form.get("song"), artist=request.form.get("artist"))
            session["song_id"] = entry

        # Else, just save song id
        else:
            session["song_id"] = songs[0]["id"]

        # Go to rate page for current song
        return redirect("/rate")


    # User reached route via GET
    else:
        return render_template("search.html")


@app.route("/rate", methods=["GET"])
def rate():
    """Allow users to confirm that they want to rate the song they have searched"""

    # Get current title and artist
    current = db.execute("SELECT * FROM allSongs WHERE id = :song_id", song_id=session["song_id"])
    song = current[0]["title"]
    artist = current[0]["artist"]
    # Go to rate page for current song
    return render_template("rate.html", song=song, artist=artist)


@app.route("/quickRate", methods=["GET", "POST"])
def quickRate():
    """Allow users to quickly rate the song"""

    # Get current title and artist
    current = db.execute("SELECT * FROM allSongs WHERE id = :song_id", song_id=session["song_id"])
    song = current[0]["title"]
    artist = current[0]["artist"]

    # User reached route via POST
    if request.method == "POST":

        # Figure out rating input
        rawRate = request.form.get("rating")
        rate = (int(rawRate) - 1) * 10

        # Add rating to allRate table
        rating = db.execute("INSERT INTO allRate (title, artist, rating) VALUES(:title, :artist, :rating)",
                          title=song, artist=artist, rating=rate)

        # See if song is already in topRate
        top = db.execute("SELECT * FROM topRate WHERE title = :title AND artist = :artist",
                         title=song, artist=artist)

        # See how many ratings for song
        pop = db.execute("SELECT * FROM allRate WHERE title = :title AND artist = :artist",
                         title=song, artist=artist)

        # If song is not yet in topRate, add it
        if not top:
            topEntry = db.execute("INSERT INTO topRate (title, artist, avgRate, popularity) VALUES(:title, :artist, :avgRate, :popu)",
                                  title=song, artist=artist, avgRate=rate, popu=1)

        # If song is already in topRate, update avgRate value
        else:
            # Get popularity and avgRate of song
            popRate = db.execute("SELECT * FROM topRate WHERE title = :title AND artist = :artist",
                             title=song, artist=artist)

            # Update avgRate value
            update = db.execute("UPDATE topRate SET avgRate=:avgRate, popularity=:popu WHERE title=:title AND artist=:artist",
                                avgRate=((popRate[0]["avgRate"]*popRate[0]["popularity"])+rate)/(popRate[0]["popularity"]+1),
                                popu=len(pop), title=song, artist=artist)

        # Return to homepage
        return redirect("/")

    # User reached route via GET
    else:

        # Go to rate page for current song
        return render_template("quickRate.html", song=song, artist=artist)