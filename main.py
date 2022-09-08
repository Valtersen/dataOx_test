import datetime
import time
from bs4 import BeautifulSoup
import requests
from sqlalchemy import *
from sqlalchemy import exc
from sqlalchemy.orm import sessionmaker
from models import Apartment, base
import database_config as config


if __name__ == '__main__':

    engine = create_engine(f"postgresql://{config.user}:{config.password}@{config.host}:{config.port}/{config.db_name}")

    base.metadata.create_all(engine)

    page = 1
    format_str = '%d/%m/%Y'
    while True:

        if page == 1:
            response = requests.get(f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{page}/c37l1700273')
        else:
            response = requests.get(f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{page}/c37l1700273',
                                    allow_redirects=False)
        if response.status_code != 200:
            break

        else:
            parsed = BeautifulSoup(response.text, "html.parser")

            for ad in parsed.find_all('div', 'search-item'):
                session = sessionmaker(bind=engine)()

                ad_id = ad['data-listing-id']
                title = ad.find('a', class_='title').text.strip()
                desc = ad.find('div', class_='description').text.replace("\n", "").strip()
                city = ad.find('div', class_='location').find("span").text.strip()

                date_raw = ad.find('span', class_='date-posted').text.strip()
                try:
                    date = datetime.datetime.strptime(date_raw, format_str)
                except (ValueError, TypeError):
                    date = datetime.datetime.today()

                try:
                    image_url = ad.find('div', class_='image').find('img')['data-src'].strip()
                except KeyError:
                    image_url = ad.find('div', class_='image').find('img')['src'].strip()

                beds = ad.find('span', class_='bedrooms').text.replace("Beds:", "").strip()

                price_raw = ad.find('div', class_='price').text.strip()

                if price_raw == 'Please Contact':
                    price_ccy, price = None, None
                else:
                    price_ccy = price_raw[0]
                    try:
                        price = float(price_raw[1:].replace(',', ''))
                    except ValueError:
                        price = float(price_raw[1:8].replace(',', ''))

                link = 'https://www.kijiji.ca' + ad.find('a', class_='title', href=True)['href'].strip()

                try:
                    apartment = Apartment(ad_id, title, desc, city, date, image_url, beds, price, price_ccy, link)
                    session.add(apartment)
                    session.commit()
                except exc.IntegrityError:
                    session.rollback()
                    continue
                else:
                    session.close()

            page += 1
            time.sleep(1)
