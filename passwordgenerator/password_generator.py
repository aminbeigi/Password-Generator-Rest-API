import mechanicalsoup
import json
from random import randrange
from random import randint
from random import choice

API_URL = 'https://api.datamuse.com/words?rel_trg='
BROWSER = mechanicalsoup.Browser()
WORD_LST = ['cat', 'window', 'dog', 'horse', 'barn']
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
            case = randint(0, 1)
            if case == 0:
                password += char.upper()
            elif case == 1:
                password += char.lower()
        return password

    def generate(self, password_count):
        password_lst = []
        output_word_lst = []
        output_data_lst = []

        for i in range(0, password_count):
            for j in range(0, 2):
                random_word = self.get_word()
                output_word_lst.append(random_word)

                url = API_URL + f'{random_word}&max=5' # limit response length

                response = BROWSER.get(url)
                data = json.loads(response.text)

                # avoid indexing errors
                if len(data) == 0:
                    password_lst.append(random_word)

                random_num = randint(0, 4)
                password_lst.append(data[random_num]['word'])

            password = self.case_randomizer('-'.join(password_lst))
            
            data = {
                'words': output_word_lst,
                'password': password
            }

            output_data_lst.append(data)
            password_lst = []
            output_word_lst = []

        return output_data_lst