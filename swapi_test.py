import json
import unittest

class TestSWAPI(unittest.TestCase):
    def test_quest_1(self):
        expected = 20

        swapi = SWAPI()
        result = question_1(swapi, 'Revenge of the Sith')

        self.assertEqual(result, expected)

    def test_quest_2(self):
        expected = ['The Phantom Menace', 'Attack of the Clones', 'Revenge of the Sith', 'A New Hope', 'The Empire Strikes Back', 'Return of the Jedi', 'The Force Awakens']

        swapi = SWAPI()
        result = question_2(swapi)

        self.assertEqual(result, expected)

    def test_quest_3(self):
        expected = ['T-16 skyhopper', 'TIE/LN starfighter', 'Storm IV Twin-Pod cloud car']

        swapi = SWAPI()
        result = question_3(swapi, target_speed=1000)

        self.assertEqual(result, expected)


class SWAPI():
    def __init__(self):
        self.server_url = 'https://swapi.co/api/'

    def __urlRequest(self, url):
        try:
            import requests
            try:
                return requests.get(url).json()
            except Exception as e:
                print('requests library request error with URL "{}"'.format(url))
                raise SystemExit(e)
        except ImportError :
            import urllib.request
            headers = {"User-Agent": "Mozilla/5.0"}
            try:
                req = urllib.request.Request(url=url, headers=headers)
                return json.loads(urllib.request.urlopen(req).read())
            except Exception as e:
                print('urllib library request error with URL "{}"'.format(url))
                raise SystemExit(e)

    def getFilms(self, film_id=None, schema=False):
        url = self.server_url + 'films/'

        if film_id:
            url += str(film_id)
        elif schema:
            url += 'schema'
        else:
            pass

        return self.__urlRequest(url)

    def getVehicles(self, vechicle_id=None, schema=False):
        url = self.server_url + 'vehicles/'

        if vechicle_id:
            url += str(vechicle_id)
        elif schema:
            url += 'schema'
        else:
            pass

        return self.__urlRequest(url)

def question_1(swapi, target_film_name):
    films_data = swapi.getFilms()

    for film in films_data.get('results', []):
        if film.get('title') == target_film_name:
            return len(film.get('species'))

def question_2(swapi):
    films_data = swapi.getFilms()
    episodes = {}

    for film in films_data.get('results', []):
        episodes[film.get('episode_id')] = film.get('title')
    return [ episodes.get(film_id) for film_id in sorted(episodes.keys()) ]

def question_3(swapi, target_speed=0):
    vechicle_data = swapi.getVehicles()

    return [ vechicle.get('name') for vechicle in vechicle_data.get('results', []) if int(vechicle.get('max_atmosphering_speed')) > target_speed ]


def main():
    swapi = SWAPI()

    ans_1 = question_1(swapi, 'Revenge of the Sith')
    ans_2 = question_2(swapi)
    ans_3 = question_3(swapi, target_speed=1000)

    print_q = lambda index, qestion: print('Question {}: {}'.format(str(index), qestion))
    print_a = lambda index, answer: print('{}Ans {}: {}\n'.format(' '*2, index, str(answer)))
    
    print_q(1, 'How many different species appears in film-6 (Revenge of the Sith) ?')
    print_a(1, ans_1)
    print_q(2, 'Please list all the film names and sort the name by episode_id.')
    print_a(2, ans_2)
    print_q(3, 'Please find out all vehicles which max_atmosphering_speed is over 1000.')
    print_a(3, ans_3)

if __name__ == "__main__":
    main()

    # suite = (unittest.TestLoader().loadTestsFromTestCase(TestSWAPI))
    # unittest.TextTestRunner(verbosity=2).run(suite)