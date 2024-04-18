import requests
import os

#===============================================================================
# Functions to retrieve input data and submit answers
#===============================================================================

def get_cookie():
    cookie_file = 'session_cookie.txt'
    if os.path.exists(cookie_file):
        with open(cookie_file) as f:
            return f.read().strip()
    else:
        cookie = input("Veuillez entrer votre cookie de session : ").strip()
        with open(cookie_file, 'w') as f:
            f.write(cookie)
        return cookie

def get_input(year, day):
    filename = f"aoc_{year}/data/day_{day:02}.txt"
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.read()
    else:
        url = f"https://adventofcode.com/{year}/day/{day}/input"
        session_cookie = get_cookie()
        cookies = {'session': session_cookie}
        response = requests.get(url, cookies=cookies)
        with open(filename, 'w') as file:
            file.write(response.text)
        return response.text

def submit_answer(year, day, answer, level=1, send=True):
    if not send:
        print(f"Answer for day {day}, part {level}: {answer}")
        return
    session_cookie = get_cookie()
    url = f"https://adventofcode.com/{year}/day/{day}/answer"
    data = {
        'level': level,  # 1 pour la première partie, 2 pour la deuxième partie
        'answer': answer,
    }
    cookies = {'session': session_cookie}
    response = requests.post(url, cookies=cookies, data=data)
    return response.text

def setup_aoc_year(year):
    # Création du répertoire racine pour l'année
    root_dir = os.path.join(os.getcwd(), f"aoc_{year}")
    src_dir = os.path.join(root_dir, "src")
    data_dir = os.path.join(root_dir, "data")
    
    # Créer les répertoires s'ils n'existent pas
    os.makedirs(src_dir, exist_ok=True)
    os.makedirs(data_dir, exist_ok=True)
    
    # Créer un fichier .py pour chaque jour dans src
    for day in range(1, 26):  # Généralement, l'AoC va du 1er au 25 décembre
        day_file_name = f"day_{day:02}.py"
        day_file_path = os.path.join(src_dir, day_file_name)
        if not os.path.exists(day_file_path):
            with open(day_file_path, 'w') as day_file:
                day_file.write(f"""import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct

YEAR = {year}
DAY = {day}




def part_1(data):
    return ""

def part_2(data):
    return ""



if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
""")

    print(f"Advent of Code {year} setup complete in {root_dir}")

if __name__ == "__main__":
    year = input("Veuillez entrer l'année pour l'Advent of Code: ")
    setup_aoc_year(year)