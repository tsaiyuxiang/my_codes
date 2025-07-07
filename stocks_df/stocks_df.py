# stocks_df.py
# 蔡宇翔 2025/7/7 交的作業
# colab link  https://colab.research.google.com/drive/1vf3dn7kRfWZONTq9OB1hjWlZWb8N7ZP5?usp=sharing

import pandas as pd
import requests
from io import StringIO
from datetime import datetime, timedelta

# --- Step 1: Generate date list ---
start_date = datetime(2025, 6, 30)
end_date = datetime(2025, 7, 4)
dates = [(start_date + timedelta(days=i)).strftime("%Y%m%d") for i in range((end_date - start_date).days + 1)]

# --- Step 2: Prepare placeholders ---
all_dfs = []
row_counts = {}

# --- Step 3: Loop through each date ---
for date in dates:
    print(f"📅 Fetching data for {date}...")
    url = f"https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date={date}&type=ALL&response=csv"

    try:
        response = requests.get(url)
        response.encoding = 'big5'  # TWSE uses Big5 for Traditional Chinese

        lines = response.text.splitlines()

        # Locate the start of "每日收盤行情(全部)"
        start_index = None
        for i, line in enumerate(lines):
            if "每日收盤行情(全部)" in line:
                start_index = i
                break

        if start_index is None:
            print(f"⚠️  No '每日收盤行情(全部)' section for {date}. Skipping.")
            continue

        # Extract data lines below the section header (skip 2 lines: title and unit row)
        table_lines = []
        for line in lines[start_index + 2:]:
            if not line.strip():
                break
            table_lines.append(line)

        # Convert to CSV and read into DataFrame
        csv_str = "\n".join(table_lines)
        df = pd.read_csv(StringIO(csv_str))
        df.columns = df.columns.str.strip().str.replace('"', '')
        df['日期'] = date  # Add date column

        all_dfs.append(df)
        row_counts[date] = len(df)

    except Exception as e:
        print(f"❌ Error processing {date}: {e}")
        continue

# --- Step 4: Combine all DataFrames ---
if all_dfs:
    combined_df = pd.concat(all_dfs, ignore_index=True)

    # Save to CSV
    combined_df.to_csv("twse_5days.csv", index=False, encoding="utf-8-sig")
    print("\n✅ Data saved to 'twse_5days.csv'")

    # --- Step 5: Report row counts ---
    print("\n📊 Number of rows (stocks) per day:")
    for date, count in row_counts.items():
        print(f"{date}: {count} rows")

    total_rows = sum(row_counts.values())
    print(f"\n🧮 Total rows over 5 days: {total_rows}")

    # --- Step 6: Show first 50 rows ---
    print("\n🔎 First 50 rows of combined DataFrame:")
    print(combined_df.head(50))
else:
    print("\n⚠️ No data collected. Please check the date range or network.")
