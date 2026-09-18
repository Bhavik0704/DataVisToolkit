import matplotlib.pyplot as plt
import pandas as pd

def bar_chart(df: pd.DataFrame, x: str, y: str, output: str):
    plt.figure(figsize=(10, 6))
    plt.bar(df[x], df[y], color="steelblue")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(y + " by " + x)
    plt.tight_layout()
    plt.savefig(output)
    plt.close()

def scatter_plot(df: pd.DataFrame, x: str, y: str, output: str):
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x], df[y], color="darkred")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(y + " vs " + x)
    plt.tight_layout()
    plt.savefig(output)
    plt.close()

def grouped_bar(df: pd.DataFrame, x: str, y_cols: list, output: str):
    plt.figure(figsize=(10, 6))
    width = 0.2
    positions = range(len(df[x]))

    for i, col in enumerate(y_cols):
        plt.bar([p + i * width for p in positions], df[col], width=width, label=col)

    plt.xticks([p + width for p in positions], df[x])
    plt.xlabel(x)
    plt.ylabel("Values")
    plt.title("Grouped Bar Chart")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output)
    plt.close()
