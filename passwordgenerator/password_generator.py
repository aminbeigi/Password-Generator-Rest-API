import mechanicalsoup
import json
from random import randrange
from random import randint
from random import choice

API_URL = 'https://api.datamuse.com/words?rel_trg='
BROWSER = mechanicalsoup.Browser()
WORD_LST = ['cat', 'window', 'dog', 'horse', 'barn']

class PasswordGenerator():
    def case_randomizer(self, string):
        password = ''
        for char in string:
            case = randint(0, 2)
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
                random_word = choice(WORD_LST)
                output_word_lst.append(random_word)
                url = API_URL + f'{random_word}' + '&max=1'

                response = BROWSER.get(url)
                data = json.loads(response.text)
                password_lst.append(data[0]['word'])

                password = self.case_randomizer('-'.join(password_lst))
            
            data = {
                'words': output_word_lst,
                'passwords': password
            }

            output_data_lst.append(data)
            password_lst = []
            output_word_lst = []

        return output_data_lst