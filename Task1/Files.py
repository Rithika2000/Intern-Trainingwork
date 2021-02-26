import ClointFusion as cf
import os

#checking current file directory
excelpath = os.getcwd() + "\Excel.xlsx"
print(excelpath)

#Gives all the columns in the excel file
header_columns = cf.excel_get_all_header_columns(excelpath)
for i in header_columns:
    print(i)

#to get row and column count

row,column  = cf.excel_get_row_column_count(excelpath)

print(row)
print(column)

#gives the name of the excel sheet 
sheet_name = cf.excel_get_all_sheet_names(excelpath)
print(sheet_name)

#removes duplicates w.r.t ID column 

cf.excel_remove_duplicates(excel_path = excelpath,sheet_name='Sheet1',header=0,columnName='ID ',saveResultsInSameExcel=True,which_one_to_keep='first')


#to sort a particular column

cf.excel_sort_columns(excelpath,'Sheet1',header=0,secondColumnToBeSorted= "OrderDate",secondColumnSortType=True)


Data = {'ID ': 91, 'OrderDate' : '2020-4-14' , 'Region' : 'East','Rep' : 'Jones','Item' : 'Binder','Units' : 60,'UnitCost' : 4.99,'Total' : 449.1}
for i in range(0,8):
    cf.excel_set_single_cell(excelpath,'Sheet1',header=0,columnName=list(Data.keys())[i],cellNumber=i,setText=list(Data.values())[i])
    

# Lets first create a separate folder to hold split excel files

excelpath1 = os.getcwd() + "\Split"

cf.folder_create(excelpath1)

# Use this function to splits the excel file as per given row limit
cf.excel_split_the_file_on_row_count(excelpath,sheet_name='Sheet1', rowSplitLimit=12, outputFolderPath=excelpath1)


# Initializing dictionary
Dict = {}


for i in range(row-1):
    key = cf.excel_get_single_cell(excel_path=excelpath,sheet_name='Sheet1',header=0,columnName='ID ',cellNumber=i)
    value = cf.excel_get_single_cell(excel_path=excelpath,sheet_name='Sheet1',columnName='Units',cellNumber=i)
    Dict[key] = value

print(Dict)



