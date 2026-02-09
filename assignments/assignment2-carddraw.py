# basic code taken from Andrew's lab and geeksforgeeks: https://www.geeksforgeeks.org/python/response-json-python-requests/ 
# requests fetch data from a url
import requests
def deal_five_cards():
    shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
    # fetch data from the api and store it in response
    response = requests.get(shuffle_url)
    # the json() method converts the response to a python dictionary
    data = response.json()
    print(data)
    # once drawn, parse the deck id and use it to draw 5 cards from the deck
    deck_id = data["deck_id"]
    draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
    response = requests.get(draw_url)
    data_2 = response.json()
    print(data_2)

    cards = data_2["cards"]
    return cards

# run the program and print the hand of cards
hand = deal_five_cards()
print("Your hand:")
# iterate through the hand and print the value and suit of each card
for card in hand:
    print(card["value"], "of", card["suit"])