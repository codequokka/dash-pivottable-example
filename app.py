# You can run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import sys
import dash
import dash_html_components as html
import dash_pivottable
import data

if len(sys.argv) >= 2:
    debug = True
else:
    debug = False

pop_data = data.get_pop_data(
    population_src_file="./data/WPP2019_TotalPopulationBySex.csv",
    locations_src_file="./data/WPP2019_F01_LOCATIONS.XLSX",
    debug=debug,
)

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="世界人口予測", style={"textAlign": "center"}),
        dash_pivottable.PivotTable(
            data=pop_data,
            cols=["Time"],
            rows=["GeoRegName"],
            vals=["Population"],
            hiddenFromDragDrop=["Population"],
            hiddenFromAggregators=[
                "Time",
                "GeoRegName",
                "SubRegName",
                "Location",
                "PopType",
            ],
            aggregatorName="Sum",
        ),
    ]
)

if __name__ == "__main__":
    if not debug:
        app.run_server(host="0.0.0.0", port=8050)
    else:
        app.run_server(host="0.0.0.0", port=8050, debug=True)
