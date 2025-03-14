#!/bin/bash
cd /home/maxence/projet_adv_pgl_s2
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# URL de la page à scraper
URL="https://www.investing.com/commodities/crude-oil"

# Scraper la page et extraire le prix du pétrole
PRICE=$(curl -s "$URL" | grep -oP '(?<=data-test="instrument-price-last">)[0-9]+\.[0-9]+')

# Récupérer la date actuelle
DATE=$(date +"%Y-%m-%d %H:%M:%S")

# Vérifier si le prix a bien été extrait
if [[ -n "$PRICE" ]]; then
    echo "$DATE, $PRICE" >> /home/maxence/projet_adv_pgl_s2/oil_prices.csv
    echo "Prix du pétrole : $PRICE USD"
else
    echo "Erreur : Impossible d'extraire le prix."
fi
