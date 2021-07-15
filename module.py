import pandas as pd
import plotly.express as px


def str2matrix(string_text):
    d_list = string_text.split(",")
    matrix = []
    for i, d in enumerate(d_list):
        if i % 2 == 0:
            matrix.append([float(d_list[i]), float(d_list[i+1])])
    print(matrix)
    df = pd.DataFrame(matrix, columns=["latDeg", "lngDeg"])
    return df


def visualize_location(df, zoom=12):
    fig = px.scatter_mapbox(df,
                            lat="latDeg",
                            lon="lngDeg",
                            zoom=zoom,
                            height=400,
                            width=600)
    fig.update_layout(mapbox_style='stamen-terrain')
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.update_layout(title_text="GPS trafic")
    return "<h2>GPS_MAP</h2>" + fig.to_html(include_plotlyjs='cdn', full_html=False) + "<a href='/'>Back to top</a>"
