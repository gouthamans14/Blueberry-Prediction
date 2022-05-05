# -*- coding: utf-8 -*-
"""
Created on Tue May  3 20:23:02 2022

@author: gouthaman
"""
import warnings  # helps to remove warnings 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import dabl as db
import numpy as np
import joblib 
from xgboost import XGBRFRegressor

import os
currpath =os.path.dirname(os.path.realpath(__file__))
#print("path: {}".format(currpath))

#url = "F:\\TMLC\\BlueBerry Prediction\\Dataset\WildBlueberryPollinationSimulationData.csv"
path=(currpath + "/Dataset/WildBlueberryPollinationSimulationData.csv")
df = pd.read_csv(path)

#print(df.head())

features=['seeds','fruitset','osmia','fruitmass','honeybee','andrena','RainingDays','MaxOfLowerTRange','AverageRainingDays','AverageOfUpperTRange']
xgbref =joblib.load(currpath +"\Lregressor.pkl")
#print(xgbref.get_booster().feature_names)

def predict_yield(attributes : np.ndarray ):
    pred=xgbref.predict(attributes)
    print("Yield Predict")
    return pred[0]

