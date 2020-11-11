
##########################################################
#  Python script template for Question 1 (IAML Level 10)
#  Note that
#  - You should not change the name of this file, 'iaml01cw2_q1.py', which is the file name you should use when you submit your code for this question.
#  - You should write code for the functions defined below. Do not change their names.
#  - You can define function arguments (parameters) and returns (attributes) if necessary.
#  - In case you define additional functions, do not define them here, but put them in a separate Python module file, "iaml01cw2_my_helpers.py", and import it in this script.
#  - For those questions requiring you to show results in tables, your code does not need to present them in tables - just showing them with print() is fine.
#  - You do not need to include this header in your submission.
##########################################################

#--- Code for loading modules and the data set and pre-processing --->
# NB: You can edit the following and add code (e.g. code for loading sklearn) if necessary.

import numpy as np
import scipy
import matplotlib.pyplot as plt
import seaborn as sns
from helpers.iaml01cw2_helpers import *
# from iaml01cw2_my_helpers import *

#<----

# Q1.0
Xtrn, Ytrn, Xtst, Ytst = load_FashionMNIST("/home/ryan/PycharmProjects/INFR10069-2020-CW2/data")
Xtrn_orig = Xtrn
Xtst_orig = Xtst

Xtrn = Xtrn/255
Xtst = Xtst/255

Xmean = []

for i in np.transpose(Xtrn):
    Xmean.append(np.mean(i))
# print(np.shape(Xtrn))

Xtrn_nm = []
for i,j in enumerate(np.transpose(Xtrn)):
    row = []
    # print()
    for x in j:
        row.append(x - Xmean[i])
    Xtrn_nm.append(row)

Xtst_nm = []
for i,j in enumerate(np.transpose(Xtst)):
    row = []
    # print()
    for x in j:
        row.append(x - Xmean[i])
    Xtst_nm.append(row)

# print((Xtrn)[0])
# print(np.transpose(Xtrn_nm)[0])



# print(np.shape(Xtrn))

# Q1.1
def iaml01cw2_q1_1():
    print(Xtrn_nm[0][0:4])
    print(Xtrn_nm[-1][0:4])
iaml01cw2_q1_1()   # comment this out when you run the function

# Q1.2
def iaml01cw2_q1_2():

    print(np.shape(Xtrn))



    pass
# iaml01cw2_q1_2()   # comment this out when you run the function

# Q1.3
def iaml01cw2_q1_3():
    pass
# iaml01cw2_q1_3()   # comment this out when you run the function


# Q1.4
def iaml01cw2_q1_4():
    pass
# iaml01cw2_q1_4()   # comment this out when you run the function


# Q1.5
def iaml01cw2_q1_5():
    pass
# iaml01cw2_q1_5()   # comment this out when you run the function


# Q1.6
def iaml01cw2_q1_6():
    pass
# iaml01cw2_q1_6()   # comment this out when you run the function


# Q1.7
def iaml01cw2_q1_7():
    pass
# iaml01cw2_q1_7()   # comment this out when you run the function


# Q1.8
def iaml01cw2_q1_8():
    pass
# iaml01cw2_q1_8()   # comment this out when you run the function
