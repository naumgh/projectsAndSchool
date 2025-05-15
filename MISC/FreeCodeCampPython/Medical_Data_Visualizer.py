import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("medical_examination.csv")
print(df.head())

df['overweight']=(df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)
print(df.head())

def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` with specified variables
    df_cat = pd.melt(df, id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data to split it by 'cardio'
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    # Draw the catplot
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio',
                      data=df_cat, kind='bar').fig
    # Do not modify
    fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi'])&
        (df['height'] >= df['height'].quantile(0.025))&
        (df['height'] <= df['height'].quantile(0.975))&
        (df['weight'] >= df['weight'].quantile(0.025))&
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    fig, ax = plt.subplots(figsize=(12, 12))
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", ax=ax)
    fig.savefig('heatmap.png')
    return fig

