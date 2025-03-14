#!/bin/bash

# URL de la page à scraper
URL="https://www.investing.com/commodities/crude-oil"

# Scraper la page et extraire le prix du pétrole
PRICE=$(curl -s "$URL" | grep -oP '(?<=data-test="instrument-price-last">)[0-9]+(\.[0-9]+)?')

# Vérifier si le prix a bien été extrait
if [[ -n "$PRICE" ]]; then
    echo "$(date +'%Y-%m-%d %H:%M:%S'), $PRICE" >> oil_prices.csv
    echo "Prix du pétrole : $PRICE USD"
else
    echo "Erreur : Impossible d'extraire le prix."
fi
