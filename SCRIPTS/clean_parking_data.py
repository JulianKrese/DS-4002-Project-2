import pandas as pd
import os
from datetime import datetime
import numpy as np

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
    
    # Engineered numeric features
    cleaned_data['Hour'] = df['DateTime'].dt.hour
    cleaned_data['Month'] = df['DateTime'].dt.month
    cleaned_data['IsWeekend'] = df['DateIssued'].dt.dayofweek.isin([5, 6]).astype(int)
    
    print("Adding time series features...")
    cleaned_data['Year'] = df['DateIssued'].dt.year
    cleaned_data['DayOfWeek'] = df['DateIssued'].dt.day_name()
    # Numeric encoding for DayOfWeek (Mon=0 ... Sun=6, Unknown=-1)
    dow_map = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6
    }
    cleaned_data['DayOfWeekEnc'] = cleaned_data['DayOfWeek'].map(dow_map).fillna(-1).astype(int)
    cleaned_data['Quarter'] = df['DateIssued'].dt.quarter
    
    print("Processing street names...")
    cleaned_data['StreetName'] = df['StreetName'].str.strip()
    # Frequency encoding for StreetName
    street_counts = cleaned_data['StreetName'].value_counts(dropna=False)
    street_freq = street_counts / len(cleaned_data)
    # Map to frequency; unknowns (if any) get global mean
    street_global_mean = float(street_freq.mean())
    cleaned_data['StreetFreqEnc'] = cleaned_data['StreetName'].map(street_freq).fillna(street_global_mean).astype('float32')
    
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
    
    print("Adding time-based encoding...")

    def extract_hour(time_str):
        try:
            if ':' in time_str:
                time_obj = datetime.strptime(time_str.strip(), '%H:%M')
                return time_obj.hour
            elif len(time_str.strip()) == 4 and time_str.strip().isdigit():
                return int(time_str.strip()[:2])
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

    original_hours = time_series.apply(extract_hour)
    cleaned_data['TimePeriod'] = original_hours.apply(get_time_period)

    # Numeric encoding for TimePeriod
    time_period_map = {
        'Night': 0,
        'Morning': 1,
        'Afternoon': 2,
        'Evening': 3,
        'Unknown': -1
    }
    cleaned_data['TimePeriodEnc'] = cleaned_data['TimePeriod'].map(time_period_map).fillna(-1).astype(int)
    
    print("Processing violation descriptions...")
    cleaned_data['ViolationDescription'] = df['ViolationDescription']
    # Ordinal-style encoding for ViolationDescription (stable for this dataset run)
    violation_codes, violation_uniques = pd.factorize(cleaned_data['ViolationDescription'], sort=False)
    # Shift by +1 so that unknowns (if merged later) can use 0
    cleaned_data['ViolationDescEnc'] = (violation_codes + 1).astype('int32')
    
    print("Removing rows with missing data...")
    initial_count = len(cleaned_data)
    cleaned_data = cleaned_data.dropna(subset=['IssuedDate', 'StreetName', 'ViolationDescription'])
    final_count = len(cleaned_data)
    
    print(f"Removed {initial_count - final_count} rows with missing data")
    print(f"Final data shape: {cleaned_data.shape}")
    
    print(f"Saving cleaned data to {output_file}...")
    cleaned_data.to_csv(output_file, index=False, encoding='utf-8')
    
    print("Building encoded numeric feature frame...")
    encoded_cols = [
        'Year', 'Quarter', 'Hour', 'Month', 'IsWeekend',
        'DayOfWeekEnc', 'TimePeriodEnc', 'StreetFreqEnc', 'ViolationDescEnc'
    ]
    # Ensure dtypes are numeric
    encoded_df = cleaned_data[encoded_cols].copy()
    encoded_df = encoded_df.apply(pd.to_numeric, errors='coerce')

    encoded_output_file = "DATA/Final/encoded_parking_tickets.csv"
    encoded_df.to_csv(encoded_output_file, index=False, encoding='utf-8')
    print(f"Encoded numeric features saved to: {encoded_output_file}")

    # Keep a preview of most anomalous-ready rows (smallest StreetFreqEnc for rarity cue)
    preview_cols = ['IssuedDate', 'StreetName', 'ViolationDescription', 'StreetFreqEnc']
    print("\nPreview of encoded data (rarest streets first):")
    print(cleaned_data.sort_values('StreetFreqEnc', ascending=True)[preview_cols].head(5))
    
    print("Data cleaning completed successfully!")
    print(f"Cleaned data saved to: {output_file}")
    
    print("\nSample of cleaned data:")
    print(cleaned_data.head()[[
        'IssuedDate','Year','DayOfWeek','DayOfWeekEnc','Quarter','StreetName','StreetFreqEnc',
        'TimePeriod','TimePeriodEnc','ViolationDescription','Hour','Month','IsWeekend'
    ]])
    
    return cleaned_data

if __name__ == "__main__":
    clean_parking_data()
