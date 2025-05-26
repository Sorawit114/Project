import os
import pandas as pd

def load_all_data(data_folder):
    all_files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]
    df_list = []
    for file in all_files:
        file_path = os.path.join(data_folder, file)
        try:
            # อ่านไฟล์แบบไม่เกิด error ถ้าไฟล์ว่างจะข้าม
            df = pd.read_csv(file_path, header=0)
            if df.empty:
                print(f"Warning: '{file}' is empty, skipping.")
                continue
            # กรองแถว header ซ้ำ
            df = df[df['Price'] != 'Ticker']
            df['Ticker'] = file.replace('.csv', '')
            df_list.append(df)
        except pd.errors.EmptyDataError:
            print(f"Warning: '{file}' is empty or corrupted, skipping.")
        except Exception as e:
            print(f"Warning: Failed to read '{file}': {e}")
    if not df_list:
        raise ValueError("No valid CSV data found in folder.")
    combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df

def save_combined_data():
    data_folder = 'data'
    combined_df = load_all_data(data_folder)
    combined_df.to_csv(os.path.join(data_folder, 'stock_data.csv'), index=False)
    print(f"Combined data saved to {os.path.join(data_folder, 'stock_data.csv')}")

if __name__ == '__main__':
    save_combined_data()
