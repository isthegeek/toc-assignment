''' TOC Assignment : Question 3 
	Modelling a vending machine (Mealy machine)'''

# Dependencies for the program

import pandas as pd
# pandas is used for querying the state transition table stored as a dataframe 
import sys 
import numpy as np
# item set and cost dictionary 
drinks_menu = {'1_Tea' : 20 , '2_Coffee': 10, '3_Juice' : 15}
# states in the finite state machine 
state_dict = { 'Dispense_Drink' : 0 ,'Tea' : 20, 'Juice' : 15, 'Coffee' : 10 , 'Amount_r20' : 20, 'Amount_r15': 15, 'Amount_r10': 10, 'Amount_r5': 5, 'Return_5_Dispense_Drink': -5}

#aphabet of finite state machine 
alphabet = [0,1,2,3,5,10]


def show_menu():
	print "Drinks Menu\n"
	print(drinks_menu)



current_state = 1
next_state = 1
df = pd.read_csv('state_transition.csv',  sep = ',')
#column names = ['current_state','input','next_state']
# To view the state transition table 
print df 

# TODO : Use dictionary mapping to display the dataframe in natural language 
num_rows = len(df.index) 

#print num_rows

#print list(df.columns.values)


# Returning the next state given the input and current state 
def find_next_state(input_u, current_u):
	for i in range(1,12):
	
		input_m = df.iloc[i,1]
		current_m = df.iloc[i,0]

		if (input_m == input_u and current_m == current_u):
			return df.iloc[i,2]


# Validating the input 
def input_check(current_u, input_u):
	if (current_u == 1 and input_u in [0,1,2,3]):
		return 1
	if (current_u in [1, 20, 15, 10, 5] and input_u in [5,10]):
		return 1

	return 0


def run_test:
	test_df = pd.read_csv('test.csv', sep =  ',')
	test_set =  np.array(test_df)


# TODO write test for the module 