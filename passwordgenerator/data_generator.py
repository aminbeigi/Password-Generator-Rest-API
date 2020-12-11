import mechanicalsoup
import json
from random import randrange, randint, choice

"""Generate a data dict based on random words or user inputted words"""

API_URL = 'https://api.datamuse.com/words?rel_trg='
BROWSER = mechanicalsoup.Browser()
WORD_LST_PATH = 'wordlist.txt'
MAX_API_RESPONSE = 5

class DataGenerator():
    def get_word(self):
        with open(WORD_LST_PATH) as f:
            lines = f.readlines()
            random_num = randint(0, len(lines))
            random_word = lines[random_num]
            random_word = random_word[0:-1] # cull new line character
        return random_word
    
    # parse http get request into list
    def parse_string(self, string):
        # e.g. cat&dog&wolf
        word_lst = []

        if string.count('&') == 0:
            word_lst.append(string)     
            return word_lst

        for i in range(0, string.count('&')):
            word = string[0:string.find('&')]
            word_lst.append(word)
            string = string.removeprefix(word + '&') # remove word and &
        word_lst.append(string)
        return word_lst

    def case_randomizer(self, string):
        password = ''
        for char in string:
            case = randint(0, 2)
            if case == 0:
                password += char.upper()
            elif case == 1:
                password += char.lower()	
            else:
                if char == 'a':
                    password += '@'
                elif char == 'e':
                    password += '3'
                elif char == 'i' or char == 'l':
                    password += choice('1!|')
                elif char == 'o':
                    password += choice('0.')
                elif char == 'c':
                    password += choice('<(')	
                elif char == 's':
                    password += '$'
                else:
                    password += char
        return password

    def generate_random(self, limit=5):

        output_dictionary_lst = [] # will contain list of dicts
        number_of_words_in_each_dict = 2
        for i in range(0, limit):
            # reset for new dict
            output_string = ''
            words_lst = []
            related_words_lst = []
            for j in range(0, number_of_words_in_each_dict):
                random_word = self.get_word()
                words_lst.append(random_word)
                url = API_URL + f'{random_word}&max={MAX_API_RESPONSE}' # limit response length
                response = BROWSER.get(url)
                data = json.loads(response.text)

                # no data for that word
                if len(data) == 0:
                    output_string += random_word
                    related_words_lst.append(random_word)
                    continue

                # avoid indexing errors
                if len(data) < MAX_API_RESPONSE:
                    url = API_URL + f'{random_word}&max={len(data)}'
                    random_num = randint(0, len(data)-1)
                else:
                    random_num = randint(0, MAX_API_RESPONSE-1)
                    
                related_word = data[random_num]['word']
                related_words_lst.append(related_word)
                output_string += related_word

            password = self.case_randomizer(output_string)
            data = {
                'words': words_lst,
                'related words': related_words_lst,
                'password': password
            }

            output_dictionary_lst.append(data)

        return output_dictionary_lst

    def generate_custom(self, limit, user_string):
        words_lst = self.parse_string(user_string)

        related_words_lst = []
        output_dictionary_lst = []

        for i in range(0, limit):
            output_string = ''
            for j in range(0, len(words_lst)):

                url = API_URL + f'{words_lst[j]}&max={MAX_API_RESPONSE}' # limit response length
                response = BROWSER.get(url)
                data = json.loads(response.text)

                # avoid indexing errors
                if len(data) == 0:
                    output_string += words_lst[j]
                    related_words_lst.append(words_lst[j])
                    continue
                if len(data) < MAX_API_RESPONSE:
                    url = API_URL + f'{words_lst[j]}&max={len(data)}'
                    random_num = randint(0, len(data)-1)
                else:
                    random_num = randint(0, MAX_API_RESPONSE-1)
                    
                related_word = data[random_num]['word']
                related_words_lst.append(related_word)
                output_string += related_word

            password = self.case_randomizer(output_string)
            
            data = {
                'words': words_lst,
                'related words': related_words_lst,
                'password': password
            }

            output_dictionary_lst.append(data)
            related_words_lst = []

        return output_dictionary_lst