import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

# Clean the data
df = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df["value"], color="red", linewidth=1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save and return the figure
    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    # Prepare data for bar plot
    df_bar = df.copy()
    df_bar["year"] = df.index.year
    df_bar["month"] = df.index.month_name()
    df_bar = df_bar.groupby(["year", "month"]).mean().unstack()

    # Draw bar plot
    fig = df_bar.plot(kind="bar", legend=True, figsize=(10, 6)).figure
    plt.title("Average Daily Page Views per Month")
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months", labels=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    plt.tight_layout()

    # Save and return the figure
    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    # Prepare data for box plots (seasonal)
    df_box = df.copy()
    df_box["year"] = df.index.year
    df_box["month"] = df.index.strftime("%b")
    months_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(20, 7))
    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0]).set(title="Year-wise Box Plot (Trend)", xlabel="Year", ylabel="Page Views")
    sns.boxplot(x="month", y="value", data=df_box, order=months_order, ax=axes[1]).set(title="Month-wise Box Plot (Seasonality)", xlabel="Month", ylabel="Page Views")

    # Save and return the figure
    fig.savefig("box_plot.png")
    return fig
