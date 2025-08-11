import requests
import os
from dotenv import load_dotenv

load_dotenv()
WORKING_DIR = os.getenv("WORKING_DIR")


def get_cookie():
    cookie_file = f"{WORKING_DIR}/session_cookie.txt"
    if os.path.exists(cookie_file):
        with open(cookie_file) as f:
            return f.read().strip()
    else:
        cookie = input("Veuillez entrer votre cookie de session : ").strip()
        with open(cookie_file, "w") as f:
            f.write(cookie)
        return cookie


def get_input(year, day):
    filename = f"{WORKING_DIR}/aoc_{year}/data/day_{day:02}.txt"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            input = file.read()
            return input[:-1:] if input[-1] == "\n" else input
    else:
        url = f"https://adventofcode.com/{year}/day/{day}/input"
        session_cookie = get_cookie()
        cookies = {"session": session_cookie}
        # print(f"Utilisation des cookies : {cookies}")
        # print(f"Requête GET vers : {url}")
        response = requests.get(url, cookies=cookies)
        # print(f"Réponse reçue : {response.text}")
        with open(filename, "w") as file:
            file.write(response.text)
        return response.text[:-1:] if response.text[-1] == "\n" else response.text


def submit_answer(year, day, answer, level=1, send=True):
    if not send:
        print(f"Answer for day {day}, part {level}: {answer}")
        return
    session_cookie = get_cookie()
    url = f"https://adventofcode.com/{year}/day/{day}/answer"
    data = {
        "level": level,  # 1 for the first part, 2 for the second
        "answer": answer,
    }
    cookies = {"session": session_cookie}
    response = requests.post(url, cookies=cookies, data=data)
    return response.text


def setup_aoc_year(year):
    # Création du répertoire racine pour l'année
    root_dir = os.path.join(os.getcwd(), f"{WORKING_DIR}/aoc_{year}")
    src_dir = os.path.join(root_dir, "src")
    data_dir = os.path.join(root_dir, "data")

    if not os.path.exists(root_dir):
        # print(f"Directory for aoc {year} already exists. Exiting.")
        # return
        # Créer les répertoires s'ils n'existent pas
        os.makedirs(src_dir, exist_ok=True)
        os.makedirs(data_dir, exist_ok=True)

    # Créer un fichier .py pour chaque jour dans src

    for day in range(1, 26):
        day_file_name = f"day_{day:02}.py"
        day_file_path = os.path.join(src_dir, day_file_name)
        if not os.path.exists(day_file_path):
            with open(day_file_path, "w") as day_file:
                day_file.write(
                    f"""import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = {year}
DAY = {day}

data = aoct.get_input(YEAR, DAY)

res = 0

# # graphs
# V = list(set(re.findall(r'[a-z]{"{2}"}', data)))
# V_T = {"{V[i] : i for i in range(len(V))}"}
# edges = [(V_T[a], V_T[b]) for a, b in re.findall(r'([a-z]{"{2}"})\\-([a-z]{"{2}"})', data)]
# G = ig.Graph(edges=edges, directed=False)
# # edges = [(V_T[a], V_T[b], int(c)) for a, b, c in re.findall(r'([a-z]{"{2}"})\\-([a-z]{"{2}"})\\-(\\d+)', data)]
# # G = ig.Graph(edges=[(s,t) for s,t,_ in edges], directed=False, edge_attrs={'{"weight": [w for _,_,w in edges]}'})

#data = as_grid(data)
for l in data.split("\\n"):
    l = nums(l)

print(res)
"""
                )

    print(f"Advent of Code {year} setup complete in {root_dir}")


def create_env_if_not_exists():
    current_abs_path = os.path.abspath(__file__)
    if not os.path.exists(".env"):
        with open(".env", "w") as f:
            f.write(f"WORKING_DIR={os.path.dirname(current_abs_path)}\n")
        print(".env file created")


if __name__ == "__main__":
    create_env_if_not_exists()
    year = input("Enter the year for Advent of Code: ")
    setup_aoc_year(year)
