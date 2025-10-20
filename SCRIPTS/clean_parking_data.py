import pandas as pd
import os
from datetime import datetime

def clean_parking_data():

    input_file = "DATA/Initial/Parking_Tickets.csv"
    output_file = "DATA/Final/cleaned_parking_tickets.csv"
    
    os.makedirs("DATA/Final", exist_ok=True)
    
    print("Loading parking ticket data...")
    df = pd.read_csv(input_file)
    
    print(f"Original data shape: {df.shape}")
    
    cleaned_data = pd.DataFrame()
    
    print("Processing dates...")

    df['DateIssued'] = pd.to_datetime(df['DateIssued'], errors='coerce')

    df = df.dropna(subset=['DateIssued'])
    
    print("Filtering to years 2000-2024...")
    df = df[(df['DateIssued'].dt.year >= 2000) & (df['DateIssued'].dt.year <= 2024)]
    print(f"Records after year filtering: {len(df)}")

    df['DateTime'] = pd.to_datetime(df['DateIssued'].dt.strftime('%Y-%m-%d') + ' ' + df['TimeIssued'].astype(str), errors='coerce')
    cleaned_data['IssuedDate'] = df['DateTime'].dt.strftime('%m/%d/%Y, %I:%M %p')
    
    print("Adding time series features...")
    cleaned_data['Year'] = df['DateIssued'].dt.year
    cleaned_data['DayOfWeek'] = df['DateIssued'].dt.day_name()
    cleaned_data['Quarter'] = df['DateIssued'].dt.quarter
    
    print("Processing street names...")
    cleaned_data['StreetName'] = df['StreetName'].str.strip()
    
    print("Processing times...")

    time_series = df['TimeIssued'].astype(str)
    
    def format_time(time_str):
        try:
            if ':' in time_str:
                time_obj = datetime.strptime(time_str.strip(), '%H:%M')
                return time_obj.strftime('%I:%M %p')
            elif len(time_str.strip()) == 4 and time_str.strip().isdigit():
                hour = int(time_str.strip()[:2])
                minute = int(time_str.strip()[2:])
                time_obj = datetime.strptime(f"{hour:02d}:{minute:02d}", '%H:%M')
                return time_obj.strftime('%I:%M %p')
            else:
                return time_str.strip()
        except:
            return time_str.strip()
    
    cleaned_data['TimeIssued'] = time_series.apply(format_time)
    
    print("Adding time-based encoding...")
    def extract_hour(time_str):
        try:
            if ':' in time_str and ('AM' in time_str or 'PM' in time_str):
                time_obj = datetime.strptime(time_str.strip(), '%I:%M %p')
                return time_obj.hour
            elif len(time_str) == 4 and time_str.isdigit():
                return int(time_str[:2])
            return None
        except:
            return None
    
    def get_time_period(hour):
        if hour is None:
            return 'Unknown'
        elif 6 <= hour < 12:
            return 'Morning'
        elif 12 <= hour < 18:
            return 'Afternoon'
        elif 18 <= hour < 22:
            return 'Evening'
        else:
            return 'Night'
    
    cleaned_data['Hour'] = cleaned_data['TimeIssued'].apply(extract_hour)
    cleaned_data['TimePeriod'] = cleaned_data['Hour'].apply(get_time_period)
    
    print("Processing violation descriptions...")
    cleaned_data['ViolationDescription'] = df['ViolationDescription']
    
    print("Removing rows with missing data...")
    initial_count = len(cleaned_data)
    cleaned_data = cleaned_data.dropna(subset=['IssuedDate', 'StreetName', 'TimeIssued', 'ViolationDescription'])
    final_count = len(cleaned_data)
    
    print(f"Removed {initial_count - final_count} rows with missing data")
    print(f"Final data shape: {cleaned_data.shape}")
    
    print(f"Saving cleaned data to {output_file}...")
    # Save with proper encoding for time series data
    cleaned_data.to_csv(output_file, index=False, encoding='utf-8')
    
    print("Data cleaning completed successfully!")
    print(f"Cleaned data saved to: {output_file}")
    
    print("\nSample of cleaned data:")
    print(cleaned_data.head())
    
    return cleaned_data

if __name__ == "__main__":
    clean_parking_data()
