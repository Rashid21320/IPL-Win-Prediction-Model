# IPL-Win-Prediction-Model (Machine Learning + Streamlit + Flask )

## Project Objective

  The objective of this project is to build a predictive Machine Learning model that forecasts the winning team of an IPL (Indian Premier League) match based on key match-related features such as venue, toss results, batting team, bowling team, and match conditions.
The project uses Logistic Regression to estimate win probabilities and is deployed using Streamlit for interactive predictions and Flask for a custom frontend UI.
This end-to-end project helps cricket analysts, fans, and recruiters understand how ML can be used in sports analytics.

## Datasets Used
<a href = "https://www.kaggle.com/datasets/saiprudvirajy/indian-premier-league-ipl-2008-2024"> IPL-Ball By Ball-2008-2024

## Machine Learning Approach
### Model Used: Logistic Regression
Selected due to its strong interpretability and suitability for binary classification problems.
### Features Used
Batting Team
Bowling Team
Venue
Toss Winner
Toss Decision
Current Score features (if live prediction)
Run Rate, Required Run Rate, Overs left (optional)
### Target Variable
Match Winner (1 = Batting team wins, 0 = Bowling team wins)

## Process Workflow
1️### Data Collection
Collected IPL ball-by-ball and match-level data from Kaggle & public IPL datasets.
Cleaned raw data and stored it in CSV format for analysis and model training.

