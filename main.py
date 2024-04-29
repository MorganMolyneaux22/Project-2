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
    
    
if __name__ == "__main__":
    table('ultrasoundData.csv')
    linear_regression(pd.read_csv('ultrasoundData.csv'))
    parsimonious_model('ultrasoundData.csv')

    