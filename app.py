import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, callback, Output, Input

df = pd.read_csv("output.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

PRICE_INCREASE = pd.Timestamp("2021-01-15").timestamp() * 1000

def make_figure(region):
    if region == "all":
        filtered = df.groupby("date", as_index=False)["sales"].sum()
    else:
        filtered = df[df["region"] == region].groupby("date", as_index=False)["sales"].sum()

    fig = px.line(
        filtered,
        x="date",
        y="sales",
        labels={"date": "Date", "sales": "Total Sales ($)"},
        color_discrete_sequence=["#e91e8c"],
    )
    fig.add_vline(
        x=PRICE_INCREASE,
        line_dash="dash",
        line_color="#ff6b6b",
        annotation_text="Price Increase (15 Jan 2021)",
        annotation_position="top left",
        annotation_font_color="#ff6b6b",
    )
    fig.update_layout(
        plot_bgcolor="#1e1e2e",
        paper_bgcolor="#1e1e2e",
        font_color="#cdd6f4",
        xaxis=dict(gridcolor="#313244"),
        yaxis=dict(gridcolor="#313244"),
    )
    return fig

app = Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#181825",
        "minHeight": "100vh",
        "padding": "40px",
        "fontFamily": "Segoe UI, sans-serif",
    },
    children=[
        html.H1(
            "Pink Morsel Sales Visualiser",
            style={
                "color": "#e91e8c",
                "textAlign": "center",
                "marginBottom": "8px",
                "fontSize": "2.4rem",
                "letterSpacing": "1px",
            },
        ),
        html.P(
            "Exploring sales before and after the January 2021 price increase",
            style={"color": "#a6adc8", "textAlign": "center", "marginBottom": "30px"},
        ),
        html.Div(
            style={"textAlign": "center", "marginBottom": "24px"},
            children=[
                html.Label(
                    "Filter by Region:",
                    style={"color": "#cdd6f4", "marginRight": "16px", "fontWeight": "bold"},
                ),
                dcc.RadioItems(
                    id="region-radio",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "South", "value": "south"},
                        {"label": "East", "value": "east"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    style={"color": "#cdd6f4"},
                    inputStyle={"marginRight": "6px"},
                    labelStyle={"marginRight": "20px", "fontSize": "1rem"},
                ),
            ],
        ),
        html.Div(
            style={
                "backgroundColor": "#1e1e2e",
                "borderRadius": "12px",
                "padding": "16px",
                "boxShadow": "0 4px 24px rgba(0,0,0,0.4)",
            },
            children=[dcc.Graph(id="sales-chart")],
        ),
    ],
)

@callback(Output("sales-chart", "figure"), Input("region-radio", "value"))
def update_chart(region):
    return make_figure(region)

if __name__ == "__main__":
    app.run(debug=True)
