import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'



def get_big_mac_price_by_year(year,country_code):
    df = pd.read_csv(big_mac_file)
    df = df[(df['date'].str.startswith(str(year))) & (df['iso_a3'].str.lower() == country_code)]
    return round(df['dollar_price'].mean(), 2) if not df.empty else "No data"
# My buddy Anderson helped a lot with this code. I have an extremely hard time writing this one
# ChatGPT helped explain some things. Also it helped simplify the code


def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)
    df = df[df['iso_a3'].str.lower() == country_code]
    return round(df['dollar_price'].mean(), 2) if not df.empty else "No data"
# ChatGPT wrote these lines
# These lines of code made sense to me 

def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    df = df[df['date'].str.startswith(str(year))]
    if df.empty:
        return "No data"
    row = df.loc[df['dollar_price'].idxmin()]
    return f"{row['name']}({row['iso_a3']}): ${round(row['dollar_price'], 2)}"
# ChatGPT wrote this as well
# Anderson had to break down a lot of this. I am still a bit confused
# Got some help rewriting code


def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    df = df[df['date'].str.startswith(str(year))]
    if df.empty:
        return "No data"
    row = df.loc[df['dollar_price'].idxmax()]
    return f"{row['name']}({row['iso_a3']}): ${round(row['dollar_price'], 2)}"
# This was another part that had me confused
# Rewrote code here too
# ChatGPT wrote this

if __name__ == "__main__":
    year = input("Enter a year: ")
    country = input("Enter a country code: ").lower()
    print("\nResults:")
    print(f"- Avg price in {year} for {country.upper()}: {get_big_mac_price_by_year(year, country)}")
    print(f"- Avg price for {country.upper()}: {get_big_mac_price_by_country(country)}")
    print(f"- Cheapest Big Mac in {year}: {get_the_cheapest_big_mac_price_by_year(year)}")
    print(f"- Most expensive Big Mac in {year}: {get_the_most_expensive_big_mac_price_by_year(year)}")
# This is probably the only thing that i completely understood
# My CS friend helped me write this
# ChatGPT helped very little here

# Sorry for using AI

# OpenAI. (2025). ChatGPT 4.o (Mar 24 version) [Large language model]. 
#   https://chat.openai.com/chat