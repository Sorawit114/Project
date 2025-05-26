import os
import pandas as pd

def load_all_data(data_folder):
    all_files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]
    df_list = []
    for file in all_files:
        file_path = os.path.join(data_folder, file)
        df = pd.read_csv(file_path, header=0)
        # กรองแถวที่เป็น header ซ้ำออก
        df = df[df['Price'] != 'Ticker']
        df['Ticker'] = file.replace('.csv', '')
        df_list.append(df)
    combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df

def main():
    data_folder = 'data'
    df = load_all_data(data_folder)
    print(df.head())

if __name__ == '__main__':
    main()
