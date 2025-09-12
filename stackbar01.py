# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 20:58:36 2025

@author: ABRAHAM
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

# 3. Create the figure with seaborn
plt.figure(figsize=(14, 10))

# Create custom color palette
colors = ['#4c78a8', '#f58518', '#e45756']  # Blue, Orange, Red
custom_palette = sns.color_palette(colors)

# Create the stacked bar plot using matplotlib with seaborn styling
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

# 4. Add percentage labels to each segment
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

# 5. Polish the chart with seaborn aesthetics
# Set y-axis labels
ax.set_yticks(range(len(df_wide)))
ax.set_yticklabels(df_wide.index, fontsize=11)

# Set x-axis
ax.set_xlabel('Percentage (%)', fontsize=12, fontweight='bold')
ax.set_xlim(0, 100)
ax.set_xticks(range(0, 101, 10))

# Title and subtitle
plt.suptitle('Use of GenAI Tools for Work by Sector', fontsize=16, fontweight='bold', y=0.98)

# Legend
ax.legend(
    bbox_to_anchor=(1.05, 1), 
    loc='upper left', 
    frameon=True, 
    fancybox=True, 
    shadow=True,
    fontsize=11
)

# Grid and spines
ax.grid(True, alpha=0.3, axis='x')
sns.despine(left=True, bottom=True)

# Adjust layout
plt.tight_layout()

# 6. Show the plot
plt.show()

# Optional: Display the normalized data for verification
print("\nNormalized Percentages (sum to 100% for each sector):")
print(df_perc.astype(int))