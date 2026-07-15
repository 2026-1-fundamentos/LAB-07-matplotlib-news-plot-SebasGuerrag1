"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    import pandas as pd
    import matplotlib.pyplot as plt
    import os

    df = pd.read_csv("files/input/news.csv", index_col=0)
    os.makedirs("files/plots", exist_ok=True)

    plt.figure(figsize=(10, 6))
    colors={
        "Television": "dimgray",
        "Newspaper": "grey",
        "Radio": "lightgrey",
        "Internet": "tab:blue"
    }
    zorder={
        "Television": 1,
        "Newspaper": 2,
        "Radio": 1,
        "Internet": 1
    }
    linewidth={
        "Television": 3,
        "Newspaper": 3,
        "Radio": 2,
        "Internet": 4
    }
    for column in df.columns:
        plt.plot(df.index, 
                 df[column], 
                 label=column, 
                 color=colors[column],
                 zorder=zorder[column],
                 linewidth=linewidth[column]
                 )
    plt.title("How people get their news")
    #plt.text("An increasing proportion cite Television as their main news source", fontsize=11, transform=plt.gca().transAxes)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    for column in df.columns:
        first_year=df.index[0]
        plt.scatter(
             x=first_year,
             y=df[column][first_year],
             color=colors[column],
            zorder=zorder[column],
        )
        plt.text(
            first_year-1.7,
            y=df[column][first_year],
            s=column+" "+str(df[column][first_year])+"%",
            ha="left",
            va="center",
            color=colors[column],
            fontsize=12,
        )
        last_year=df.index[-1]
        plt.scatter(
             x=last_year,
             y=df[column][last_year],
             color=colors[column]
        )
        plt.text(
            last_year+0.3,
            y=df[column][last_year],
            s=column+" "+str(df[column][last_year])+"%",
            ha="left",
            va="center",
            color=colors[column],
            fontsize=12,
        )
    plt.xticks(
        ticks=df.index, 
        labels=df.index,
        ha="center",
        )
    plt.tight_layout()
                 
    plt.savefig("files/plots/news.png")
pregunta_01()
