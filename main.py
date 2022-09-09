# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from poeprofit.incursion_flips import get_incursion_flips


def fill_data_list(response):
    data = []
    for line in response['lines']:
        item = {
            'name': line['name'],
            'value': line['chaosValue']
        }
        data.append(item)
    return data


def get_vials_data():
    url = "https://poe.ninja/api/data/ItemOverview?league=Kalandra&type=Vial&language=en"
    response = requests.get(url).json()
    return fill_data_list(response)


def get_armour_data():
    url = "https://poe.ninja/api/data/ItemOverview?league=Kalandra&type=UniqueArmour&language=en"

    response = requests.get(url).json()
    return fill_data_list(response)


def get_weapon_data():
    url = "https://poe.ninja/api/data/ItemOverview?league=Kalandra&type=UniqueWeapon&language=en"

    response = requests.get(url).json()
    return fill_data_list(response)

def get_accesories_data():
    url = "https://poe.ninja/api/data/ItemOverview?league=Kalandra&type=UniqueAccessory&language=en"

    response = requests.get(url).json()
    return fill_data_list(response)

def get_jewel_data():
    url = "https://poe.ninja/api/data/ItemOverview?league=Kalandra&type=UniqueJewel&language=en"

    response = requests.get(url).json()
    return fill_data_list(response)


def get_flask_data():
    url = "https://poe.ninja/api/data/ItemOverview?league=Kalandra&type=UniqueFlask&language=en"

    response = requests.get(url).json()
    return fill_data_list(response)


def compute_flip(flip, prices):
    before_price = 0
    after_price = 0

    relevant_prices = prices[flip.type]

    for price in relevant_prices:
        if price['name'] == flip.after:
            after_price = price['value']
        if price['name'] == flip.before:
            before_price = price['value']

    vial_prices = prices["vial"]

    vial_price = 0
    for vial in vial_prices:
        if flip.vial == vial['name']:
            vial_price = vial['value']

    return after_price - before_price - vial_price


if __name__ == '__main__':
    vial_data = get_vials_data()
    accesories_data = get_accesories_data()
    armour_data = get_armour_data()
    weapon_data = get_weapon_data()
    jewel_data = get_jewel_data()
    flask_data = get_flask_data()
    prices = {
        "vial": vial_data,
        "weapon": weapon_data,
        "accesoires": accesories_data,
        "armour": armour_data,
        "jewel": jewel_data,
        "flask": flask_data
    }

    flips = get_incursion_flips()
    results = []
    for flip in flips:
        price = compute_flip(flip, prices)
        results.append({'flip': flip,
                        'price': round(price, 2)
                        })
    results.sort(key=lambda x: x['price'], reverse=True)

    for result in results:
        print(result['flip'], result['price'])
