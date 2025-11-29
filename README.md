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
### Data Collection

Collected IPL ball-by-ball and match-level data from Kaggle & public IPL datasets.
Cleaned raw data and stored it in CSV format for analysis and model training.

### Data Cleaning
Removed duplicates and irrelevant columns
Handled missing values
Fixed inconsistent team and venue names
Converted categorical values into numerical format using label encoding & one-hot encoding
### Feature Engineering
Created meaningful features to improve prediction accuracy:
Run Rate (RR)
Required Run Rate (RRR)
Balls Left
Wickets in Hand
Home/Away team indicators
Toss Impact Feature
### Model Training
Split data into training and testing sets
Trained Logistic Regression model
Evaluated performance using:
Accuracy Score
Precision & Recall
Confusion Matrix
ROC-AUC Curve

### Deployment
Streamlit App
Built an interactive UI where users can enter match conditions
Model outputs:
Predicted Winner
Win Probability (0–100%)
Confidence Score
Flask Frontend
Designed a custom web UI using HTML/CSS/JS
Integrated Flask backend to serve predictions
Exposed /predict endpoint for ML inference

## Flask Frontend Preview

