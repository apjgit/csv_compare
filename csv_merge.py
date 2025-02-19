import csv

# List of CSV files
csv_files = ['file2.csv','file1.csv']  # Replace with actual file names

# Open the output file for writing the combined data
with open('combined_file.csv', 'w', newline='') as combined_file:
    writer = csv.writer(combined_file)

    # Loop through each CSV file
    for file in csv_files:
        # Open the current CSV file for reading
        with open(file, 'r') as f:
            reader = csv.reader(f)

            # Write the header and data rows
            for i, row in enumerate(reader):
                # Write the header each time, even if it's not the first file
                writer.writerow(row)

print("CSV files have been successfully combined with headers from all files.")