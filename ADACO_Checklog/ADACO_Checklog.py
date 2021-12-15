import csv
import os


def row_cleaner(row):
    clear = True
    while clear:
        for cell in row:
            if cell == '':
                row.remove(cell)
        if row.count('') == 0:
            clear = False
    return row


def index_finder(list, elem):
    for sub_list in list:
        if elem in sub_list:
            return list.index(sub_list)
            


path = r"S:\Accounting\Javier\Checkbook\outlets sheets\2021\December"

os.chdir(path)

asset_files = os.listdir()
print(asset_files)
new_lines = []
for file in asset_files:

    if '.csv' in file:

        with open(file) as file:
            file_reader = csv.reader(file, dialect="excel")
            line_list = []
            for row in file_reader:
                clean_row = row_cleaner(row)
                if len(clean_row) > 0:
                    line_list.append(clean_row)
                #print(row)
                #print(len(row))
            start_line = index_finder(line_list, 'Other Expenses')
            end_line = index_finder(line_list, 'Total Other Expenses')
   
            print(start_line, end_line)
            for elem in line_list[start_line:end_line]:

                new_lines.append(elem[5:])
        #print(new_lines)

with open(path+'\\'+"cleared_data.csv", "w", newline="") as new_file:
    writer = csv.writer(new_file)
    writer.writerows(new_lines)