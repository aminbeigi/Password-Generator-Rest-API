import mechanicalsoup
import json
from random import randrange
from random import randint
from random import choice

API_URL = 'https://api.datamuse.com/words?rel_trg='
BROWSER = mechanicalsoup.Browser()
WORD_LST_PATH = 'wordlist.txt'

class PasswordGenerator():
    def get_word(self):
        with open(WORD_LST_PATH) as f:
            lines = f.readlines()
            random_num = randint(0, len(lines))
            random_word = lines[random_num]
            random_word = random_word[0:-1] # cull new line character
        return random_word

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

    def generate(self, password_count):
        password_lst = []
        words_lst = []
        related_words_lst = []
        output_dictionary_lst = [] # will contain list of dicts

        for i in range(0, password_count):
            for j in range(0, 2):
                random_word = self.get_word()
                words_lst.append(random_word)

                url = API_URL + f'{random_word}&max=5' # limit response length

                response = BROWSER.get(url)
                data = json.loads(response.text)

                # avoid indexing errors
                if len(data) == 0:
                    password_lst.append(random_word)
                    related_words_lst.append(random_word)
                    continue
                if len(data) < 5:
                    url = API_URL + f'{random_word}&max={len(data)}'
                    random_num = randint(0, len(data)-1)
                    related_word = data[random_num]['word']
                    related_words_lst.append(related_word)
                    continue

                random_num = randint(0, 4)
                related_word = data[random_num]['word']
                related_words_lst.append(related_word)
                password_lst.append(related_word)

            password = self.case_randomizer(''.join(password_lst))
            
            data = {
                'words': words_lst,
                'related words': related_words_lst,
                'password': password
            }

            output_dictionary_lst.append(data)
            password_lst = [] # BETTER NAME FOR THIS
            words_lst = []
            related_words_lst = []

        return output_dictionary_lst