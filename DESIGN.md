The design of sonGrade is based in HTML, CSS, Python, and SQL tables.

The controller code, written in Python in application.py, employs SQL, flask,
and flask_session, which is used to store values from one page to another. In
application.py, the GET and POST routes for each page are coded, allowing values
to be selected from and inserted into SQL tables.

The view code consists of index.html, search.html, rate.html, and quickRate.html,
along with style.css, which styles for all of those pages.

The model code consists of three SQL tables, located in songrade.db. allSongs
consists of all songs (titles and artists) that are rated on the site, allRate
consists of all individual ratings of those songs (0-100), and topRate keeps track
of the songs' average ratings (overall rating) and their popularity (number of
ratings).

The homepage (/) displays a navbar with buttons, a parallax image with text, and
two tables, which are implemented with Jinja to change according to the values
in the SQL tables. There is a top rated songs table and a worst rated songs table,
both of which are created by first selecting all values from topRate (to get the
title, artist, average rating, and popularity), then sorting all of the songs in
ascending order from lowest rated to highest rated in rankedList. Next, a new list,
revList is created, which reverses the order of rankedList. Both revList and
rankedList are fed into index.html using Jinja, so the tables can be displayed.

The /search route, if reached via GET, renders the search.html template. Once the
user searches a song, they reach /search via POST. When this occurs, first the
session is cleared, allowing a new song to be searched. Next, the song that is
searched is saved in session and entered into allSongs (if it's not already there),
so future pages will know the current song.

The /rate renders the rate.html template, which displays the song that the user
searched to confirm that the user wants to rate that song. It has redirecting links
to quickRate.html or index.html (quit).

The /quickRate route, if reached via GET, renders the quickRate.html page, which
once again displays the song, and additionally has a sliding range form, which the
user can use to rate the song. Once that form is submitted, the rating is calculated,
then is inserted into the allRate and topRate tables. If the song already exists in
topRate, the new average rating is calculated, and the popularity is increased by one.
This is done by updating the avgRate and popularity values in topRate. Once the rating
is completed, the user is returned to the homepage, where the process can be completed.
