import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
 # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    print(df.head())
    fig, ax = plt.subplots(figsize=(12,6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label = "Original Data", alpha=0.5)


    # Create scatter plot


    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"],df["CSIRO Adjusted Sea Level"])
    x_vals = pd.Series(range(df['Year'].min(), 2051))
    y_vals = slope *x_vals + intercept

    ax.plot(x_vals, y_vals, 'r', label = f'Best Fit (1880-2050): y = {slope:.4f}x + {intercept:.2f}')
    # Create second line of best fit

    df_recent = df[df['Year'] >= 2000]

    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent["Year"],df_recent["CSIRO Adjusted Sea Level"])
    x_future = pd.Series(range(2000, 2051))
    y_future = slope_recent * x_future + intercept_recent

    ax.plot(x_future,y_future,'g', label = f'Best Fit (2000-2051): y = {slope_recent:.4f}x + {intercept_recent:.2f}')

    # Add labels and title

    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()