# https://plot.ly/python/
# https://docs.google.com/document/d/1DjWL2DxLiRaBrlD3ELyQlCBRu7UQuuWfgjv9LncNp_M/edit#heading=h.w8hlxhsxs4zj

from plotly.offline import iplot
from plotly.offline import init_notebook_mode
import plotly.graph_objs as go

init_notebook_mode(connected=True)



# BASICS -----------------------
# define layout
# define chart/data, keep in square brackets
# combine both into fig
# iplot them out
layout = go.Layout(width=500, \
                   height=500, \
                   title='Confusion Matrix', \
                   font=dict(size=8))
data = go.Heatmap(z=x,x=title,y=title)
fig = go.Figure(data=[data], layout=layout)
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


## COOKIE CUTTERS
# -----------------

# TIME-SERIES LINE WITH VOLUME STOCK DATA
apple = dfm[dfm['assetCode']=='AAPL.O']

data1 = go.Scatter(
          x=apple.time,
          y=apple['close'],
          name='Price')

data2 = go.Bar(
            x=apple.time,
            y=apple.volume,
            name='Volume',
            yaxis='y2')

data = [data1, data2]

# set double y-axis
layout = go.Layout(
    title='Closing Price & Volume for AAPL.O',
    yaxis=dict(
        title='Price'
    ),
    yaxis2=dict(
        overlaying='y',
        side='right',
        range=[0, 1500000000], #increase upper range so that the volume bars are short
        showticklabels=False,
        showgrid=False
    )
)

fig = go.Figure(data=data,layout=layout)

iplot(fig)


# CANDLESTICK
data = [go.Candlestick(x=apple.time,
                       open=apple.open,
                       high=apple.open, #no data so used another column
                       low=apple.close, #no data so used another column
                       close=apple.close)]

# remove range slider
layout = go.Layout(
    xaxis = dict(
        rangeslider = dict(
            visible = False
        )
    )
)

fig = go.Figure(data=data,layout=layout)
iplot(fig)