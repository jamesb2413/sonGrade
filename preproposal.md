# Proposal

## What will (likely) be the title of your project?

SonGrade

## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")

A website that lets users rate songs and displays tables of related songs with their ratings.

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

I plan to create a web application which compiles a databases of users' ratings of songs out of
a scale of 100. There will be two different methods for rating songs, one of which will be giving
a holistic, overall rating right off the bat out of 100, and one of which will be a more in-depth analysis,
taking into account ratings out of 10 of lyrics, sonics, the factor of the performer's personality/reputation,
and impact of the live performance, along with an overall score. THe more in-depth analysis will be
converted into a score out of 100. If multiple ratings are made for a song, the ratings will be averaged
and the song's average rating will be displayed. On the homepage (index.html), highest ratings, ratings
of new songs, and songs that are rated most frequently will be displayed. Users will be able to rate a
song by searching for it in a database and submitting a rating without logging in, but they will also
be able to create an account and log in to see a history of their ratings, along with their average scores
given across all of the songs they have rated. When songs are first rated, they will be added to the database,
so more songs accumulate over time.

The software will be run with a few html forms, python, and a couple of SQL tables.

## If planning to combine CS50's final project with another course's final project, with which other course? And which aspect(s) of your proposed project would relate to CS50, and which aspect(s) would relate to the other course?

TODO, if applicable

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

I will make a table that can hold songs and their ratings, and develop forms to submit ratings of songs.

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

I will allow individual users to register and store an additional table which will keep a history of their previous ratings.

### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

I will additionally create tables of most popular, highest rated, lowest rated, and new ratings.

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

I will first need to develop a frame of a few forms and a table, with python control programming. I also
need to calculate ways to average out scores so that multiple categorical scores out of 10 can be equated
to a score out of 100. I also need to decide whether I will be able to use a song database, such as Last.fm,
or whether that will be impossible. If impossible, I will need to simply add what users type into forms into
the database, but that may cause issues if users type things that are not songs. Issues like these are ones
that I will need to tackle first.
