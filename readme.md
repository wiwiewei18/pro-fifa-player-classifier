# FIFA21 Pro Player Classifier

## Project Overview

This project aims to develop a classification model to predict whether a player is a "valuable player" based on various features from the FIFA21 official dataset. A "valuable player" is defined as a player with an overall rating of 75 or higher. The project leverages machine learning techniques, particularly logistic regression, to make these predictions.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Modeling Process](#modeling-process)
- [Results](#results)
- [Future Work](#future-work)

## Dataset

The dataset used for this project is the FIFA21 official dataset, which includes various attributes for soccer players, such as:

- **Player Information**: Name, Age, Nationality, Club, etc.
- **Player Attributes**: Potential, Value (€), Wage (€), Skills, Physical Attributes, etc.
- **Positioning Data**: Preferred Position, Best Position, Work Rates, etc.

Key features used in this project include both raw attributes and engineered features, such as:

- **Value (€)**
- **Potential Value**
- **Wage (€)**
- **Best Overall Rating**
- **Release Clause (€)**
- **Reactions**
- **International Reputation**
- **Potential**
- **Potential Normalized**

The target variable (`Good Player`) is a binary label where `1` indicates a valuable player (overall rating >= 75) and `0` indicates otherwise.

## Project Structure

- `dataset/`: Contains the FIFA21 dataset.
- `notebooks/`: Jupyter notebooks for data preprocessing, feature engineering, and model training.
- `utils/`: Reuseable function to help the development process.
- `README.md`: Project overview.

## Modeling Process

1. **Data Preprocessing**: Cleaning and preparing the dataset for modeling. This includes handling missing values, encoding categorical variables, and scaling numerical features.
2. **Feature Engineering**: Creating new features that may improve model performance, such as skill scores, physical scores, and defensive scores.
3. **Model Training**: The model is trained on the preprocessed data using logistic regression.
4. **Model Selection**: Logistic regression was chosen as the model for its simplicity and interpretability.
5. **Evaluation**: The model's performance is evaluated using metrics such as accuracy, precision, recall, and F1-score.

## Results

The logistic regression model achieved the following performance metrics:

- **Accuracy**: 0.97
- **Precision**: 0.93
- **Recall**: 0.90
- **F1-Score**: 0.91

These results suggest that the model is reasonably effective at predicting whether a player is valuable.

## Future Work

- **Model Improvement**: Experiment with other classification algorithms such as Random Forest, SVM, or Gradient Boosting.
- **Hyperparameter Tuning**: Perform grid search or random search to find the optimal hyperparameters for the model.
- **Feature Selection**: Explore different feature selection techniques to improve model performance.
- **Deployment**: Deploy the model using a web framework (e.g., Flask) to create a simple web app for user interaction.
