# Incorporated Places

Incorporated Places randomly chooses an [incorporated
place](http://en.wikipedia.org/wiki/Place_(United_States_Census_Bureau)#Incorporated_place)
(weighted by its population), zooms in to it, and pans around the area.
Approximately every 90 seconds, it chooses a new place and zooms to it and
beings again. You can click to cycle through road, satellite, and hybrid map
modes. Other than map mode, the viewer has no control over the experience.

It is intended to make the viewer appreciate the country's geography, think
about the people living in each place, and, most importantly, please viewers
aesthetically.

# The code

The map uses a JSON file containing the population and name of every
incorporated place in the country. To create the JSON data file, use
`places.py`, which takes as input a [U.S. Census incorporated places population
dataset](http://www.census.gov/popest/datasets.html) and outputs the JSON to
the second positional argument:
   
    ./places.py SUB-EST2009-IP.UTF-8.csv places.js

N.B.: `places.py` uses Python's `csv` module, which currently has problems with
inputs that are not UTF-8. Thus, it is necessary to convert the character set
of the [Census's
csv](http://www.census.gov/popest/cities/files/SUB-EST2009-IP.csv):

    iconv -f ISO-8859-1 -t UTF-8 SUB-EST2009-IP.csv > SUB-EST2009-IP.UTF-8.csv

# Thanks

Infinite thanks to the Google Maps team for creating a map so fun to look at
and an API so easy to use, I had to create this.
