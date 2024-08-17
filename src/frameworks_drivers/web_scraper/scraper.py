import os
import urllib.request 
import bs4 as bs
import re

def scraper_example():
    """
    https://pythonprogramming.net/introduction-scraping-parsing-beautiful-soup-tutorial/
    This function demonstrates how to scrape data from a web page using BeautifulSoup library.
    It performs the following steps:
    1. Opens a URL using urllib.request.urlopen() function.
    2. Parses the HTML source code using BeautifulSoup and 'lxml' parser.
    3. Prints the title of the page.
    4. Prints the name of the title tag.
    5. Prints the value of the title tag.
    6. Prints the name of the parent tag of the title tag.
    7. Prints the first paragraph tag.
    8. Prints all the paragraph tags in the HTML source code.
    9. Prints the text content of each paragraph tag.
    10. Prints all the links in the HTML source code.
    11. Prints the entire text content of the HTML source code.
    Note: This function assumes that the URL 'https://pythonprogramming.net/parsememcparseface/' is accessible and contains the desired HTML content.
    """
    source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

    soup = bs.BeautifulSoup(source,'lxml')

    # title of the page
    print(soup.title)

    # get attributes:
    print(soup.title.name)

    # get values:
    print(soup.title.string)

    # beginning navigation:
    print(soup.title.parent.name)

    # getting specific values:
    print(soup.p)

    # finding all paragraph tags
    print(soup.find_all('p'))

    # finding all paragraph tags
    print("finding all paragraph tags")
    for paragraph in soup.find_all('p'):
        print(paragraph.string)
        print(str(paragraph.text))

    # finding all links
    print("finding all links")
    for url in soup.find_all('a'):
        print(url.get('href'))

    # print the entire text
    print(soup.get_text())

class Car:
    def __init__(self, name, year, passenger, transmission, luggage_large, luggage_small, engine, fuel):
        self.name = name
        self.year = year
        self.passenger = passenger
        self.transmission = transmission
        self.luggage_large = luggage_large
        self.luggage_small = luggage_small
        self.engine = engine
        self.fuel = fuel

    def __str__(self):
        return f"Car Name: {self.name}, Year: {self.year}, Passenger: {self.passenger}, Transmission: {self.transmission}, Luggage Large: {self.luggage_large}, Luggage Small: {self.luggage_small}, Engine: {self.engine}, Fuel: {self.fuel}"

def open_test_file() -> str:
    # 현재 파일의 경로를 가져옵니다.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 읽고자 하는 파일의 경로를 생성합니다.
    file_path = os.path.join(current_dir, 'test.html')
    # test.html 파일을 읽어들입니다.
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content

cars = []

# URL of the webpage to scrape
URL = "https://www.apexrentals.co.nz/cars"

source = urllib.request.urlopen(URL).read()
soup = bs.BeautifulSoup(source,'lxml')

# BeautifulSoup 객체를 생성합니다.
# soup = bs.BeautifulSoup(open_test_file(), 'lxml')

# id가 Content_Content_upFleet인 div 요소를 찾습니다.
content_div = soup.find('div', id='Content_Content_upFleet')

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
            if(car_img['alt'] == 'Year'):
                # print(f'year :{car_img.next_sibling.strip()}')
                year = car_img.next_sibling.strip()
            if(car_img['alt'] == 'Adult'):
                # print(f'Passenger :{car_img.next_sibling.strip()}')
                passenger = car_img.next_sibling.strip()
            if(car_img['alt'] == 'Transmission'):
                # print(f'Transmission :{car_img.next_sibling.strip()}')
                transmission = car_img.next_sibling.strip()
            if(car_img['alt'] == 'Luggage Large'):
                # print(f'Luggage Large :{car_img.next_sibling.strip()}')
                luggage_large = car_img.next_sibling.strip()
            if(car_img['alt'] == 'Luggage Small'):
                # print(f'Luggage Small :{car_img.next_sibling.strip()}')
                luggage_small = car_img.next_sibling.strip()
            if(car_img['alt'] == 'Engine'):
                # print(f'Engine :{car_img.next_sibling.strip()}')
                engine = car_img.next_sibling.strip()
            if(car_img['alt'] == 'Fuel'):
                # print(f'Fuel :{car_img.next_sibling.strip()}')
                fuel = car_img.next_sibling.strip()
        car = Car(car_name, year, passenger, transmission, luggage_large, luggage_small, engine, fuel)
        cars.append(car)
else:
    print("id가 'Content_Content_upFleet'인 div 요소를 찾을 수 없습니다.")

for car in cars:
    print(car)
