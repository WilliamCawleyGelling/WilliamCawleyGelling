# -*- coding: utf-8 -*-
"""
Data Cleaning

Created by William Cawley Gelling on 09/08/22. 

Data Cleaning package to be used for Data_Recruitment_Exercise.xlsx
"""

import pandas as pd 
import numpy as np 



def readData(fileName,sheetName) :
    """
    :type fileName: str
    :rtype: pd.DataFrame
    
    Reads the data from fileName and returns a dataframe with the data from sheetName
    """
    return pd.read_excel(fileName, sheetName)
    

#Function to check which columns have no data in them and then drops them 
def dropEmptyColumns(data):

    """
    :type data: pd.DataFrame
    
    Drops columns with where all values are NaN
    """
    for column in data.columns:
        if data[column].isnull().all():
            data.drop(column, axis=1, inplace=True)

def MergeColumbs(data, cols): 
    """
    :type data: pd.DataFrame
    :type cols: list[str]
    
    Merges the columbs in cols into one column cols[0] 
    """

    for col in cols:
        data[cols[0]] = data[cols[0]] + data[col]
        data.drop(col, axis=1, inplace=True)
    

def deleteColumbs(data, cols): 
    """
    :type data: pd.DataFrame
    :type cols: list[str]
    
    Deletes the columbs in cols from the dataframe 
    """
    for i in cols:
        data.drop(i, axis=1, inplace=True)
    
def deleteSameColumbs(data, cols):
    """
    :type data: pd.DataFrame
    :type cols: list[str]

    Deleats columns in cols if they are the same as cols[0] 
    
    """
    for i in range(1, len(cols)) :
        if data[cols[0]].equals(data[cols[i]]):
            data.drop(cols[i], axis=1, inplace=True)



def combineNullElements(data, col1, col2):
    """
    :type data: pd.DataFrame
    :type col1: str
    :type col2: str

    Combines col2 into col1 for elements where col1 is null
    """
    
    if len(data[col1]) != len(data[col2]): 
        raise Exception("The columns are not the same length")
    
    for i in range(len(data[col1])): 
        if np.isnan(data.at[i,col1]):
            if not np.isnan(data.at[i,col2]):
                data.at[i,col1] = data.at[i,col2]
                            
    data.drop(col2, axis=1, inplace=True)
    
def fillNaN(data,col):
    """
    :type data: pd.DataFrame
    :type col: str    
    
    replaces NaN with 0 in column col
    """
    data[col] = data[col].replace(np.nan, 0)

def replaceValues(data,oldValues, newValues): 
    """
    :type data: pd.DataFrame
    :type oldValues: list
    :type newValues: list

    Replaces oldValues with newValues in data
    """
    for i in range(len(oldValues)):
        data = data.replace(oldValues[i], newValues[i])

    
    

def printToExcel(data, fileName, sheetName):
    """
    :type data: pd.DataFrame
    :type fileName: str
    :type sheetName: str
    """
    data.to_excel(fileName, sheetName)
    
def runCleaning(fileName, sheetName, printFileName, printSheetName):
    """
    :type fileName: str
    :type sheetName: str
    :type printFileName: str
    :type printSheetName: str

    Runs the cleaning functions on the data in fileName and prints the results to printFileName and printSheetName
    functions can be commented out are changed depending on what you want to do with the data
    """
    data = readData(fileName, sheetName) #read data from fileName and sheetName

    dropEmptyColumns(data) #Removes columns with no data in them these are TRANS_DATE, CUST_ALT_REGION, NOTES, CUST_NOTES, SPECIAL_REQUEST, DISCOUNT_C 

    deleteSameColumbs(data, ["REGION", "CUST_REGION", "CUST_AREA"]) #this leaves REGION 
    
    deleteSameColumbs(data, ["DELIVERY_DATE", "MONTH"]) #this leaves DELIVERY_DATE

    deleteColumbs(data, ["NO_OF_ITEMS"]) #deleate No_of_items as there is no need for it 
    
    combineNullElements(data, "ITEM_VOLUME", "ITEM_VOL")
    
    fillNaN(data,"TAX")
    
    replaceValues(data, ["y","n"], ["Y","N"])

    printToExcel(data, printFileName, printSheetName) #Prints the data to an excel file


if __name__ == "__main__": #This runs the code if the script is run directly

    fileName = "Data__Recruitment_Exercise.xlsx" #fthe name of the excel document 

    sheetName = "Raw Data"  #the name of the sheet in the excel document

    printFileName = "Data_Recruitment_Exercise_Cleaned.xlsx" #the name of the excel document to be printed to

    printSheetName = "Cleaned Data" #the name of the sheet in the excel document to be printed to

    runCleaning(fileName, sheetName, printFileName, printSheetName) #Runs the cleaning function on the data in the excel document and prints it to the excel document with the name printFileName and sheetName printSheetName
        
