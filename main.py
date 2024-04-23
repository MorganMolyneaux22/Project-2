# ################################################################################
#
# ███████  ██████ ███████     ██████  ███████  ██  ██████  
# ██      ██      ██               ██      ██ ███ ██  ████ 
# █████   ██      █████        █████      ██   ██ ██ ██ ██ 
# ██      ██      ██               ██    ██    ██ ████  ██ 
# ███████  ██████ ███████     ██████     ██    ██  ██████  
# 
# Project Created by: Morgan Molyneaux, Kamilla Turapova, Sioelli Olive
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
    print(data.head())




if __name__ == "__main__":
    table('ultrasoundData.csv')
