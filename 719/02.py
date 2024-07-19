import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# 讀取 CSV 檔案
file_path = '統計表.csv'
df = pd.read_csv(file_path)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

# 創建不同的圖表
fig1 = px.scatter(df, x="地區總人口數%", y="長照機構數%", title="地區人口數 vs 長照機構數%")
fig2 = px.scatter(df, x="65歲以上長期照顧需求人數%", y="長照機構數%", title="65up長照需求人數 vs 長照機構數%")
fig3 = px.scatter(df, x="醫療院所數%", y="長照機構數%", title="醫療院所數 vs 長照機構數%")

app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='地區總人口數% vs 長照機構數%', children=[
            dcc.Graph(figure=fig1)
        ]),
        dcc.Tab(label='65歲以上長期照顧需求人數% vs 長照機構數%', children=[    
            dcc.Graph(figure=fig2)
        ]),
        dcc.Tab(label='醫療院所數% vs 長照機構數%', children=[
            dcc.Graph(figure=fig3)
        ]),
    ])
])

if __name__ == '__main__':
    app.run(debug=True)
