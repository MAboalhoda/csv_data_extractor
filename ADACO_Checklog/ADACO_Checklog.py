import csv
import os, pprint
from depts import departments, expense_code


def row_cleaner(row):
    """This function is to clear all the empty vlaued elements in each row"""
    clear = True
    while clear:
        for cell in row:
            if cell == '':
                row.remove(cell)
        if row.count('') == 0:
            clear = False
    return row


def index_finder(list, elem):
    """this function is to get the index of the targeted element in the nested list"""
    for sub_list in list:
        if elem in sub_list:
            return list.index(sub_list)
            


path = r"file location"

os.chdir(path)

asset_files = os.listdir()
#print(asset_files)
new_lines = []
for file in asset_files:

    if '.csv' in file:

        with open(file) as file:
            file_reader = csv.reader(file, dialect="excel")
            line_list = []
            #here we clean the row from the empty values and make nested list for each row to loop through it
            for row in file_reader:
                clean_row = row_cleaner(row)
                if len(clean_row) > 0:
                    line_list.append(clean_row)
                #print(clean_row)
                #print(len(row))
            #below we get the indexs for the lines that we need to loop in and fitch the vlaues targeted

            start_line = index_finder(line_list, 'Other Expenses')
            end_line = index_finder(line_list, 'Total Other Expenses')
            

            #in the below we get the department code to map it in the system
            department_code = ''
            for elem in line_list:
                for key in departments:
                    if key == elem[0]:
                        department_code = departments[elem[0]]
                        #print(departments[elem[0]])

            #here we get the account code
            #for elem in line_list:
            #    if len(line_list) > 1:
            #        for key in expense_code:
            #            if key == elem[0]:
            #                print(key, expense_code[elem[0]])

            
            #print(start_line, end_line)
        for elem in line_list[start_line:end_line]:
            line = []
            if len(elem) > 1:
                line.insert(0,department_code)
                for key in expense_code:
                    if key == elem[0]:
                        line.insert(1,expense_code[elem[0]])
                line.extend(elem[5:])

                new_lines.append(line)
        #print(new_lines)


with open(path+'\\'+"cleared_data.csv", "w", newline="") as new_file:
    writer = csv.writer(new_file)
    writer.writerows(new_lines)

if __name__ == "__main__":
    __name__