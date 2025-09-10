# coding: utf-8
import pandas as pd

#Load the cars dataset
cars = pd.read_csv("Cars.csv")

#Display the first five rows with odd-numbered columns
print("a. First five rows with odd-numbered columns:")
print(cars.iloc[:5, ::2])

#Display the row that contains the Model of Mazda RX4
print("\nb. Row with Model = 'Mazda RX4':")
print(cars.loc[cars['Model'] == 'Mazda RX4'])

#How many cylinders does the car model Camaro Z28 have?
print("\nc. Cylinders of 'Camaro Z28':")
print(cars.loc[cars['Model'] == 'Camaro Z28', ['cyl']])

#Determine how many cylinders and what gear type do the car models have
#'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic' have.
print("\nd. Cylinders and Gear type of selected models:")
selected_models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
print(cars.loc[cars['Model'].isin(selected_models), ['Model', 'cyl', 'gear']])
import pandas as pd

#Load the cars dataset
cars = pd.read_csv("Cars.csv")

#Display the first five rows with odd-numbered columns
print("a. First five rows with odd-numbered columns:")
print(cars.iloc[:5, ::2])

#Display the row that contains the Model of Mazda RX4
print("\nb. Row with Model = 'Mazda RX4':")
print(cars.loc[cars['Model'] == 'Mazda RX4'])

#How many cylinders does the car model Camaro Z28 have?
print("\nc. Cylinders of 'Camaro Z28':")
print(cars.loc[cars['Model'] == 'Camaro Z28', ['cyl']])

#Determine how many cylinders and what gear type do the car models have
#'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic' have.
print("\nd. Cylinders and Gear type of selected models:")
selected_models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
print(cars.loc[cars['Model'].isin(selected_models), ['Model', 'cyl', 'gear']])
get_ipython().run_cell_magic('writefile', 'Estrada_Pandas-P1.py', '\nimport pandas as pd\n\n#Load the cars dataset\ncars = pd.read_csv("Cars.csv")\n\n#Display the first five rows with odd-numbered columns\nprint("a. First five rows with odd-numbered columns:")\nprint(cars.iloc[:5, ::2])\n\n#Display the row that contains the Model of Mazda RX4\nprint("\\nb. Row with Model = \'Mazda RX4\':")\nprint(cars.loc[cars[\'Model\'] == \'Mazda RX4\'])\n\n#How many cylinders does the car model Camaro Z28 have?\nprint("\\nc. Cylinders of \'Camaro Z28\':")\nprint(cars.loc[cars[\'Model\'] == \'Camaro Z28\', [\'cyl\']])\n\n#Determine how many cylinders and what gear type do the car models have\n#\'Mazda RX4 Wag\', \'Ford Pantera L\', and \'Honda Civic\' have.\nprint("\\nd. Cylinders and Gear type of selected models:")\nselected_models = [\'Mazda RX4 Wag\', \'Ford Pantera L\', \'Honda Civic\']\nprint(cars.loc[cars[\'Model\'].isin(selected_models), [\'Model\', \'cyl\', \'gear\']])\n')
get_ipython().run_line_magic('save', 'Hernandez_Pandas-P1.py')
import pandas as pd

#Load the cars dataset
cars = pd.read_csv("Cars.csv")

#Display the first five rows with odd-numbered columns
print("a. First five rows with odd-numbered columns:")
print(cars.iloc[:5, ::2])

#Display the row that contains the Model of Mazda RX4
print("\nb. Row with Model = 'Mazda RX4':")
print(cars.loc[cars['Model'] == 'Mazda RX4'])

#How many cylinders does the car model Camaro Z28 have?
print("\nc. Cylinders of 'Camaro Z28':")
print(cars.loc[cars['Model'] == 'Camaro Z28', ['cyl']])

#Determine how many cylinders and what gear type do the car models have
#'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic' have.
print("\nd. Cylinders and Gear type of selected models:")
selected_models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
print(cars.loc[cars['Model'].isin(selected_models), ['Model', 'cyl', 'gear']])
get_ipython().run_line_magic('save', 'Hernandez_Pandas-P1.py')
import pandas as pd

#Load the cars dataset
cars = pd.read_csv("Cars.csv")

#Display the first five rows with odd-numbered columns
print("a. First five rows with odd-numbered columns:")
print(cars.iloc[:5, ::2])

#Display the row that contains the Model of Mazda RX4
print("\nb. Row with Model = 'Mazda RX4':")
print(cars.loc[cars['Model'] == 'Mazda RX4'])

#How many cylinders does the car model Camaro Z28 have?
print("\nc. Cylinders of 'Camaro Z28':")
print(cars.loc[cars['Model'] == 'Camaro Z28', ['cyl']])

#Determine how many cylinders and what gear type do the car models have
#'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic' have.
print("\nd. Cylinders and Gear type of selected models:")
selected_models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
print(cars.loc[cars['Model'].isin(selected_models), ['Model', 'cyl', 'gear']])
