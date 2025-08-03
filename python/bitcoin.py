import requests
import json
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        n_bitcoins = float(sys.argv[1])

    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=bf78a31b9bf6766e64b944eebba98c89d06620cd68a57c201897210227c24897")
        data = response.json()
        bitcoin_price = float(data["data"]["priceUsd"])

        total_cost = n_bitcoins * bitcoin_price
        print(f"${total_cost:,.4f}")

    except requests.RequestException:
        print("peepee")
        sys.exit()


if __name__ == "__main__":
    main()
