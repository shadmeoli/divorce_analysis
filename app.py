import os, sys
import time
import json
from datetime import datetime


import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px




# the main entry class
class Dash:

    # constructor
    def __init__(self):
        
        # reading the file 
        self.file = pd.read_csv('Marriage_Divorce_DB.csv')
        # dataframe 
        self.df = pd.DataFrame(self.file)

        # page configuration
        st.set_page_config("Cheating_rate", layout="wide")

    # render lottie animation
    def anim(self, filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)
    
    # viewing the distribution of the whole dataset
    def total_simple_distribution(self):
        
        with st.container():
            
            st.subheader("Distribution")
           
            st.metric(
                label='Number of divorce world wide',
                value=len(self.df),
                delta='+',
                help="Total number of divorce!"
            )
            st.bar_chart(self.df.describe(), height=500, width=100)
    
    
    # viewing each column
    def distinct_check(self):
            
        with st.expander("All Causes of divorce"):
            filters = self.df.columns.to_list()
            cause_selection = st.multiselect("Select the brand", options=filters, default=filters[0])
        
        try:
            print(cause_selection)
            distribution, correlation, neighbours = st.columns(3)
            
            with distribution:
                st.write("Distribution")
                st.bar_chart(self.df[cause_selection].describe())
            
            with correlation:
                st.write("Correlation")
                st.bar_chart(self.df[cause_selection].corr())
            
            with neighbours:
                sns.set_style("darkgrid")
                fig = plt.figure(figsize=(5, 4))
                sns.scatterplot(data=self.df[cause_selection])
                st.pyplot(fig)
        
        
        except Exception as e:
            print(e)
            st.warning("Choose a cause to view distribution")
    
    
    def main(self):
        st.title("Devorce")
        
        # hero section
        with st.container():
            st.write("""
                    Is divorce or breake ups in a realationship healthy?
                It is wise sometimes to leave but if it can be fixed and 
                there is love between the partners, why not try and make 
                things work?  
                    """)
        
        # summary /intro section
        self.total_simple_distribution()

        
        st.write("""
            Let us break down each each couse of divorce 
            and pick our cherries from there
                 """)
        
        # in deapth cause analysis
        self.distinct_check()
        
        
        
        
            
        
        
            
        
        


# runner 
if __name__ == '__main__':
    dash = Dash()
    dash.main()