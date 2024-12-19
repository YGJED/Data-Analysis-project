#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd  #imports the pandas library and assigns it to pd
import matplotlib.pyplot as plt  #imports the matplotlib.pyplot visualization library and assigns it to plt
import numpy as np   #imports the NumPy numerical and array library and gives it an alias 'np'
import seaborn as sns  #imports the Seaborn data visualization library and gives it an alias 'sns'.


# In[2]:


# Read the XLSX file and make it a DataFrame
DATA = pd.read_excel('project_table.xlsx', index_col=None) 
DATA.head(11).style\
    .background_gradient(cmap='Greens', subset='AGE')\
    .background_gradient(cmap='Purples', subset='SYS_BP')\
    .background_gradient(cmap='Blues', subset='DIA_BP')\
#used to get the first 11 rows of the DATA and styles them
#applies a green background color gradient to the 'AGE'
#applies a Purple background color gradient to the 'SYS_BP'
#applies a Purple background color gradient to the 'DIA_BP'


# In[3]:


DATA.head()
DATA
 # displays the entire data in a formatted tabular view.


# In[4]:


DATA_LIST= DATA.values.tolist() #converts the 'DATA' into a list and sets DATA_LIST equal to it.
DATA_LIST #displays the entire 'DATA_LIST', in the form of a list


# In[5]:


#defines the function with the name create_generation list with the parameter age_list and sets the three variables under18 adult and senior to 0
def create_generation_list (age_list):
    under18 = 0  
    adult = 0 
    senior = 0
    #iterates through the list and compares the elements in the list to values
    for i in age_list:
        if i <= 18:#if the element in the list is less than or equal to 18 add 1 to under18
            under18+=1
        elif i <= 59:#if the element in the list is less than or equal to 59 add 1 to adult
            adult+=1
        else:
            senior+=1#if the element in the list anyting other than the 
         

        
        
        
    age_count = [under18 , adult, senior]  #stores the values of under18, adult, and senior in the age_count list
    return age_count#returns the list age_count


# In[6]:


AGE = []#sets AGE to an empty list
for row in DATA_LIST:
   AGE.append (row[1])#stores the values from the age section of our table to the list AGE
   
age_counting = create_generation_list (AGE)#the list age we created with the values added is then used as the argument and stored in the variable age_counting
print(age_counting)#the values are displayed using the print function


# In[7]:


my_gen_list = create_generation_list (AGE)
#calling a function called create_generation_list with the 'AGE' variable as an argument represented as my_gen_list
my_array= np.array(AGE)# Converting the data to an array
mylabels = ["Adult", "Under 18", "Senior"] #creates a list called 'mylabels' with 3 categories for the pie chart
myexplode = [0.15, 0.15, 0] 
#creates a list 'myexplode' and based of the parameters, it explodes/seperates the category from the pie chart

plt.pie(my_gen_list, labels = mylabels, explode = myexplode)
#plt.pie is a function used to create the pie chart. 
#It takes 'my_gen_list' as the data printed, 'mylables' as the label for each slice
#myexplode is used to explode the distance of each slice

plt.legend(loc = 'center right', bbox_to_anchor=(1,0,0.5,1))
#adds a legend to the pie chart. The loc is use to specify the position and bbox_to_anchor adjusts the position
plt.show() #used to display the pie chart


# In[8]:


def blood_presure_categorize (systolic_bp, diastolic_bp): #defines function with parameters systolic_bp and diastolic 
#sorts the systolic_bp and diastolic_bp setting bp_type to either normal, elevated, or hypertension
#by comparing them with other values    

    if systolic_bp < 120 and diastolic_bp<80:
            bp_type = 'Normal'
    elif systolic_bp >=120 and systolic_bp <= 139 and diastolic_bp>=80 and diastolic_bp<=89:
            bp_type = 'Elevated'
    elif systolic_bp >= 140 and diastolic_bp>=90:
            bp_type = 'Hypertension'
    else:
        bp_type = 'unknown'



    return bp_type #returns the the bp_type 


# In[9]:


BPS = [] #initlizes empty lists
BPD = []
BP_CAT = []

for row in DATA_LIST:
    BPS.append (row[5])#stores the 5th row of DATA_LIST in BPS
    BPD.append (row[6])#stores the 6th row of DATA_LIST in BPD



for i in range (len(BPS)): #iterates through BPS and BPD lists
    bpc = blood_presure_categorize (BPS[i], BPD[i]) #stores the retured values from the B.P.C function in the bpc variable 
    BP_CAT.append(bpc) #stores the bp_type values in the list BP_CaT
    print (i, "--", bpc) #displays the values using the print function


# In[10]:


# Your data
x=BPS
y=BPD
# Create the scatter plot using seasborns sns.scatterplot function. 
#The 'x', & 'y' variables specify the data for the x and y axis
#hue is set to the different categories
#alpaha sets the transparency levels of the points 
#s sets the size of the markers 
#palette gives each category a color
sns.scatterplot(x=x, y=y, hue=BP_CAT, alpha=0.5, s=100, palette=['red', 'green', 'orange'])

# Customize the plot
plt.title("Systolic vs Diastolic")
plt.ylabel("Diastolic Blood Pressure")
plt.xlabel("Systolic Blood Pressure")

# Move the legend outside the plot
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

# Show the plot
plt.show()


# In[11]:


import pandas as pd
DATA = pd.read_excel('project_table.xlsx') 
HB_lvl= []
NAME = []

#defining the variable the hemoglobin level and the people's name
#Use the bracket to initialize the list

i = 0

#the index starts the beginning

for row in DATA_LIST:
    HB_lvl.append(row[4])
    NAME.append(row[2])
    
#creating the list that reads from the hemoglobin list in row 4 
#and the people's name in row 2

while i < len(HB_lvl):
    
#creates the while loop statement that 
#reads the length of the hemoglobin list

    if HB_lvl[i]<12:
        split_name = NAME[i].split()
        print('HB level =', HB_lvl[i], f"gm/dL ({split_name[1]} {split_name[0][0]}.)")
        i += 1
        
#if the hemoglobin level is less than 12
#then it will split the name that will print out
#full last name and only first initial of the first name

    else:
        i += 1
        
#if condition does not statisfy then it will move on the next list
# the i += 1 stop the while loop going infinite by adding 1











# In[12]:


import pandas as pd
DATA = pd.read_excel('project_table.xlsx') 
BL_S= []
NAME = []

#defining the variable the blood sugar level and the people's name
#Use the bracket to initialize the list

i = 0

#the index starts the beginning

for row in DATA_LIST:
    BL_S.append(row[3])
    NAME.append(row[2])
    
#creating the list that reads from the blood sugar level list in row 3 
#and the people's name in row 2

while i < len(BL_S):
    
#creates the while loop statement that 
#reads the length of the blood sugar level list

    if BL_S[i]>100:
        split_name = NAME[i].split()
        print('Sugar level =', BL_S[i], f"gm/dL ({split_name[1]} {split_name[0][0]}.)")
        i += 1
        
#if the sugar blood level is more than 100
#then it will split the name that will print out
#full last name and only first initial of the first name

    else:
        i += 1
#if condition does not statisfy then it will move on the next list
# the i += 1 stop the while loop going infinite by adding 1











# In[ ]:





# In[ ]:





# In[ ]:




