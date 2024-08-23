import glob
import os
import pandas as pd
import matplotlib.pyplot as plt

def read_queries(file_path):
    with open(file_path, 'r') as file:
        queries = file.read().split(';')
    return [query.strip() for query in queries if query.strip()]

def find_csv_files(root_folder):
    return glob.glob(os.path.join(root_folder, '*.csv.gz'))

def load_and_concatenate_data(csv_files):
    # Use a generator to read and concatenate dataframes to save memory
    dataframes = (pd.read_csv(file, compression='gzip') for file in csv_files)
    concatenated_df = pd.concat(dataframes, ignore_index=True)
    return concatenated_df

def process_data(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['interval_start'] = df['timestamp'].dt.floor('15T')
    result_df = df.groupby('interval_start').size().reset_index(name='transaction_count')
    return result_df

def visualize_data(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['interval_start'], df['transaction_count'], marker='o')
    plt.title('Number of Transactions per 15-Minute Interval')
    plt.xlabel('Time Interval')
    plt.ylabel('Number of Transactions')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

def main():
    # Find all CSV files in the root folder
    root_folder = '.'  # Update with your root folder path if different
    csv_files = find_csv_files(root_folder)
    
    if not csv_files:
        print("No CSV files found in the specified directory.")
        return
    
    # Load and concatenate data from all CSV files
    concatenated_df = load_and_concatenate_data(csv_files)
    
    # Process the data according to the query
    processed_df = process_data(concatenated_df)
    
    # Visualize the data
    visualize_data(processed_df)

if __name__ == "__main__":
    main()