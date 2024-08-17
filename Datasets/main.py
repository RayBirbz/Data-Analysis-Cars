# Modules
import pandas as pd
import matplotlib.pyplot as plt
import time
import sys


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
def avg_new():
    average_new = new['Selling_Price'].mean()
    print(f'The average selling price is '[average_new])
# AVerage currrent price
def avg_new_present():
    average_new_present = new['Present_Price'].mean()
    print(f'The average present price is '[average_new_present])

# -- Functions --

# Showing the original dataframe
def ShowOriginal():
    print(original)

# Showing the updated dataframe
def ShowNew():
    print(new)


# The user interface 

def UI():
    try:
        main_options = True

        while True: # The variables and IF statements that keep track of which options to show
            if main_options:
                Options()
            else:
                more_options()
            if main_options: # The main opptions
                try:
                    option = int(input('Enter your selection: '))
                    if option == 1:
                        ShowOriginal()
                    elif option == 2:
                        ShowNew()
                    elif option == 3:
                        main_options = False
                    elif option == 4:
                        new.info()
                    elif option == 5:
                        print('Quitting...')
                        time.sleep(500)
                        return
                    else:
                        print("Please select a valid choice.")

                except:
                    print("Please enter an option in the appropiate format.")
            else: # The analysis options 
                try:
                    option = int(input('Enter your selection: '))
                    if option == 1:
                        avg_new()
                    elif option ==  2:
                        avg_new_present()
                    elif option == 3:
                        main_options = True
                    else:
                        print('Please select a valid choice')
                except:
                        print("Please enter an option in the appropiate format.")
    except:
        print('Error')
        sys.exit()

# Main Options

def Options():
    print("""To analyse the dataset of Cars, please select one of the options below: 
          
          1 - Show the original dataset
          2 - Show the new and updated dataset
          3 - View more analysis options
          4 - View the general info of the dataset
          5 - Quit
          """)

# More options for analysis
def more_options():
    print("""To analyse additional information on the dataset of Cars, please select one of the options below: 
          
          1 - Show the average selling price
          2 - Show the average present price
          3 - Go back
          """)
# Running the UI
UI()