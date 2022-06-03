#CSVtoExcel

import csv
import openpyxl

#Open the CSV File
data = open('C:\\Users\\Dell\\Desktop\\Python Examples\\CSVtoExcel.csv',encoding = 'utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)


#create or open the excel sheet through openpyxl
createexcelsheet = openpyxl.Workbook()
#openexcelsheet = openpyxl.load_workbook(filepath)
excelrow = createexcelsheet.active

for lines in data_lines:
    #Add CSV Data into the Excel Sheet
    excelrow.append(lines)
    
#save the converted data in ExcelSheetData.xlsx file
createexcelsheet.save('C:\\Users\\Dell\\Desktop\\Python Examples\\ExcelSheetData.xlsx')