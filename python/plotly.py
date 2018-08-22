# https://plot.ly/python/
# https://docs.google.com/document/d/1DjWL2DxLiRaBrlD3ELyQlCBRu7UQuuWfgjv9LncNp_M/edit#heading=h.w8hlxhsxs4zj

from plotly.offline import iplot
from plotly.offline import init_notebook_mode
import plotly.graph_objs as go

init_notebook_mode(connected=True)


# LAYOUT -----------------------
layout = go.Layout(
    autosize=False,
    width=500,
    height=500,
    margin=go.Margin(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4),
    paper_bgcolor='#7f7f7f',
    plot_bgcolor='#c7c7c7')
fig = go.Figure(data=data, layout=layout)
iplot(fig)


# Scatterplot
iplot([go.Scatter(x=[1, 2, 3], y=[3, 1, 6], mode='markers', name='label')])
# Barchart
iplot([go.Bar(x=[1, 2, 3], y=[3, 1, 6])])


# multiple plots
trace0 = go.Scatter(
    x = random_x, y = random_y0,
    mode = 'markers',
    name = 'markers')
trace1 = go.Scatter(
    x = random_x, y = random_y1,
    mode = 'lines+markers',
    name = 'lines+markers')
trace2 = go.Scatter(
    x = random_x, y = random_y2,
    mode = 'lines',
    name = 'lines')
data = [trace0, trace1, trace2]
iplot(data)