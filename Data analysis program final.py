# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 14:03:23 2021

@author: nstam
"""

# Reading an excel file using Python
import xlrd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.transforms as mtransforms
from statistics import mean
 
# Give the location of the file
loc = ("C:\TIm Gay Research\camera interferometer data.xlsx")
volt_1 = []
volt_2 = []
volt_diff = []
pos_1 = []
pos_2 = []
pos_3 = []
pos_4 = []
min_disp_1 = []
min_disp_2 = []
min_width_1 = []
min_width_2 = []
fringe_size = []
fringe_displacement = []
fringe_shift = []
data_points = []
uncertainty_disp = []
uncertainty_width = []
uncertainty_shift = []
uncertainty_voltage = []
unc = []
delta = 0.0
weight = []

a = 0.0
b = 0.0

# To open Workbook

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
 
# For row 0 and column 0
for i in range(1, sheet.nrows):
    volt_1.append(sheet.cell_value(i,0))
    
for i in range (1,sheet.nrows):
    pos_1.append(sheet.cell_value(i, 1))
    
for i in range(1, sheet.nrows):
    pos_2.append(sheet.cell_value(i,2))
    
for i in range(1, sheet.nrows):
    volt_2.append(sheet.cell_value(i,3))
    
for i in range(1, sheet.nrows):
    pos_3.append(sheet.cell_value(i,4))

for i in range(1, sheet.nrows):
    pos_4.append(sheet.cell_value(i,5))

for i in range(1, sheet.nrows):
    a = sheet.cell_value(i,6)
    uncertainty_disp.append(np.sqrt(a*a+a*a))
    
for i in range(1, sheet.nrows):
    b = sheet.cell_value(i,6)
    uncertainty_width.append(np.sqrt(b*b+b*b))
    
for i in range(1, sheet.nrows):
    c = sheet.cell_value(i,7)
    uncertainty_voltage.append(np.sqrt(c*c + c*c))
    
for i in range(sheet.nrows-1):
    min_disp_1.append(pos_3[i]-pos_1[i])    
#print(min_disp_1)

for i in range(sheet.nrows-1):
    min_disp_2.append(pos_4[i]-pos_2[i])    
#print(min_disp_2)

for i in range(sheet.nrows-1):
    min_width_1.append(pos_2[i]-pos_1[i])
#print(min_disp_1)

for i in range(sheet.nrows-1):
    min_width_2.append(pos_4[i]-pos_3[i])
#print(min_disp_2)

for i in range(sheet.nrows-1):
    fringe_size.append((min_width_1[i]+min_width_2[i])/2.)
#print(fringe_size)

for i in range(sheet.nrows-1):
    fringe_displacement.append((min_disp_1[i]+min_disp_2[i])/2.)
    
for i in range(sheet.nrows-1):
    fringe_shift.append((fringe_displacement[i]/fringe_size[i]))


volt_1 = np.array(volt_1)
volt_2 = np.array(volt_2)
volt_diff = volt_2-volt_1

data_point = list(zip(volt_diff, fringe_shift))

#fit to y = a + bx

#calculate uncertainty in data points

for i in range(sheet.nrows-1):
    p = uncertainty_disp[i]/fringe_displacement[i]
    w = uncertainty_width[i]/fringe_size[i]
    uncer = fringe_shift[i]*np.sqrt(p*p + w*w)
    uncertainty_shift.append(uncer)

#make uncertainty into a matrix
def unc_calc(unc_1, unc_2):
    uncertainty = []
    for i in range(1,len(unc_2)):
        uncertainty.append(np.sqrt(unc_1[i]**2 + unc_2[i]**2))
    return uncertainty
unc = unc_calc(uncertainty_voltage, uncertainty_shift)

#calculate Delta from Bevington  for y = a + bx

def delta_calc(x, y, unc):
    first = 0
    second = 0
    third = 0
    Delta = 0
    for i in range(1, len(unc)):
        first = first + (1/(unc[i]*unc[i]))
        second = second + (x[i]*x[i])/(unc[i]*unc[i])
        third = third + x[i]/(unc[i]*unc[i])
    Delta = first*second-third*third
    return(Delta)

delta= delta_calc(volt_diff, fringe_shift, unc) 


def a_calc(x,y,unc,delta):
    first = 0
    second = 0
    third = 0
    fourth = 0
    fifth = 0
    A = 0
    for i in range(1, len(unc)):
        first = first + (x[i]*x[i])/(unc[i]*unc[i])
        second = second + (y[i])/(unc[i]*unc[i])
        third = third + x[i]/(unc[i]*unc[i])
        fourth = fourth + (x[i]*y[i])/(unc[i]*unc[i])
        fifth = fifth + (x[i]*x[i])/(unc[i]*unc[i])
    A = (first * second - third*fourth)/delta
    fifth = fifth/delta
    print("Error in a=" ,fifth)
    return(A)
    
a = a_calc(volt_diff, fringe_shift, unc, delta)  

def b_calc(x, y, unc, delta):
    first = 0
    second = 0
    third = 0
    fourth = 0
    fifth = 0
    B = 0
    #for i in range(1, len(uncer_y)):
        #uncer.append(np.sqrt(uncer_x[i]*uncer_x[i]+ uncer_y[i]*uncer_y[i]))
    for i in range(1, len(unc)):
        first = first + 1/(unc[i]*unc[i])
        second = second + (x[i]*y[i])/(unc[i]*unc[i])
        third = third + x[i]/(unc[i]*unc[i])
        fourth = fourth + (y[i])/(unc[i]*unc[i])
        fifth = fifth + 1/(unc[i]*unc[i])
    B = (first * second - third*fourth)/delta
    fifth = fifth/delta
    print("Error in b=", fifth)
    return(B)
    

b = b_calc(volt_diff, fringe_shift, unc, delta)           
           
print("Delta =", delta)
print("a=", a)
print("b =", b)

def abline(slope, intercept):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '--')


fig = plt.subplots()
x = volt_diff
y = fringe_shift
yerr = uncertainty_shift
plt.errorbar(x, y, yerr, fmt = 'o')
abline(b,a)
plt.xlabel("Change in Voltage")
plt.ylabel("Fringe Shift")
plt.title("Fringe Shift vs Change in Voltage")

mu = mean(fringe_shift)

#calculate standard deviation

def calc_std_dev(x, y, mu):
    variance = 0
    std_dev = 0
    for i in range(len(y)):
        variance = variance + (y[i] - mu)**2
    std_dev = np.sqrt(variance/len(y))
    return(std_dev)
    
s_deviation = 0
s_deviation = calc_std_dev(volt_diff, fringe_shift, mu)

print("Standard Deviation =", s_deviation)
#***calculate weighted average***

#calculate weights
def weight_calc(uncert):
    weight = []
    for i in range(1,len(uncert)):
        weight.append(1/(uncert[i]*uncert[i]))
    return weight

weight = weight_calc(unc)

def weighted_average(weight, x):
    w_ave = 0
    first = 0
    second = 0
    for i in range(1, len(weight)):
       first = first + (weight[i]*y[i])
       second = second + weight[i]
    w_ave = first/second
    return w_ave

weighted_ave = weighted_average(weight, fringe_shift)

print("Mean fringe shift", mean(fringe_shift))

print("Weighted average", weighted_average(weight, fringe_shift) )

print("Cacluated Standard Deviation", calc_std_dev(volt_diff, fringe_shift, weighted_ave))

#chi_square calculation
def chi_square(x, y, slope, intercept):
    chi_sq = 0
    for i in range(1, len(y)):
        chi_sq = chi_sq + ((y[i]-(slope*x[i]+intercept))**2)/(slope*x[i]+intercept)
    return chi_sq

chi_square(volt_diff, fringe_shift, b, a)
print("Chi-square =" , chi_square(volt_diff, fringe_shift,b,a))
print("Reduced chi-square = ", chi_square(volt_diff, fringe_shift, b, a)/len(fringe_shift))