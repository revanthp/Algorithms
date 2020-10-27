# Decision Tree Implementation
# input 
#   parameters:
#   - tree_depth
#   - min_sample_leaf
#   - min_sample_split
# output :
#   - tree model

# Add in unit testing methods
import numpy as np
# import pandas as pd

def entropy(p):
  return -np.sum(p * np.log2(p) + (1-p) * np.log2(1-p))

def calculate_entropy(arr, bkpt):
  pass
  
def calculate_gini(arr, bkpt):
  pass

Class DecisionTreeClassifier:
  def __init__(self, max_depth, min_sample_leaf, min_sample_split, random_state):
    pass
    
  def train(self, X, y):
    pass
    
  def predict(self, X):
    pass
 
