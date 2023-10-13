import os
from termcolor import colored
from pyfiglet import figlet_format
from scripts import textToCSV

input_file_path = os.path.join('data', 'input')
output_file_path = os.path.join('data', 'output')
input_file_name = "data.txt"
output_file_name = "data.csv"

ascii_art = figlet_format("file-tweak", font="slant")
colored_ascii_art = colored(ascii_art, color='blue')
print(colored_ascii_art)
print(colored("by @eleven", color='grey'))
print(colored("----------------------------------------------------", color='grey'))

textToCSV.textToCSV(input_file_path, input_file_name,
                    output_file_path, output_file_name)

print(colored("----------------------------------------------------", color='grey'))
