COVID-19 Data Analysis Project
This repository contains a data analysis project focused on exploring the relationship between a country's happiness score and its COVID-19 outcomes. The analysis uses real-world datasets and is conducted using Python in a Jupyter Notebook environment.

Project Objective
The main goal of this project is to analyze and visualize two distinct datasets—one on COVID-19 cases and deaths, and another on worldwide happiness metrics. By merging and analyzing these datasets, the project seeks to uncover potential correlations and answer the question: "Did happier countries experience better COVID-19 outcomes?"

Methodology
The project follows a structured data analysis workflow:


Data Loading and Preprocessing:
The raw COVID-19 confirmed cases and deaths datasets were loaded.
The data was cleaned by dropping irrelevant geographical columns (Lat, Long, Province/State).
Daily time-series data was aggregated to get a single, total count of confirmed cases and deaths for each country.


Dataset Merging:
The processed COVID-19 data was merged with the Worldwide Happiness Report using a common key (Country). This created a single, comprehensive dataset for combined analysis.


Exploratory Data Analysis (EDA) & Visualization:
A correlation matrix heatmap was generated to visualize the relationships between happiness indicators (GDP, social support) and COVID-19 outcomes (cases, deaths).
Scatter plots were created to specifically show the correlation between a country's Happiness Score (Ladder) and its total confirmed cases and deaths.


Key Findings
The analysis revealed several important insights:
The correlation matrix showed a positive but weak correlation between happiness metrics (like GDP and Happiness Score) and both confirmed cases and deaths.
The visualizations did not support the initial hypothesis that "happier countries had better outcomes." Instead, countries with higher happiness scores and GDP often had more reported cases and deaths.
This unexpected positive correlation is likely due to confounding variables, such as better testing and reporting infrastructure in developed nations and higher rates of international travel, which may have led to a faster spread of the virus and more accurate data collection.
In conclusion, the data suggests that the relationship between a country's happiness and its pandemic experience is complex and not a simple inverse correlation.


How to Run the Project
To run this project, you will need a Python environment with the following libraries installed:
pandas
numpy
matplotlib
seaborn
Clone this repository.
Ensure the .csv dataset files are in the same directory as the Jupyter Notebook (covid19_data_analysis.ipynb).
Open the notebook in Jupyter Notebook or JupyterLab and run the cells in order.
