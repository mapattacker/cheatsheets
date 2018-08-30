# https://plot.ly/python/
# https://docs.google.com/document/d/1DjWL2DxLiRaBrlD3ELyQlCBRu7UQuuWfgjv9LncNp_M/edit#heading=h.w8hlxhsxs4zj

from plotly.offline import iplot
from plotly.offline import init_notebook_mode
import plotly.graph_objs as go

init_notebook_mode(connected=True)


# LAYOUT -----------------------
    # width, height
layout = go.Layout(width=500, height=500)
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


# USING CUFFLINKS WITH PLOTLY -----------------------
import cufflinks as cf

