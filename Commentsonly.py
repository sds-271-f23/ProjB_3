#!/usr/bin/env python
# coding: utf-8

# # Lab 7 - Collaboration Lab

# This lab is going to be quite different from the previous ones. 
# 
# You will work in teams of two to create a python mini-package. Details on what that package must accomplish and how it must be organized will be included. Consider these a set of requirements given to you by a client that you must satisfy.
# 
# This package will have a few parts to it, and you must divide up the work so that both members of the team contribute functions to the package. You must document the package in detail with both comments and a README that describes how to use it.
# 
# Once you are finished with this package, you will turn in the following things in the following way:
# 
# 1. You will turn in on GitHub a shared Jupyter notebook (.ipynb) and Python file (.py). The Python file will contain your package (with code and comments) and the Jupyter notebook will import your package and document how it works.
# 
# 2. You will also turn in via GitHub a version of the package (just the .py file) where you have deleted *all the code you wrote* leaving only the comments. **You may leave function definitions, but none of the code below them.**

# 

# You will be working collaboratively on this project, so you should use version control.
# 
# <div class="alert alert-info"> Exercise 1:
# 
# If you have not yet created a [GitHub account](https://github.com/), do so now. 
# 
# Once every member of your team has a GitHub account, one member of the team should create a *private* repo for the project. Come up with a team name and name the repo "SDS271-F23-[your-team-name]"
#     
# Next, [add every member of the team to the repo](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository).
#     
# Add Casey to your repo -- this is how you will turn in this assignment. Casey's GitHub username is @caseyberger
# 
# Now, you're ready for the project.
# </div>

# ## Project A

# ### Fit a curve and plot
# 
# Now write a class that determines the relationship between altitude and temperature. It should:
# 
# 1. automatically read in the csv when initializing
# 2. clean the data appropriately and return a new dataframe *Careful: be aware of units! You may need to create some new columns in your dataframe! Kelvin = Celsius + 273.15*
# 3. fit the data to the line $T = - r h + T_0$ where $h$ is Altitude in km and $T$ is temperature in Kelvin
#   
#   Special hint for this part **when you define your fit function inside the class, put ```@staticmethod``` above the function definition** -- this allows ```curve_fit``` to use the fit function without errors. You can read more about static methods [here](https://www.digitalocean.com/community/tutorials/python-static-method) and I'm happy to explain where those errors come from another time!
#  
# 4. calculate (and return) the unknown parameter $r$ with error
# 4. calculate (and return) the unknown parameter $T_0$ with error
# 6. plot the data and the fit together on the same graph and label it appropriately

# In[6]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# In[17]:


df = pd.read_csv('atm_data.csv')
df.columns


# In[41]:


class Alt_Temp_Relationship:

    def __init__(self): # Initialize the class
        self.atm_data = pd.read_csv('atm_data.csv')
        self.update_df = self.atm_data

    # Static method defining the fit function
    @staticmethod
    def fit_function(h, r, T0):
        return -r*h + T0 

    def clean_data(self): #Cleans the data
        # Drops any NaN values
        self.update_df = self.atm_data.dropna()
        
        # Convert Celsius to Farenheit
        self.update_df.loc[:,"Temperature (K)"] = self.update_df.loc[:,"Temperature (C)"] + 273.15 
        
        #return f'Are there any n/a values in this dataframe (T/F): {self.update_df.isnull().values.any()}'

    def get_parameters(self, altitude, temp):   # Returns a dictionary of fitted parameters and their errors
        param_dict = {}
        params, cov = curve_fit(Alt_Temp_Relationship.fit_function, altitude, temp)
#         perr = np.sqrt(np.diag(cov))
        
        param_dict['r'] = params[0]
        param_dict['r_error'] = np.sqrt(cov[0][0])
        param_dict['T0'] = params[1]
        param_dict['T0_error'] = np.sqrt(cov[1][1])
        
        return param_dict

    def plot_data(self):
        # Plots the original data and the fitted curve
        print(self.update_df)
        x = self.update_df['Altitude (km)']
        y = self.update_df['Temperature (K)']
        param_dict = self.get_parameters(x, y)
        Temp = -x * param_dict['r'] + param_dict['T0']
        
        print('T0 is ' + str(param_dict['T0']) + ' with an error of ' + str(param_dict['T0_error']))
        print('r is ' + str(param_dict['r']) + ' with an error of ' + str(param_dict['r_error']))
        
        plt.scatter(x, y, color = "teal", marker = "*", s = 10, label="Data")
        plt.plot(x, Temp, color = "darkblue", label = "Fit, y(x) = -6.49282709 + 288.15763374 km")
        plt.xlabel("Altitude (km)", fontsize= 12)
        plt.ylabel('Temperature (K)', fontsize= 12)
        plt.show()


# In[42]:


checking = Alt_Temp_Relationship()
checking.clean_data()
checking.plot_data()


# # Post-Lab: Production and Reflection

# **Note: the instructions for this lab are different, so read carefully**
# 
# When you are done with this lab, make sure your team has in its GitHub one JupyterNotebook, a README, and at least one.py file that contains the class you've written. The Jupyter Notebook should import your .py file(s) and walk through how you solved the problem given to you. The README should provide a brief overview of what is in the .py file(s) and how to use it(them). It should also include the problem prompt! Finally, the .py file(s) should be adequately commented.
# 
# During class today, Casey will have added you to the SDS-271-F23 organization on GitHub and will have assigned your team a secret number and created a public repo for you in the organization. 
# 
# In this public repo, upload your README only. Then, make a copy of your .py files and **delete all the code, leaving only the comments. You may leave function definitions, but none of the code below them.** Upload this comments-only version of your .py file(s) to the public repo and add Casey to it.
# 
# In addition, don't forget to fill out the <a href="https://forms.gle/nAJeHRedav8kPyCi8"> post-lab reflection form</a>. 

# In[ ]:




