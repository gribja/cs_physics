# newton's method for backward interpolation

#importing array manipulation libray numpy to generate a sample dataset
import numpy as np


#function for calculating factorial of a given number.
""" Although there's a function available in python built-in math module "factorial()",
i'm still defining this as a purpose of learning"""

def fac(n):
    f = 1
    for i in range(2,n+1):
        f*=i
    return f

# two sample datasets, each having 5 elements are assigned to two variables xs and ys
# linspace function create an array of evenly spaced values (number odf samples)
xs = np.linspace(5,25,5) 
ys = np.linspace(2,5,5)

# function for calculating the value of polynomial of u
def u_dec(u,n):
    x_temp = u
    for i in range(0,n):
        x_temp *= (u+i)
        return x_temp

# function to determine the value of y using backward interpolation
# three parameters of this function goes this way
# x : the given number for which we have to find the corresponding y value(interpolating point)
# xp,yp : the datasets that make sense

def backward(x,xp,yp):
    n = len(xp)  # length of xp dataset
    y_diff = np.zeros((n,n))  # initialising an (n x n) dimensional matrix containing only zeros
    
    for i in range(0,n):
        y_diff[i][0] = yp[i]

    # for calculation of difference table
    for i in range(1,n):
        for j in reversed(range(i,n)):
            y_diff[j][i] = y_diff[j][i-1] - y_diff[j-1][i-1]

    print(y_diff)  #print the difference table

    sum = y_diff[n-1][0] # declare a variable assigning the value of the first element of first row.
    
    u = (x - xp[n-1])/(xp[1]-xp[0]) # calculating the value of u

    for i in range(1,n):
        sum += (u_dec(u,i)*y_diff[n-1][i])/fac(i)  # applying the formula to sum-up everything together

    return sum

print(xs)
print(ys)
print(backward(35,xs,ys)) # calling the function with necessary parameters
