from typing import List

import os
import urllib.request
import bs4 as bs

# URL of the webpage to scrape
URL = "https://www.apexrentals.co.nz/cars"


def scrap_car_reservation_info():
    reservation_info_url = "https://www.apexrentals.co.nz/reservations/vehicles"
    source = urllib.request.urlopen(reservation_info_url).read()
    soup = bs.BeautifulSoup(source, 'lxml')

    # content_div = soup.find('div', id='Content_Content_upFleet')

    print(soup)


def scrap_car_list():
    """
    Runs the web scraper to get the list of cars available for rent.
    """
    source = urllib.request.urlopen(URL).read()
    soup = bs.BeautifulSoup(source, 'lxml')

    # id가 Content_Content_upFleet인 div 요소를 찾습니다.
    content_div = soup.find('div', id='Content_Content_upFleet')

    cars = []

    if content_div:
        # 해당 div 요소 아래에 있는 모든 class가 12u인 div 요소를 찾습니다.
        car_divs = content_div.find_all('div', class_='12u')

        # 각 car_div에서 class가 dvCarHeadingSub인 div 요소를 찾고, 그 안의 h2 요소를 가져옵니다.
        for car_div in car_divs:
            car_name = None
            year = None
            passenger = None
            transmission = None
            luggage_large = None
            luggage_small = None
            engine = None
            fuel = None

            car_heading_sub = car_div.find('div', class_='dvCarHeadingSub')
            if car_heading_sub:
                car_name_tag = car_heading_sub.find('h2')
                if car_name_tag:
                    car_name = car_name_tag.get_text(strip=True)
                    # print(f"Car Name: {car_name}")
                else:
                    print("h2 요소를 찾을 수 없습니다.")
            else:
                pass
                # print("class가 'dvCarHeadingSub'인 div 요소를 찾을 수 없습니다.")
            car_imgs = car_div.find_all('img', class_='imgIcon')
            for car_img in car_imgs:
                if (car_img['alt'] == 'Year'):
                    # print(f'year :{car_img.next_sibling.strip()}')
                    year = car_img.next_sibling.strip()
                if (car_img['alt'] == 'Adult'):
                    # print(f'Passenger :{car_img.next_sibling.strip()}')
                    passenger = car_img.next_sibling.strip()
                if (car_img['alt'] == 'Transmission'):
                    # print(f'Transmission :{car_img.next_sibling.strip()}')
                    transmission = car_img.next_sibling.strip()
                if (car_img['alt'] == 'Luggage Large'):
                    # print(f'Luggage Large :{car_img.next_sibling.strip()}')
                    luggage_large = car_img.next_sibling.strip()
                if (car_img['alt'] == 'Luggage Small'):
                    # print(f'Luggage Small :{car_img.next_sibling.strip()}')
                    luggage_small = car_img.next_sibling.strip()
                if (car_img['alt'] == 'Engine'):
                    # print(f'Engine :{car_img.next_sibling.strip()}')
                    engine = car_img.next_sibling.strip()
                if (car_img['alt'] == 'Fuel'):
                    # print(f'Fuel :{car_img.next_sibling.strip()}')
                    fuel = car_img.next_sibling.strip()
            car = Car(car_name, year, passenger, transmission,
                      luggage_large, luggage_small, engine, fuel)
            cars.append(car)
    else:
        print("id가 'Content_Content_upFleet'인 div 요소를 찾을 수 없습니다.")
    return cars


if __name__ == '__main__':
    # scrap_car_list()
    scrap_car_reservation_info()
