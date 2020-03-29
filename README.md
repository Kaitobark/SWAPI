# SWAPI
## Introduction
The script is to test some API calls in SWAPI and try to solve the following questions.
1. How many different species appears in film-6 (Revenge of the Sith) ?
2. Please list all the film names and sort the name by episode_id.
3. Please find out all vehicles which max_atmosphering_speed is over 1000.

The script support two ways to send API request, requests and urllib. If the request library exist, it will use request library in default.

> SWAPI website: https://swapi.co/documentation#intro

## Usage
No argument supproted in this script. It will print out the questions and the answers.

'''
python3 swapi_test.py
'''

## Test the script (Validate the answer)

The script only tested in Python3. And the answers are hard-code in the sciprt. Therefore, if the data in the website be updated, the test will failed. The answers updated on 3/29.

### Unitest
'''
python3 -m unittest swapi_test.py -v
'''
### pytest
'''
pytest swapi_test.py -v
'''