import requests
import json

def get_most_relevant_items_for_category(category):
    url = f"https://api.mercadolibre.com/sites.MLA/search?category={category}#json"
    response = requests.get(url).text
    response = json.loads(response)
    print(response)


def main():
    CATEGORY = "MLA1577"
    get_most_relevant_items_for_category(CATEGORY)


main()