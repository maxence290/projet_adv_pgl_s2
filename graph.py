import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Crée une instance de l'application Dash
app = dash.Dash(__name__)

# Exemple de données à afficher
df = pd.DataFrame({
    "Date": ["2023-03-01", "2023-03-02", "2023-03-03"],
    "Prix du Pétrole": [66.84, 67.45, 68.00],
})
df['Date'] = pd.to_datetime(df['Date'])

# Crée un graphique avec Plotly Express
fig = px.line(df, x="Date", y="Prix du Pétrole", title="Prix du pétrole")

# Défini la mise en page du Dashboard
app.layout = html.Div([
    html.H1("Dashboard des prix du pétrole"),
    dcc.Graph(figure=fig)
])

# Lancer l'application
if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=8050)
