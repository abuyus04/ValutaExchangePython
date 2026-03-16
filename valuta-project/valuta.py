import argparse
import requests
import os
from dotenv import load_dotenv

#loader dotenv filen
load_dotenv()

def save_api_key(key):
    with open(".env", "w") as f:
        f.write(f"API_KEY={key}")

    
def get_api_key(args):
    if args.key:
        save_api_key(args.key)
        return args.key
    else:
        return os.getenv("API_KEY")
    
def convert_currency(api_key, amount, from_currency, to_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"

    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        print("Fejl i API kald")
        return
    
    rate = data["conversion_rates"].get(to_currency)
    
    if not rate:
        print("Valuta ikke fundet")
        return
    
    result = amount * rate
    print(f"{amount} {from_currency} = {result:.2f} {to_currency}")

def main():
    parser = argparse.ArgumentParser(description="Valuta omregner CLI")
    
    parser.add_argument("--key", help="API key til exchangerate-api")
    parser.add_argument("--amount", type=float, help="Beløb")
    parser.add_argument("--from_currency", help="Fra valuta (ex: USD)")
    parser.add_argument("--to_currency", help="Til valuta (ex: DKK)")
    
    args = parser.parse_args()
    
    api_key = get_api_key(args)
    
    if not api_key:
        print("Ingen API key fundet. Brug --key første gang.")
        return
    
    if args.amount and args.from_currency and args.to_currency:
        convert_currency(api_key, args.amount, args.from_currency.upper(), args.to_currency.upper())
    else:
        print("Du skal angive --amount --from_currency --to_currency")

if __name__ == "__main__":
    main()