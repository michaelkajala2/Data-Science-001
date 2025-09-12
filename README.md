# Data-Science-001
This Python script normalizes survey data on Generative AI tool usage across government sectors and visualizes it as a clear, color-coded horizontal stacked bar chart. It produces publication-ready graphics with labeled percentages, making it easy to compare sectoral adoption patterns at a glance.

# Features
--------
- Data Preparation: Input data of survey responses by sector is converted to a pandas DataFrame.
- Normalization: Each sector’s responses are normalized to ensure the total equals 100% (with rounding correction).
- Long Format Conversion: Data is melted for easier plotting using Seaborn/Matplotlib.
- Stacked Horizontal Bar Plot: A custom color palette and white-grid style are used to make the chart accessible and attractive.
- Percentage Labels: Displays percentage values directly on each bar segment (hidden for very small segments).
- Publication-Ready Output: Chart includes a clear title, subtitle, labeled axes, legend, and grid.

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

# Example Output
--------------
<img width="1973" height="1418" alt="image" src="https://github.com/user-attachments/assets/389641f4-46f9-4478-8470-e0984371fb0b" />


Each bar represents one sector, and each color corresponds to a response category:
- Blue: “Yes”
- Orange: “No, but I intend to use these tools in the future”
- Red: “No, and I’m not interested in them either”

Customization
-------------
- Color Palette: Change the colors list for different color schemes.
- Labels Visibility: Adjust the if value > 3: threshold to show/hide small segment labels.
- Data Source: Replace the hard-coded data dictionary with your own dataset.

License
-------
This script is released under the MIT License.
Feel free to modify and adapt it for your own work.
