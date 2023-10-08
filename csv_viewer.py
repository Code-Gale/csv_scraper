import csv

# Ask the user for the CSV file path
csv_file_path = input("Enter the path to your CSV file: ")

try:
    # Open the CSV file in read mode
    with open(csv_file_path, mode='r', newline='') as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)
        
        # Check if the file is empty
        if not csv_reader.fieldnames:
            print("The CSV file is empty.")
        else:
            # Print the header row with field names
            field_names = csv_reader.fieldnames
            print("CSV file header:", field_names)
            
            # Provide a list of available fields for the user to choose from
            print("Available fields:")
            for field in field_names:
                print(field)
            
            # Ask the user which field to scrape
            field_to_scrape = input("Enter the field name to scrape: ")
            
            # Verify that the chosen field exists in the CSV
            if field_to_scrape not in field_names:
                print(f"Field '{field_to_scrape}' not found in the CSV file.")
            else:
                # Create a text file to save the scraped data
                output_file_path = input("Please enter output file name: ")
                
                # Open the output file for writing
                with open(output_file_path, mode='w') as output_file:
                    # Display all rows and save the selected field to the output file
                    for row in csv_reader:
                        if field_to_scrape in row:
                            scraped_data = row[field_to_scrape]
                            print(f"{field_to_scrape}: {scraped_data}")
                            output_file.write(scraped_data + "\n")
                
                print(f"Scraped data from '{field_to_scrape}' field has been saved to '{output_file_path}'")
except FileNotFoundError:
    print(f"The file '{csv_file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
