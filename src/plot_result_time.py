import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[1000,5000,10000,50000,100000],
    y=[97.78805447,244.428334,391.4800842,531.1620238,644.0667562],
    name='time_tf',
    mode = 'lines+markers'
)
trace2 = go.Scatter(
    x=[1000,5000,10000,50000,100000],
    y=[20.76813388,105.6043713,207.5891514,1034.064328,2066.19803],
    name='time_sgd',
    mode = 'lines+markers'
)
 
trace3 = go.Scatter(
    x=[1000,5000,10000,50000,100000],
    y=[118.4438679,358.4222879,548.1600642,2586.589987,5058.723876],
    name='time_skmlp',
    mode = 'lines+markers'
)


layout= go.Layout(
    title= 'time-step',
    hovermode= 'closest',
    xaxis= dict(
        title= 'Step',
    ),
    yaxis=dict(
        title= 'time(s)',
    ),
    showlegend= True
)

data = [trace1, trace2, trace3]

fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='time-step')

# result go to https://plot.ly/~kaiwang0112006/8/time-step/