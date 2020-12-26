# CS1210 Homework 4
# EUYSUNG CHA
# A07

import csv
import matplotlib.pyplot as plt

#helper function for counting 
def numCounter(nlist):
    nlist.count(0)
    nlist.count(1)
    nlist.count(2)
    nlist.count(3)
    nlist.count(4)
    nlist.count(5)
    nlist.count(6)
    nlist.count(7)
    nlist.count(8)
    nlist.count(9)
    
    return {0:nlist.count(0), 1:nlist.count(1), 2:nlist.count(2), 3:nlist.count(3), 4:nlist.count(4), 5:nlist.count(5), 6:nlist.count(6), 7:nlist.count(7), 8:nlist.count(8), 9:nlist.count(9), 'total':len(nlist)}


def unpackNumber(number):
    # divide number into integer part and decimal part in list
    list_num=str(float(number)).split('.')
    # find leading number
    lead_num= int(list_num[0][0])
    # make empty list for integer part (with out leading part) and decimal part
    list_int=[]
    list_deci=[]
    # make integer list
    int_part = list((list_num[0][1:]))
    for i in int_part:
            list_int.append(int(i))    
    # make decimal list
    deci_part = list(list_num[1])
    for d in deci_part:
        if int(list_num[1])>0:
            list_deci.append(int(d))
        else:
            list_deci
    # combine those list in tuple
    if lead_num>0:
        return [lead_num],list_int,list_deci
    else:
        return [],list_int,list_deci
    
    
def unpackFile(filename, colnum):
    
    # open and read file
    open_file = open(filename)
    # read file by using csv module and skipping line which contain '#'
    read_file = csv.reader(line for line in open_file if not line.startswith('#'))
    # empty list for dataset
    column_list=[]
    unpackNum_list=[]
    # empty list for unpackNumber
    leading_list=[]
    int_list=[]
    deci_list=[]
    # append data in specific column    
    for row in read_file:
        column_list.append(row[colnum])
        
    # list for data with unpackNumber
    for num in column_list:
        unpackNum_list.append(unpackNumber(num))
        
    # make three different list (leading, non-leading, decimal place)    
    for l in range(len(unpackNum_list)):
        leading_list.append(unpackNum_list[l][0])
    for i in range(len(unpackNum_list)):
        int_list.append(unpackNum_list[i][1])
    for d in range(len(unpackNum_list)):
        deci_list.append(unpackNum_list[d][2])
            
    # make a dictionary for each dataset (leading, non-leading, decimal place)    
    x = numCounter(sum(leading_list,[]))
    y = numCounter(sum(int_list,[]))
    z = numCounter(sum(deci_list,[]))
        
    
    # return tuple with three element    
    return x,y,z
            
x,y,z=unpackFile('dowjones.csv',1)
def plotDistribution(D, title='Digit Distribution', xaxis='digit', yaxis='percent'):
    # delete item 'total' from dictionary
    del D['total']
    # set information of graph
    plt.title(title)
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    # set range of graph
    plt.bar(range(len(D)), D.values())
    # label axis
    plt.xticks(range(0,len(D)+1,2), [0,2,4,6,8,10])
    plt.yticks(range(0,len(D),len(D)//5),['0.20', '0.40', '0.60', '0.80', '1.00'])
    plt.show( )



