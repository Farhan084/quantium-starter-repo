import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

df = pd.read_csv("output.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

daily = df.groupby("date", as_index=False)["sales"].sum()

fig = px.line(
    daily,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Total Sales ($)"},
)
fig.add_vline(
    x=pd.Timestamp("2021-01-15").timestamp() * 1000,
    line_dash="dash",
    line_color="red",
    annotation_text="Price Increase",
    annotation_position="top left",
)

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser"),
    dcc.Graph(figure=fig),
])

if __name__ == "__main__":
    app.run(debug=True)
