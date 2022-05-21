import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

def get_slider_map(df, size_column, title):
    df_dropna = df.dropna(subset=[size_column])
    fig = px.scatter_geo(df_dropna, 
            locations="CountryCode", 
            hover_name="CountryName", 
            size=size_column,
            animation_frame="Year",
            projection="natural earth"
        )
    fig.update_layout(title_text=title, title_x=0.5)
    return fig

def get_map(df, size_column):
    df_dropna = df.dropna(subset=[size_column])
    fig = px.scatter_geo(df_dropna, 
            locations="CountryCode", 
            hover_name="CountryName", 
            size=size_column,
            projection="natural earth"
        )
    fig.update_layout(title_text=title, title_x=0.5)
    return fig

def get_bar_chart(df, x_col, y_col, title):
    fig = px.bar(df, x=x_col, y=y_col)
    fig.update_layout(title_text=title, title_x=0.5)
    return fig

def get_donuts_chart(values, labels, title):
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    fig.update_layout(title_text=title, title_x=0.5)
    return fig

def line_plot_conso(df, y_col, title):
    fig = px.line(df, x="Year", y=y_col, color="CountryName")
    return fig

def line_plot_tweet(df, title):
    fig = px.line(df, x="start_date", y="counts", color="keywords",
        labels=dict(start_date="Date", counts="Tweet counts"))
    return fig