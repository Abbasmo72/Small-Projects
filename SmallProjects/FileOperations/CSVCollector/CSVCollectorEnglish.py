import pandas as pd
import os

def combine_csv_files(input_folder, output_file):
    """
    Combines all CSV files in a given folder into a single CSV file.

    Args:
        input_folder (str): Path to the folder containing CSV files.
        output_file (str): Path to save the combined CSV file.

    Returns:
        None
    """

    # Check if the input folder exists
    if not os.path.exists(input_folder):
        print(f"Folder '{input_folder}' does not exist.")
        return

    # Get a list of all CSV files in the folder
    csv_files = [file for file in os.listdir(input_folder) if file.endswith('.csv')]
    if not csv_files:
        print("No CSV files found in the specified folder.")
        return

    # Initialize an empty DataFrame to hold combined data
    combined_data = pd.DataFrame()

    # Iterate through each CSV file and append its data
    for file in csv_files:
        file_path = os.path.join(input_folder, file)
        try:
            print(f"Reading file: {file}")
            data = pd.read_csv(file_path)  # Read the CSV file
            combined_data = pd.concat([combined_data, data], ignore_index=True)  # Combine with existing data
        except Exception as e:
            print(f"Error reading file '{file}': {e}")

    # Save the combined data to a new CSV file
    try:
        combined_data.to_csv(output_file, index=False)
        print(f"Combined file saved as '{output_file}'.")
    except Exception as e:
        print(f"Error saving output file: {e}")

# Define the folder path containing CSV files and the output file path
input_folder_path = "path_to_your_csv_folder"
output_file_path = "combined_output.csv"

# Call the function to combine CSV files
combine_csv_files(input_folder_path, output_file_path)
