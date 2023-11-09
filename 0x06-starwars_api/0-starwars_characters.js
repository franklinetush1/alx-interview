#!/usr/bin/node
import requests
import sys

def get_movie_characters(movie_id):
    url = f"https://swapi.dev/api/films/{movie_id}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        film_data = response.json()
        characters = film_data['characters']
        
        for character_url in characters:
            character_response = requests.get(character_url)
            if character_response.status_code == 200:
                character_data = character_response.json()
                print(character_data['name'])
            else:
                print(f"Failed to fetch character data: {character_response.status_code}")
    else:
        print(f"Failed to fetch film data: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <movie_id>")
    else:
        movie_id = sys.argv[1]
        get_movie_characters(movie_id)
