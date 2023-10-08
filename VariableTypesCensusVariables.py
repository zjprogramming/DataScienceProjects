# Import pandas with alias
import pandas as pd

# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)

print(census.head())

print(census.dtypes)
print(census['birth_year'].unique())

census['birth_year'] = census['birth_year'].replace(['missing'], 1967)

print(census['birth_year'].unique())

census['birth_year'] = census['birth_year'].astype(int)
print(census.dtypes)

print(census['birth_year'].mean())

census['higher_tax'] = pd.Categorical(census['higher_tax'], ['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree'], ordered = True)

print(census['higher_tax'].unique())

census['higher_tax'] = census['higher_tax'].cat.codes

print(census['higher_tax'].median())

census_1 = pd.get_dummies(census, columns = ['marital_status'])

print(census_1.head())

census['marital_status'] = pd.Categorical(census['marital_status'], ['single', 'divorced', 'married', 'widowed'], ordered = False)

census['marital_status'] = census['marital_status'].cat.codes

print(census.head)

bins = [0,4,9,14,19,24,29,34,39,44,49,54,59,64,69,74,79,84,89,94,99]

groups = ['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85-89', '90-94', '95-99']

import datetime

census['age'] = datetime.datetime.today().year - census['birth_year']

print(census.head())

census['age_group'] = pd.cut(census['age'], bins, labels = groups)

print(census.head())
