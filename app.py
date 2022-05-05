# -*- coding: utf-8 -*-
"""
Created on Tue May  3 20:39:08 2022

@author: gouthaman
"""
import pandas as pd
import streamlit as st
from xgbmodel import predict_yield
import numpy as np
st.set_page_config(page_title="Blueberry Prediction", layout="wide")
col1, col2 = st.columns(2)


with col1:
    with st.form("Prediction_Form"):
        st.header("Enter the deciding Factors:")
        
        fruitset=st.text_input('fruitset')
        osmia=st.text_input("Osmia")
        seeds=st.text_input("seeds")
        fruitmass=st.text_input('fruitmass')
        RainingDays=st.text_input('RainingDays')
        AverageRainingDays=st.text_input('AverageRainingDays')
        honeybee = st.text_input('honeybee')
        andrena = st.text_input('andrena')
        MaxOfLowerTRange = st.text_input('MaxOfLowerTRange') 
        AverageOfUpperTRange=st.text_input('AverageOfUpperTRange') 
        
        submit_val= st.form_submit_button('Predict_yield')
   
if submit_val:
    #print(clone_size)
    
    #print(type(seeds))
    ls=np.array([float(seeds),float(fruitset),float(osmia),float(fruitmass),float(honeybee),
    float(andrena),float(RainingDays),float(MaxOfLowerTRange),float(AverageRainingDays),float(AverageOfUpperTRange)]
    ).reshape(1,-1)
    print(ls)
    value = predict_yield(attributes=ls)
    
    
    with col2:
        st.header("here are the results")
        st.success("The value is {}".format(value))