import pickle as pkl
import pandas as pd
import numpy as np
#from sklearn.linear_model import LogisticRegression 


import pickle as pkl
# open model in read binary mode
# load = open('G__logistic_model.pkl','rb')
# model = pkl.load(load)
with open('G__logistic_model.pkl', 'rb') as file:
    model = pkl.load(file)

# DEFINE A PREDICTION FUNCTION :
def predict(Pclass,Age,SibSp,Parch,Fare,Embarked_encoded,sex_encoded):
    prediction = model.predict([[Pclass,Age,SibSp,Parch,Fare,Embarked_encoded,sex_encoded]])
    return prediction



import streamlit as st
# DEFINE MAIN FUNCTION :
def main():
    st.set_page_config(page_title="Titanic's Legacy: Survived or Lost ?", layout="wide") 
    st.title(":ship: Titanic's Legacy: Survived or Lost? :ship:")  
    # Collect user input through Streamlit
    feature1 = st.number_input('Pclass: ')
    feature2 = st.number_input('Age: ')
    feature3 = st.number_input('SibSp: ')
    feature4 = st.number_input('Parch: ')
    feature5 = st.number_input('Fare: ')
    feature6 = st.number_input('Embarked_encoded: ')
    feature7 = st.number_input('sex_encoded: ')
   
    # WHEN THE PREDICTION BUTTON IS CLICKED
    if st.button('Predict'):
       result = predict(feature1,feature2,feature3,feature4,feature5,feature6,feature7)
       if result == 0:
             st.success("SORRY ! THE PERSON IS NOT ALIVE NOW START CRYING :scream:")
       else:
             st.success("THE PERSON IS ALIVE DON'T CRY..:blush:") 
              
# When we create LOGIS_DEP.py file in the backend python will give default global name to this python script file as "__name__"
# 
if __name__ == '__main__': # it will always be true so calls the main() function              
   main()
