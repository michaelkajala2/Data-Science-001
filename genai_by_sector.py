# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 16:11:25 2025

@author: MichaelP
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set seaborn style for a polished look
sns.set_style("whitegrid")
sns.set_palette("colorblind")  # Use a colorblind-friendly palette

# 1. Create the data as a DataFrame
data = {
    'Sector': [
        'Defence', 'Economic affairs', 'Education', 'Environmental protection',
        'General public services', 'Health', 'Housing and community amenities',
        'Public order and safety', 'Recreation, culture and religion', 'Social protection'
    ],
    'Yes': [43, 44, 25, 26, 29, 19, 26, 27, 23, 37],
    'No, but I intend to use these tools in the future': [29, 37, 59, 47, 49, 48, 35, 43, 46, 37],
    'No, and I\'m not interested in them either': [29, 20, 16, 26, 21, 32, 39, 30, 31, 27]
}
df = pd.DataFrame(data)

# 2. Normalize the data to ensure each row sums to exactly 100%
df_perc = df.set_index('Sector')
df_perc = df_perc.div(df_perc.sum(axis=1), axis=0) * 100
df_perc = df_perc.round()  # Round to nearest integer

# Adjust to ensure exact sum of 100% (handle rounding errors)
for i in range(len(df_perc)):
    row_sum = df_perc.iloc[i].sum()
    if row_sum != 100:
        max_col_idx = df_perc.iloc[i].idxmax()
        df_perc.loc[df_perc.index[i], max_col_idx] += (100 - row_sum)

# Convert back to long format for seaborn
df_melted = df_perc.reset_index().melt(
    id_vars='Sector', 
    var_name='Response', 
    value_name='Percentage'
)

# Custom color palette
colors = ['#4c78a8', '#f58518', '#e45756']  # Blue, Orange, Red
custom_palette = sns.color_palette(colors)

# Function to create stacked bar chart (original visualization)
def create_stacked_bar_chart():
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Calculate cumulative percentages for stacking
    df_wide = df_perc.copy()
    cumulative = np.zeros(len(df_wide))
    
    # Plot each category separately to create the stack
    for i, col in enumerate(df_wide.columns):
        ax.barh(
            y=range(len(df_wide)), 
            width=df_wide[col].values, 
            left=cumulative, 
            color=custom_palette[i], 
            edgecolor='white', 
            linewidth=0.5,
            label=col
        )
        cumulative += df_wide[col].values
    
    # Add percentage labels to each segment
    cumulative = np.zeros(len(df_wide))
    for i, col in enumerate(df_wide.columns):
        percentages = df_wide[col].values
        for j, value in enumerate(percentages):
            if value > 3:  # Only show label if segment is large enough
                x_pos = cumulative[j] + value / 2
                ax.text(
                    x_pos, j, f'{value:.0f}%', 
                    ha='center', va='center', 
                    fontweight='bold', fontsize=10,
                    color='white' if value > 15 else 'black'
                )
        cumulative += percentages
    
    # Polish the chart
    ax.set_yticks(range(len(df_wide)))
    ax.set_yticklabels(df_wide.index, fontsize=11)
    ax.set_xlabel('Percentage (%)', fontsize=12, fontweight='bold')
    ax.set_xlim(0, 100)
    ax.set_xticks(range(0, 101, 10))
    plt.suptitle('Use of GenAI Tools for Work by Sector', fontsize=16, fontweight='bold', y=0.98)
    ax.legend(
        bbox_to_anchor=(1.05, 1), 
        loc='upper left', 
        frameon=True, 
        fancybox=True, 
        shadow=True,
        fontsize=11
    )
    ax.grid(True, alpha=0.3, axis='x')
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    plt.show()

# Function to create grouped bar chart
def create_grouped_bar_chart():
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Set up the positions for the bars
    x = np.arange(len(df_perc))
    width = 0.25
    
    # Plot each response category
    for i, col in enumerate(df_perc.columns):
        ax.bar(x + i*width, df_perc[col], width, label=col, color=custom_palette[i])
    
    # Add labels and title
    ax.set_xlabel('Sector', fontsize=12, fontweight='bold')
    ax.set_ylabel('Percentage (%)', fontsize=12, fontweight='bold')
    ax.set_title('Use of GenAI Tools for Work by Sector', fontsize=16, fontweight='bold')
    ax.set_xticks(x + width)
    ax.set_xticklabels(df_perc.index, rotation=45, ha='right')
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    plt.tight_layout()
    plt.show()

# Function to create pie charts for each sector
def create_pie_charts():
    # Create a grid of pie charts
    fig, axes = plt.subplots(2, 5, figsize=(20, 10))
    axes = axes.flatten()
    
    for i, sector in enumerate(df_perc.index):
        values = df_perc.loc[sector].values
        axes[i].pie(values, labels=df_perc.columns, autopct='%1.0f%%', 
                   colors=custom_palette, startangle=90)
        axes[i].set_title(sector, fontweight='bold')
    
    plt.suptitle('Use of GenAI Tools for Work by Sector', fontsize=16, fontweight='bold', y=0.95)
    plt.tight_layout()
    plt.show()

# Function to create heatmap
def create_heatmap():
    plt.figure(figsize=(12, 8))
    sns.heatmap(df_perc, annot=True, fmt='.0f', cmap='YlOrRd', 
                cbar_kws={'label': 'Percentage (%)'})
    plt.title('Use of GenAI Tools for Work by Sector', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()

# Function to create line plot showing trends across sectors
def create_line_plot():
    plt.figure(figsize=(14, 8))
    
    for i, col in enumerate(df_perc.columns):
        plt.plot(df_perc.index, df_perc[col], marker='o', label=col, 
                 color=custom_palette[i], linewidth=2)
    
    plt.xlabel('Sector', fontsize=12, fontweight='bold')
    plt.ylabel('Percentage (%)', fontsize=12, fontweight='bold')
    plt.title('Use of GenAI Tools for Work by Sector', fontsize=16, fontweight='bold')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

# Function to create diverging bar chart
def create_diverging_bar_chart():
    # Calculate the difference between "Yes" and "No, and I'm not interested"
    df_diverging = df_perc.copy()
    df_diverging['Net Positive'] = df_diverging['Yes'] - df_diverging['No, and I\'m not interested in them either']
    df_diverging = df_diverging.sort_values('Net Positive')
    
    plt.figure(figsize=(14, 10))
    
    # Create diverging bars
    colors = ['#e45756' if x < 0 else '#4c78a8' for x in df_diverging['Net Positive']]
    plt.barh(df_diverging.index, df_diverging['Net Positive'], color=colors)
    
    plt.axvline(x=0, color='black', linestyle='-', alpha=0.3)
    plt.xlabel('Net Positive Response (Yes - Not Interested) (%)', fontsize=12, fontweight='bold')
    plt.title('Net Positive Interest in GenAI Tools by Sector', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()

# Main execution - choose which visualization to create
if __name__ == "__main__":
    # Uncomment the visualization you want to create
    
    # 1. Original stacked bar chart
    create_stacked_bar_chart()
    
    # 2. Grouped bar chart
    create_grouped_bar_chart()
    
    # 3. Pie charts for each sector
    create_pie_charts()
    
    # 4. Heatmap
    create_heatmap()
    
    # 5. Line plot
    create_line_plot()
    
    # 6. Diverging bar chart
    create_diverging_bar_chart()

# Optional: Display the normalized data for verification
print("\nNormalized Percentages (sum to 100% for each sector):")
print(df_perc.astype(int))