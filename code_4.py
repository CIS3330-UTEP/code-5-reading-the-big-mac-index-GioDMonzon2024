import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'



def get_big_mac_price_by_year(year,country_code):
    df = pd.read_csv(big_mac_file)
    # I ripped this line of code above from your in-class "demo_01_pd_query.py"
    query = f"(iso_a3 == 'ARG')"
    arg_df = df.query(query)

    for index, row in arg_df.iterrows():
        print(index)
        print(row)


def get_big_mac_price_by_country(country_code):


def get_the_cheapest_big_mac_price_by_year(year):



def get_the_most_expensive_big_mac_price_by_year(year):


if __name__ == "__main__":
    get_big_mac_price_by_year(2008, 'arg')