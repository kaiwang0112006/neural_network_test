import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[1000,5000,10000,50000,100000],
    y=[1874.529974,1678.105056,1528.060697,1369.307332,900.8799283],
    name='RMSE_tf',
    mode = 'lines+markers'
)
trace2 = go.Scatter(
    x=[1000,5000,10000,50000,100000],
    y=[1841.794214,1808.785943,1802.982112,1802.859091,1813.297946],
    name='RMSE_sgd',
    mode = 'lines+markers'
)
 
trace3 = go.Scatter(
    x=[1000,5000,10000,50000,100000],
    y=[1549.334253,1459.07353,1380.576108,1438.972875,1365.003182],
    name='RMSE_skmlp',
    mode = 'lines+markers'
)


layout= go.Layout(
    title= 'RMSE-step',
    hovermode= 'closest',
    xaxis= dict(
        title= 'Step',
    ),
    yaxis=dict(
        title= 'RMSE',
    ),
    showlegend= True
)

data = [trace1, trace2, trace3]

fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='RMSE-step')

# result go to : https://plot.ly/~kaiwang0112006/6/rmse-step/