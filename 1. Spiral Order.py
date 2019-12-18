import numpy as np

##################################
##Defining the matrix (2D array)##
##################################

temp = np.arange(0,36,1)
arr = np.reshape(temp, [9,4])
print(arr)

##################################################################
##Defining print functions for priting in a particular direction##
##################################################################

def print_right(row_num, start, stop, arr = arr):
    for i in range(start, stop+1):
        print(arr[row_num][i])
        
def print_left(row_num, start, stop, arr = arr):
    for i in range(stop, start-1, -1):
        print(arr[row_num][i])
        
def print_down(col_num, start, stop, arr = arr):
    for i in range(start, stop+1):
        print(arr[i][col_num])
        
def print_up(col_num, start, stop, arr = arr):
    for i in range(stop, start-1, -1):
        print(arr[i][col_num])

##################################
##Code for spiral order printing##
##################################

def spiral_order(arr):
    start_row = 0 
    stop_row = arr.shape[0] - 1
    start_col = 0
    stop_col = arr.shape[1] - 1
    flag = 0
    while(flag == 0):
        if(start_col < stop_col):
            print_right(start_row, start_col, stop_col, arr)
            start_row += 1
        if(start_row < stop_row):
            print_down(stop_col, start_row, stop_row, arr)
            stop_col -= 1
        if(start_col < stop_col):
            print_left(stop_row, start_col, stop_col, arr)
            stop_row -= 1
        if(start_row < stop_row):
            print_up(start_col, start_row, stop_row, arr)
            start_col += 1
        if((start_row >= stop_row) or (start_col >= stop_col)):
            flag = 1
    
if __name__== "__main__":
    spiral_order(arr)
