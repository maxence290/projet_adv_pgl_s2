import dash
from dash import dcc, html, Output, Input
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

# Définition du layout avec un graphique et un Interval pour rafraîchir
app.layout = html.Div([
    html.H1("Dashboard - Prix du Pétrole"),
    dcc.Graph(id='oil-price-graph'),
    # Interval de 5 minutes = 300000 millisecondes
    dcc.Interval(
        id='interval-component',
        interval=300000,  
        n_intervals=0
    )
])

# Callback pour mettre à jour le graphique à chaque intervalle
@app.callback(
    Output('oil-price-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph(n):
    try:
        # Lecture du fichier CSV
        # On suppose que le CSV a été généré sans header (modifie si besoin)
        # Par exemple, chaque ligne du CSV : "2025-03-14 14:09:13, 66.84"
        df = pd.read_csv('oil_prices.csv', header=None, names=["Time", "Price"])
        # Conversion de la colonne Time en datetime pour une meilleure gestion sur l'axe x
        df["Time"] = pd.to_datetime(df["Time"].str.strip())
        # Conversion de Price en numérique (en supprimant les espaces superflus)
        df["Price"] = pd.to_numeric(df["Price"].str.strip(), errors='coerce')
        # Création du graphique en ligne
        fig = px.line(df, x="Time", y="Price", title="Historique du Prix du Pétrole")
    except Exception as e:
        # En cas d'erreur de lecture, affiche un graphique vide avec le message d'erreur
        fig = px.line(title=f"Erreur lors du chargement des données: {e}")
    return fig

if __name__ == '__main__':
    # Pour que le dashboard soit accessible sur toutes les interfaces de la VM
    app.run_server(debug=True, host='0.0.0.0', port=8050)
