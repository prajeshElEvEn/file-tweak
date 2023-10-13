import os
from scripts import textToCSV

input_file_path = os.path.join('data', 'input')
output_file_path = os.path.join('data', 'output')
input_file_name = "data.txt"
output_file_name = "data.csv"

textToCSV.textToCSV(input_file_path, input_file_name,
                    output_file_path, output_file_name)
