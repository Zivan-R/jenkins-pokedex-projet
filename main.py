import requests

def get_pkmn(pokename):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokename.lower()}"
    response = requests.get(url)
    return response.json()

def main():
    pokename = "pikachu"
    data = get_pkmn(pokename)
    print(f"Name: {data['name'].capitalize()}\nHeight: {int(data['height']) / 10}m\nWeight: {int(data['weight']) / 10}kg")

if __name__ == "__main__":
    main()