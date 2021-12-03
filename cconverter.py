import json
import requests

def update_cache_rate(cache, currencies):
    r = requests.get(f"http://www.floatrates.com/daily/{cur_from}.json")
    data = json.loads(r.text)
    for cur in currencies:
        if cur in data:
            cache[cur] = data[cur]["rate"]

cache = {}

cur_from = input().lower()
update_cache_rate(cache, ["usd", "eur"])

while True:
    cur_to = input().lower()
    if cur_to == "":
        break
    amount_of_money = float(input())
    print("Checking the cache...")
    if cur_to in cache:
        print("Oh! It is in the cache!")
        exchange_rate = cache[cur_to]
    else:
        print("Sorry, but it is not in the cache!")
        update_cache_rate(cache, [cur_to])

    result = round(amount_of_money * cache[cur_to], 2)
    print(f"You received {result} {cur_to.upper()}.")