import csv


def read_csv(file_path):
    """Read a CSV file and return a list of dictionaries."""
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]


def compare_csv(old_file, new_file):
    """Compare two CSV files using the 'ID' field as the unique identifier and compare all fields."""
    old_data = read_csv(old_file)
    new_data = read_csv(new_file)

    # Create dictionaries for fast lookup using 'ID' as the unique key
    old_dict = {row['ID']: row for row in old_data}
    new_dict = {row['ID']: row for row in new_data}

    added = []
    removed = []
    modified = []

    # Check for added and modified rows
    for new_row_id, new_row in new_dict.items():
        if new_row_id not in old_dict:
            added.append(new_row)  # Row is new in new_file
        else:
            # Compare all fields for modification
            if new_row != old_dict[new_row_id]:
                modified.append(new_row)

    # Check for removed rows
    for old_row_id, old_row in old_dict.items():
        if old_row_id not in new_dict:
            removed.append(old_row)  # Row is removed from new_file

    return added, removed, modified


def write_to_csv(file_path, data, fieldnames):
    """Write data to a CSV file."""
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def print_comparison(added, removed, modified):
    """Print added, removed, and modified rows."""
    print("Added rows:")
    for row in added:
        print(row)

    print("\nRemoved rows:")
    for row in removed:
        print(row)

    print("\nModified rows:")
    for row in modified:
        print(row)


def main():
    # Paths to the old and new CSV files
    old_file = 'old_file.csv'
    new_file = 'new_file.csv'

    # Read the first file to get the fieldnames (headers) dynamically
    with open(old_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames  # Get headers dynamically

    # Compare the two CSV files
    added, removed, modified = compare_csv(old_file, new_file)

    # Write added, removed, and modified data to separate CSV files
    write_to_csv('added.csv', added, fieldnames)
    write_to_csv('removed.csv', removed, fieldnames)
    write_to_csv('modified.csv', modified, fieldnames)

    # Print the results
    print_comparison(added, removed, modified)


if __name__ == "__main__":
    main()
