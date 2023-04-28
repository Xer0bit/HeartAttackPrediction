import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Importing the dataset
dataset = pd.read_csv('data.csv')
print(dataset.head())

# create a label with name 'BP'  with 109+(0.5*age)+(0.1*weight)+(0.6*sex)+((1.4*HR)/100) 

