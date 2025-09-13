# Public Sector AI: Ready or Not?

An exploratory data analysis project examining the adoption and interest in Generative AI tools across different government sectors.

# Project Overview

This project analyzes survey data on the usage and interest in Generative AI tools across 10 different government sectors. 

The analysis includes multiple visualizations to understand patterns, trends, and sector-specific differences in AI tool adoption.

# Key Insigth 

**Sector Variations:** Economic Affairs shows the highest current adoption (44%), while Education shows the strongest future intention (59%)

**Future Intent:** Most sectors show strong intention to use AI tools in the future

**Resistance Factors:** Housing and community amenities shows the highest resistance (39%)

**Net Sentiment:** Economic affairs shows the most positive net sentiment toward AI adoption

# Requirements
------------
Install the following Python libraries (Python ≥3.8 recommended):

pip install pandas matplotlib seaborn numpy

# Usage
-----
1. Clone or download this script.
2. Run the script in your Python environment:

python genai_by_sector.py

3. The script will:
   - Print the normalized data table in the console.
   - Display a polished stacked bar chart in a pop-up window.

# Code Overview

-------------
Section          Purpose
-------          -------

Imports          Loads pandas, numpy, matplotlib, seaborn.

Data Creation    Hard-coded survey data of GenAI tool usage by sector.

Normalization    Ensures each row sums to 100%, adjusting for rounding errors.

Data Transformation Converts to long format for seaborn if needed.

Plotting         Creates a horizontal stacked bar chart with custom colors and labels.

Styling          Adds titles, legend, axis labels, and grid.

Output           Shows the chart and prints the normalized DataFrame.

# Visualization included

    Stacked Bar Chart: Complete response distribution for each sector

    Grouped Bar Chart: Comparison of response categories across sectors

    Pie Charts: Response breakdown for each individual sector

    Heatmap: Color-encoded intensity of responses across sectors

    Line Plot: Trends and patterns across ordered sectors

    Diverging Bar Chart: Net positive interest (Yes minus Not Interested)

# Stacked Bar Chart
--------------
<img width="1973" height="1418" alt="image" src="https://github.com/user-attachments/assets/389641f4-46f9-4478-8470-e0984371fb0b" />

**Purpose:** Shows the complete distribution of responses for each sector in a single view

**Insight:** Allows comparison of response patterns across sectors and within each sector

**Key observation:** Some sectors show higher adoption rates (like Economic Affairs) while others show stronger future intention (like Education)

# Grouped Bar chart
------------------
<img width="1990" height="1425" alt="image" src="https://github.com/user-attachments/assets/368a97c4-b21a-4192-9d29-2f8aa4b684aa" />

**Purpose:** Compares each response category across different sectors side-by-side

**Insight:** Makes it easy to see which sectors have the highest "Yes" responses or strongest resistance

**Key observation:** Highlights extreme values and makes direct category comparisons clearer

# Piechart by sector
---------------------
<img width="2833" height="1178" alt="image" src="https://github.com/user-attachments/assets/b6f4b0bb-bc78-4941-a9e1-0d66c75ffb9f" />

**Purpose:** Shows the proportion of responses within each individual sector

**Insight:** Reveals the internal composition of responses for each sector

**Key observation:** Some sectors are more polarized while others have more balanced responses

# Heatmap
------------------------
<img width="1608" height="1137" alt="image" src="https://github.com/user-attachments/assets/c7ef6034-fb42-40e8-b9c8-cf0766b97d82" />

**Purpose:** Uses color intensity to represent response percentages across sectors

**Insight:** Quickly identifies patterns and outliers through visual encoding

**Key observation:** Warm colors highlight sectors with higher adoption or resistance rates

# Line plot 
------------------------
<img width="1990" height="1137" alt="image" src="https://github.com/user-attachments/assets/a6df9b2f-0f79-4c16-bb06-14bf1a40766d" />

**Purpose:** Shows trends and patterns across the ordered sectors

**Insight:** Reveals if there's any progression or pattern in responses as we move through sectors

**Key observation:** Helps identify if sectors cluster in certain response patterns

# Diverging Bar 
-------------------------
<img width="2001" height="1425" alt="image" src="https://github.com/user-attachments/assets/cddec6a4-3149-4d1c-b42b-738fb9cc1099" />

**Purpose:** Highlights the net positive interest (Yes minus Not Interested)

**Insight:** Shows which sectors have the most favorable overall sentiment toward AI adoption

**Key observation:** Clearly ranks sectors from most to least receptive to AI tools

# Customization
-------------
- Color Palette: Change the colors list for different color schemes.
- Labels Visibility: Adjust the if value > 3: threshold to show/hide small segment labels.
- Data Source: Replace the hard-coded data dictionary with your own dataset.

# Conclusion
--------------
Each visualization provides a different perspective on the same data, helping to tell a comprehensive story about AI tool adoption across government sectors. 

The stacked bar gives the complete picture, while the other charts focus on specific aspects like comparisons, compositions, patterns, and net sentiment.

Last modified *September 13, 2025*
