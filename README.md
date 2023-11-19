# Unemployment Analysis With Python  

## Project Overview

This project aims to analyze and visualize unemployment-related data, focusing on Estimated Unemployment Rate, Estimated Employed, and Estimated Labour Participation Rate. The analysis is performed at both regional and state levels, providing insights into minimum, average, and maximum values for each parameter.

## Data Analysis

The script reads the initial dataset, displays basic information, handles missing values, and calculates statistical measures. It then processes the data to create a new dataset with unique entries for each state, including minimum, average, and maximum values for Estimated Unemployment Rate, Estimated Employed, and Estimated Labour Participation Rate.

## Data Visualization

The script generates various bar charts to visualize the Minimum, Average, and Maximum Estimated Unemployment Rate, Estimated Employed, and Estimated Labour Participation Rate. Additionally, a geographical map is created using Folium, displaying state-specific information upon clicking markers.

## Script Details

The `unemployment_analysis.py` script performs the following tasks:

1. **Reads the raw dataset and displays basic information:**
   - Utilizes Pandas to read the raw dataset.
   - Displays essential information about the dataset.

2. **Calculates descriptive statistics, identifies null values, and displays data types:**
   - Uses Pandas to calculate descriptive statistics.
   - Identifies and presents null values within the dataset.
   - Displays the data types of each column.

3. **Transforms the dataset by adding new columns:**
   - Adds new columns for minimum, average, and maximum values for unemployment rate, employed individuals, and labor participation rate for each state.

4. **Creates a new dataset without duplicate rows:**
   - Utilizes Pandas to remove duplicate rows based on state information.
   - Generates a new dataset without duplicate entries.

5. **Drops unnecessary columns and saves the updated dataset:**
   - Removes unnecessary columns from the dataset.
   - Saves the updated dataset, excluding unnecessary columns, to "updated_data.csv."

6. **Displays figures and saves them as PNG files:**
   - Uses Matplotlib to generate figures.
   - Shows and saves figures for minimum, average, and maximum estimated unemployment rates, employed individuals, and labor participation rates, both by region and by state.

7. **Creates an interactive map using Folium:**
   - Utilizes Folium to create an interactive map.
   - Displays state-specific information on click.
   - Saves the interactive map as an HTML file ("state_map.html").

## Video Representation

Check out the video representation of the project for a more interactive and engaging overview: [Unemployment Analysis Video](link_to_your_video)


## Requirements
This project requires the following Python libraries:
    
Pandas

Matplotlib

folium (for data visualization with map)
    
You can install these dependencies using pip:

    pip install pandas matplotlib folium

or 
    
    pip install -r requirements.txt

## Usage

To use this project, follow these steps:

1. Ensure you have Python installed on your machine.
2. Clone the project repository to your local machine:

     ```bash
     git clone https://github.com/mominurr/oibsip_task2.git
     cd oibsip_task2
     python unemployment_analysis.py
    

## Conclusion

This project provides valuable insights into unemployment trends, allowing for a comprehensive understanding of the Estimated Unemployment Rate, Estimated Employed, and Estimated Labour Participation Rate across different regions and states. The generated visualizations enhance the interpretability of the data, aiding in informed decision-making.

##Author:
[Mominur Rahman](https://github.com/mominurr)