'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_info() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("Rockruff")
    print(poke_info)
    return

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # TODO: Clean the Pokemon name parameter
    pokemon_name = pokemon_name.lower().strip()

    # TODO: Build a clean URL and use it to send a GET request
    url = f"{POKE_API_URL}{pokemon_name}/"

    # TODO: If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
    response =requests.get(url)

    # TODO: If the GET request failed, print the error reason and return None
    if response.status_code== 200:
        pokemon_data =response.json()
        return pokemon_data
    else:
        print(f"failed to retrieve data: {response.status_code} - {response.reason}")


    return None

if __name__ == '__main__':
    main()