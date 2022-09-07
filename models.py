from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base


base = declarative_base()


class Apartment(base):

    __tablename__ = 'apartment'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    city = Column(String)
    date = Column(DateTime)
    image = Column(String)
    beds = Column(String)
    price = Column(Float, nullable=True)
    price_ccy = Column(String, nullable=True)
    link = Column(String)

    def __init__(self, id, title, description, city, date, image, beds, price, price_ccy, link):
        self.id = id
        self.title = title
        self.description = description
        self.city = city
        self.date = date
        self.image = image
        self.beds = beds
        self.price = price
        self.price_ccy = price_ccy
        self.link = link
