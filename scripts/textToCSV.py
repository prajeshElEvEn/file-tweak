import os
import csv
from tqdm import tqdm
from termcolor import colored


def textToCSV(input_file_path, input_file_name, output_file_path, output_file_name):
    try:
        input_file = os.path.join(input_file_path, input_file_name)
        output_file = os.path.join(output_file_path, output_file_name)
        print(colored(f"> Converting {input_file} to {output_file}", "green"))
        total_lines = sum(1 for line in open(input_file))

        with open(input_file, 'r') as txt_file, open(output_file, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            for line in tqdm(txt_file, total=total_lines, desc=colored("Converting .txt to .csv", "yellow")):
                data = line.strip().split()
                rank = data[0]
                name = ' '.join(data[1:-3])
                university = data[-3]
                roll_no = data[-2]
                section = data[-1]
                csv_writer.writerow([rank, name, university, roll_no, section])

        print(colored("> Conversion complete", "green"))

    except FileNotFoundError as e:
        print(colored(f"Error: {e}", "red"))
    except Exception as e:
        print(colored(f"An unexpected error occurred: {e}", "red"))
