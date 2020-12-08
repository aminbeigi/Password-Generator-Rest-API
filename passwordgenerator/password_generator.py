import mechanicalsoup
import json
from random import randrange
from random import randint
from random import choice

API_URL = 'https://api.datamuse.com/words?rel_trg='

WORD_LST = ['cat', 'window', 'dog', 'horse', 'barn']

class PasswordGenerator():
    def randomizer(self, string):
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

    def generate(self, password_num):
        password_lst = []
        output_word_lst = []
        output_data_lst = []

        for i in range(0, password_num):
            for i in range(0, 2):
                random_word = choice(WORD_LST)
                output_word_lst.append(random_word)
                url = API_URL + f'{random_word}'

                browser = mechanicalsoup.Browser()
                response = browser.get(url)
                data = json.loads(response.text)
                random_num = randrange(len(data)) # randrange throws ValueError here if data = 0
                password_lst.append(data[random_num]['word'])

                password = self.randomizer(''.join(password_lst))
            
            data = {
                'words': output_word_lst,
                'passwords': password
            }

            output_data_lst.append(data)
            password_lst = []
            output_word_lst = []

        return output_data_lst