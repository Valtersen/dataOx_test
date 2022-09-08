import gspread as gspread
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
import database_config as config
from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials
import pandas


engine = create_engine(
    f"postgresql://{config.user}:{config.password}@{config.host}:{config.port}/{config.db_name}")

session = sessionmaker(bind=engine)()

scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "v_credentials.json", scope)
client = gspread.authorize(credentials)

# sheet = client.create("Apartments")

sheet = client.open("Apartments").sheet1
sql = "SELECT * FROM apartment"

df = pandas.read_sql(sql, engine)

set_with_dataframe(sheet, df)
