
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",parse_dates=["date"],index_col='date')
#print(df.head())


#print(df.sum())
# Clean data
total_views = df['value'].sum()

df = df[
    (df['value'] < df['value'].quantile(0.975)) &
    (df['value'] > df['value'].quantile(0.025))
]

#print(df_cleansed.head())

def draw_line_plot():
    # Draw line plot
    fig = df.plot(figsize=(12,6), kind = 'line', title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019', ylabel = 'Page Views', xlabel = 'Date').get_figure()


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['year'] = df.index.year
    df['month'] = df.index.month

    # Group by year and month, and calculate the mean daily page views for each month
    monthly_avg = df.groupby(['year', 'month'])['value'].mean().unstack()

    # Plot the bar plot (each month as a separate series)
    ax = monthly_avg.plot.bar(figsize=(12, 6), title='Average Daily Page Views per Month by Year', xlabel='Years', ylabel='Average Page Views')

    # Add legend title and month names directly
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ax.legend(title='Months', labels=months)

    # Get the figure from the axes object and save the plot
    fig = ax.get_figure()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

