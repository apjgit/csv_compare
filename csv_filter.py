
import csv


def filter_csv(input_file, output_file, filter_values, column_index):
    """
    Filters rows in a CSV file based on given values for a specific column and writes the result to a new file.

    :param input_file: Path to the input CSV file
    :param output_file: Path to the output CSV file
    :param filter_values: List of values to filter by (it checks if the column value is in this list)
    :param column_index: Index of the column to filter on (0-based index)
    """
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        rows = list(reader)

        # Filter rows based on the given column and values
        filtered_rows = [row for row in rows if row[column_index] in filter_values]

    # Write the filtered rows to the output file (without header)
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(filtered_rows)  # Write only the filtered rows without the header

    print(f"Filtered rows have been saved to {output_file}")
    print(filtered_rows)


def main():
    # Example usage
    input_file = 'old_file.csv'  # Your input CSV file path
    output_file = 'filtered_file.csv'  # Output file path for filtered data
    filter_values = ['ID1', 'one']  # List of values to filter on (for example: filtering names)
    column_index = 0  # The column index to filter on (e.g., 1 for 'Name')

    output_file2 = 'filtered_file2.csv'  # Output file path for filtered data
    filter_values2 = ['ID2', 'two']  # List of values to filter on (for example: filtering names)
    filter_csv(input_file, output_file, filter_values, column_index)
    filter_csv(input_file, output_file2, filter_values2, column_index)


if __name__ == "__main__":
    main()
