
import pandas as pd
import matplotlib.pyplot as plt
import io, base64

def plot_chart(df: pd.DataRame, chart_type="bar"):
    """
    Generate a chart from a pandas DataFrame and return it as a base64-encoded string.
    
    args:
        df (pd.DataFrame): The DataFrame containing the data to plot.
        chart_type (str): The type of chart to generate ("bar", "line", "scatter").
    
    returns:
        str: A base64-encoded string of the generated chart image.
    """
    fig, ax = plt.subplots()
    
    if chart_type == "bar":
        df.plot(kind="bar", ax=ax)
    elif chart_type == "line":
        df.plot(kind="line", ax=ax)
    elif chart_type == "pie":
        if df.shape[1] >= 2:
            df.set_index(df.columns[0].iloc[:,0].plot(kind="pie", ax=ax))
    
    else:
        return None

    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    
    return plot_url