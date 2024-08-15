# Modules
import pandas as pd
import matplotlib.pyplot as plt
import time


# -- Variables --

# Quit
quit = False

# -- Dataframe Setup --

# Setting up the original dataframe 
original = pd.read_csv('Datasets/data/cardata.csv')

# Setting up the new dataframe and its organised version
new = pd.read_csv('Datasets/data/cardata.csv')
new = new.drop(columns=['Owner'], axis=1)
new.head()

# -- Additional Variables --

# Average selling price

# -- Functions --

# Showing the original dataframe
def ShowOriginal():
    print(original)

# Showing the updated dataframe
def ShowNew():
    print(new)
# Showing the average 
def avg_new():
    average_new = new['Selling_Price'].mean()
    print(average_new)

# The user interface and options

def Options():
    global quit
    print("""To analyse the dataset of Cars, please select one of the options below: 
          
          1 - Show the original dataset
          2 - Show the new and updated dataset
          3 - View the average selling price for all the cars
          4 - View the average present price for all the cars
          5 - View the general info of the dataset
          6 - Quit
          """)
    try:
        option = int(input('Enter your selection: '))
        if option == 1:
            ShowOriginal()
        elif option == 2:
            ShowNew()
        elif option == 3:
            avg_new()
        elif option == 5:
            new.info()
        elif option == 6:
            quit = True
        else:
            print("Please select a valid choice.")

    except:
        print("Please enter an option in the appropiate format.")

while not quit:
    Options()