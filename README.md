# MINDS_assignment
Assignment 1 for MINDS position

This program is written to scrape the Orbital launches table to make a list of dates in 2019 and the count of accepted launches.
This was written as part of the coding exercise.

The Wikipedia article: [2019 in spaceflight](https://en.wikipedia.org/wiki/2019_in_spaceflight)

* lauches.py contains the python3 program for creating output.csv file.
  To launch:
  ```
  python3 launches.py
  ```
* output.csv contains comma-separated date and number of accepted launches.
  For example:
  ```
  date,value
  2019-01-01T00:00:00,0
  2019-01-02T00:00:00,0
  2019-01-03T00:00:00,0
  2019-01-04T00:00:00,0
  2019-01-05T00:00:00,0
  2019-01-06T00:00:00,0
  2019-01-07T00:00:00,0
  2019-01-08T00:00:00,0
  2019-01-09T00:00:00,0
  2019-01-10T17:05:00,1
  2019-01-11T15:31:00,1
  ...
  2019-12-26T23:11:57,4
  2019-12-27T12:45:00,1
  2019-12-28T00:00:00,0
  2019-12-29T00:00:00,0
  2019-12-30T00:00:00,0
  2019-12-31T00:00:00,0
  ```
* spaceflight.html is HTML file of the Wikipedia article.
