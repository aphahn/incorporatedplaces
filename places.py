#!/usr/bin/env python

# From the Census Incorporated place CSV, create an optimized JS lookup that
# will return a place based on the following procedure:
#
# 1. Choose a random number in the range of [0, Population of the US)
# 2. Return the place that person would live in
#
# Output:
# {
#   // Whoa. A _bunch_ of people don't live in incorporated places!
#   totalPopulation: 192213590,
#   placeData: [
#       [population counter, "Place name", state code (0--49)],
#       ...
#       [population counter, "Place name", state code (0--49)]
#   ],
#   stateNames: ["Alabama", "Alaska", ..., "Wyoming"]
# }
# where population counter is the beginning of the US population that lives there

import csv
import json
import sys

def cleanup_name(name):
    # Remove the last uncapitalized words
    words = name.split()

    words.reverse()

    last_index = 0
    for i, word in enumerate(words):
        if not word.islower():
            # We've found the last uncapitalized word
            last_index = len(words) - i
            break

    # Back to normal
    words.reverse()

    words = words[0:last_index]
    return " ".join(words)

def main():
    if len(sys.argv) < 3:
        sys.exit("Usage: ./places.py IN_CSV OUT_JSON")

    places_reader = csv.DictReader(open(sys.argv[1], 'r'))

    pop_counter = 0
    place_data = []
    state_names = []

    for row in places_reader:
        name = cleanup_name(row['name'])

        state_name = row['STATENAME']
        if state_name not in state_names:
            state_names.append(state_name)
        state_code = state_names.index(state_name)

        place_data.append([pop_counter, name, state_code])

        pop_counter += int(row['POP_2009'])

    to_json = {}
    to_json["totalPopulation"] = pop_counter
    to_json["placeData"] = place_data
    to_json["stateNames"] = state_names

    json.dump(to_json, open(sys.argv[2], 'w'))

if __name__ == '__main__':
    main()
