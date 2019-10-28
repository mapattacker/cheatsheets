import plotly_express as px

# Quick Start
# https://plot.ly/python/plotly-express/
# API documentation
# https://www.plotly.express/plotly_express/

px.bar(df, x='index', y='percentage', height=400)
px.line(train, x='timestamp',y='meter')
px.scatter()