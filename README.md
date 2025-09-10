# Programming-Assignment-3

PROBLEM 1

  For Problem 1, I began by importing the necessary library and loading the CSV file into a DataFrame named cars. I then displayed the first five rows to quickly check the top portion of the dataset. Finally, I showed the last five rows to verify the bottom part of the data and ensure it was loaded correctly.

- Before starting, i imported PANDA library into the code using:
                  import pandas as pd

- I loaded the csv as cars using:
                  cars = pd.read_csv("cars.csv")

- I printed the first five output using head:
                  print("First five rows of cars dataset:")
                  print(cars.head())

- then I printed the last five output using tail:
                  print("Last five rows of cars dataset:")
                  print(cars.tail())

- Saved the file as Hernandez_Pandas-P1.py in another cell

PROBLEM 2

  For Problem 2, I used the same cars DataFrame. I first showed the first five rows but only kept the odd-numbered columns. After that, I searched for the row with the model Mazda RX4 and checked how many cylinders the Camaro Z28 had. Lastly, I looked at the cylinders and gear types for Mazda RX4 Wag, Ford Pantera L, and Honda Civic.

- Similar to the first problem, i imported PANDA library as well.
                  import pandas as pd

- I loaded the csv as cars using:
                  cars = pd.read_csv("Cars.csv")

- I displayed the first five rows with odd-numbered columns using:
                  print("a. First five rows with odd-numbered columns:")
                  print(cars.iloc[:5, ::2])

- I displayed the row that contains the Model of Mazda RX4 using:
                  print("\nb. Row with Model = 'Mazda RX4':")
                  print(cars.loc[cars['Model'] == 'Mazda RX4'])

- I displayed how many cylinders the car model Camaro Z28 has using:
                  print("\nc. Cylinders of 'Camaro Z28':")
                  print(cars.loc[cars['Model'] == 'Camaro Z28', ['cyl']])

- I displayed how many cylinders and what gear type the car models Mazda RX4 Wag, Ford Pantera L, and Honda Civic have using:
                  print("\nd. Cylinders and Gear type of selected models:")
                  selected_models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
                  print(cars.loc[cars['Model'].isin(selected_models), ['Model', 'cyl', 'gear']])

- I saved the file as Hernandez_Pandas-P2.py
