import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


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


def get_mix_chart(df, x_axis_col, line_col, line_axis_label, bar_col, bar_axis_label, title):
    x_data = list(df[x_axis_col].values)
    line_data = list(df[line_col].values)
    bar_data = list(df[bar_col].values)

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(
            x=x_data,
            y=bar_data,
            name=bar_axis_label
        ),
        secondary_y=False
    )

    fig.add_trace(
        go.Scatter(
            x=x_data,
            y=line_data,
            name=line_axis_label
        ),
        secondary_y=True
    )
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


def scatter_plot(df, x_col, y_col):
    # x = df[x_col]
    # y = df[y_col]
    # fig = px.scatter(x=x, y=y)

    fig = px.scatter(df, x=x_col, y=y_col, color="CountryName")
    return fig
