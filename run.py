import os
import csv

from api.bazaraki_api import BazarakiApi
from scrapper.scrapper import Scrapper
from watcher.cars_ads_manager import CarAdsManager

def main():
    manager = CarAdsManager(BazarakiApi(), Scrapper())
    page = 1
    result = {}
    while True:
        ads = manager.get_cars_ads(page)
        last = ads[-1]
        if result.get(last.id) != None:
            break
        for item in ads:
            result[item.id] = item
        page = page + 1
    
    write_to_csv(list(result.values()))

def write_to_csv(results: list):
    with open('mazda_cx30_ads.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        fields = ["Name", "Brand", "Model", "Year", "Cost", "Mileage", "Power", "Fuel", "Location", "URL"]
        writer.writerow(fields)

        for item in results:
            title = item.title
            title = title.replace(item.brand,"")
            title = title.replace(item.model,"")
            title_items = title.split(" ")
            year = title_items[-1]
            power = title_items[-2]

            description_items = item.description.split(", ")
            mileage = description_items[0]
            fuel = description_items[-1]

            writer.writerow([item.title, item.brand, item.model, year, item.price, mileage, power, fuel, item.location, item.url])
 

if __name__ == "__main__":
    main()