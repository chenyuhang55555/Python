import tushare as ts
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go

df = ts.get_stock_basics()

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children="PE"),
    html.Div(children="2017年10月13收瘟涨幅排名前50的PE"),
    dcc.Graph(
    id="pe-graph",
    figure={
        "data": [go.Bar(x=df.head(50)["name"].values, y=df.head(50)["pe"].values,name="PE")],
        "layont":go.Layout (title="PE排名")
        })
])

if __name__ == '__main__':
    app.run_server(debug=True)
