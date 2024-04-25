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

if __name__ == "__main__":
    table('ultrasoundData.csv')
