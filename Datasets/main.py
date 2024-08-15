# Modules
import pandas as pd
import matplotlib.pyplot as plt

# -- Dataframe Setup --

# Setting up the original dataframe 
original = pd.read_csv('Datasets/data/cardata.csv')

# Setting up the new dataframe and its organised version
new = pd.read_csv('Datasets/data/cardata.csv',
                  header=0,
                  names = ['Car Name', 'Year', 'Selling Price', 'Present Price', 'Kilometres Driven', 'Fuel Type', 'Seller Type'])
print(new)

# -- Functions --

# Showing the original dataframe
def ShowOriginal():
    print(original)

# Showing the updated dataframe
def ShowNew():
    print(new)
    
