# ################################################################################
#
# ███████  ██████ ███████     ██████  ███████  ██  ██████  
# ██      ██      ██               ██      ██ ███ ██  ████ 
# █████   ██      █████        █████      ██   ██ ██ ██ ██ 
# ██      ██      ██               ██    ██    ██ ████  ██ 
# ███████  ██████ ███████     ██████     ██    ██  ██████  
# 
# Project Created by: Morgan Molyneaux, Kamila Turapova, Sioeli Olive
# 
# Purpose:
# [FILL OUT LATER]
# 
#
# Features:
# - [FILL OUT LATER]
# 
# 
#
################################################################################
import pandas as pd
import numpy as np;
import statsmodels.formula.api as smf
import statsmodels.api as sm

def table(file_path):
    ''' Loads data from .csv file into a panda table'''
    # Load the .csv file into a panda table
    
    data = pd.read_csv(file_path)
    print(data)
    # print(data.head) # prints the first 5 rows of the table

    # Calculate mean Force for each combination of Line and Shift
    means = data.groupby(['Line', 'Shift'])['Force'].mean().reset_index()

    # Print the means
    print("\nMean Force for each combination of Line and Shift:")
    print(means)
    print("\nThe mean force does not vastly differ for each combination of Line and Shift."
          "\nThis shows that Line and Shift do not make a significant difference on Force.")


def linear_regression(data):
    ''' Performs linear regression analysis to determine the significant predictors of Force.
    Args:
    data (DataFrame): The DataFrame containing the data.
    
    Returns:
    None
    '''
    print("\n \n-------------------------------------------------------------------------------------")
    print("                                 Linear Regression Analysis")
    # Define the predictors and response variable
    X = data[['Amp', 'Freq', 'Temp', 'Time']]
    y = data['Force']

    # Add intercept term
    X = sm.add_constant(X)

    # Fit the linear regression model
    model = sm.OLS(y, X).fit()

    # Print summary statistics
    print("\nLinear Regression Summary:")
    print(model.summary())
    # toDo add print summary analysis here <-------
    print("-------------------------------------------------------------------------------------\n \n")


def parsimonious_model(file_path):
    ''' Using a parsimonious model to predict the force'''
    
    # Create a panda table from the .csv file that will be used to create the model
    data = pd.read_csv(file_path)
    data['Line'] = data['Line'].astype('category')
    data['Shift'] = data['Shift'].astype('category')
    data['Horn'] = data['Horn'].astype('category')

    # Leverege the statsmodels library to create the model, and print the summary
    formula = 'Force ~ Amp + Freq + Temp + Time + C(Line) + C(Shift) + C(Horn)'
    print("Full model:\n", smf.ols(formula, data=data).fit().summary())

# todO: add a function that will create a parsimonious model that will predict the force by finding significant variables (prdictors) stepwise regression
    
# Use backwards elimination to find the most significant predictors, and only include those in the model
# Find p values (anything higher than 0.05 is not significant and will be removed)
# Repeat until all predictors are significant


def backward_elimination(file_path):
    ''' Performs backward elimination to determine the significant predictors of Force and remove insignificant predictors '''
    significance_level=0.05
    data = pd.read_csv(file_path)
    
    # Convert categorical variables to dummy variables
    data = pd.get_dummies(data, columns=['Line', 'Shift', 'Horn'], drop_first=True)
    
    # Response variable & Predictor variables (excluding the response variable)
    y = data['Force']
    X = data.drop('Force', axis=1).select_dtypes(include=[np.number])  # No strings allowed or ELSE IT WILL BREAK THE PGORAM (or the panda libary more specifically)
    
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()

    # Search for the most insignificant predictor and remove it, and repeat until all predictors are significant and fit the model
    while len(X.columns) > 1:
        p_values = model.pvalues
        max_p = p_values.max()
        print("Max p-value: ", max_p)
        if max_p > significance_level:
            pushing_p = p_values.idxmax() # Get the feature with the highest p-value (most insignificant as (feature >! significant)
            X = X.drop(columns=[pushing_p])
            model = sm.OLS(y, X).fit()
        else:
            print("STUPID PROGRAM BREAKING HERE.... jk")
            break

    
    print("\nLinear Regression Summary (Backward Elimination):")
    print(model.summary())
    print("\nThe best parsimonous model to predict force is with the predictors: ", X.columns[1:], "as they are all significant predictors "
          "\nof Force (p-value < 0.05) through process of backward elimination.  In doing so, the model has been simplified and retained only the most significant predictors. \n")
    
    print("\nThe strength of the model can be seen from the R-squared value of 0.762, which indicates that the model explains 76.2% of the variance in the data."
          "\nThe adjusted R-squared value of 0.758 is also high, which indicates that the model is not overfitting the data."
          "\nAs so, the model precits [enter variance in force]")
    print("-------------------------------------------------------------------------------------\n\n")
 
if __name__ == "__main__":
    # table('ultrasoundData.csv')
    # linear_regression(pd.read_csv('ultrasoundData.csv'))
    # parsimonious_model('ultrasoundData.csv')
    backward_elimination('ultrasoundData.csv')