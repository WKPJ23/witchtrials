# For when you need a sample synthetic dataset with a little character.

import pandas as pd
import numpy as np
import random
import csv

n = 1500
gender = ['Male', 'Female']
countries = ["France","Germany","Belgium","Spain","England","Scotland","Ireland","Netherlands","Austria","Poland","Estonia","Norway","Sweden"]
execution_style = ["Burned at the Stake","Hanged","Drowned","Pressed","Tortured"]
confess = ['Yes','No']
married = ['Yes','No']

df = pd.DataFrame(dict(
    Gender = np.random.choice(gender, size=n, p=[0.3,0.7]),
    Country_of_Birth = np.random.choice(countries, size=n, p=[0.2,0.2,0.05,0.125,0.075,0.05,0.025,0.025,0.075,0.075,0.05,0.025,0.025]),
    Execution_Style = np.random.choice(execution_style, size=n, p=[0.35,0.3,0.15,0.1,0.1]),
    Confessed = np.random.choice(confess, size=n, p=[0.55,0.45]),
    Married = np.random.choice(married, size=n, p=[0.25,0.75]),
))

mean_age = 45  # specify the mean of the series
std_dev_age = 15  # specify the standard deviation
num_samples = n  # specify sample size n
age = np.random.normal(mean_age, std_dev_age, num_samples)
age = np.clip(age, 9, 87).astype(int)  # limits the range of integers
df.insert(0, "Age", age)

mean_year = 1550
std_dev_year = 150
num_samples = n
year_of_birth = np.random.normal(mean_year, std_dev_year, num_samples)
year_of_birth = np.clip(year_of_birth, 1300, 1800).astype(int)
df.insert(1, "Year of Birth", year_of_birth)

year_of_execution = df['Age'] + df['Year of Birth']
df.insert(2,"Year of Execution", year_of_execution)

# Normal export

df.to_csv('Witch_Trials.csv', index=False)

# Google Colab version export

from google.colab import files
df.to_csv('Witch_Trials.csv', index=False)
files.download("Witch_Trials.csv")