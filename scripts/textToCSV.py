import os
import csv
from tqdm import tqdm


def textToCSV(input_file_path, input_file_name, output_file_path, output_file_name):
    total_lines = sum(1 for line in open(
        os.path.join(input_file_path, input_file_name)))

    with open(os.path.join(input_file_path, input_file_name), 'r') as txt_file, open(os.path.join(output_file_path, output_file_name), 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        for line in tqdm(txt_file, total=total_lines, desc="Converting .txt to .csv"):
            data = line.strip().split()
            csv_writer.writerow(data)

    print(
        f"Conversion from {input_file_path,input_file_name} to {os.path.join(output_file_path,output_file_name)} is complete.")
