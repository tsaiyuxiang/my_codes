# working.py
# input
# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# 9:00 AM to 5 PM
# 9 AM to 5:00 PM
# output  09:00 to 17:00
# Raise a ValueError instead if the input to convert is not in either of
#   those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.).

import re

def main():
    print(convert(input("Hours: ")))

def convert(s):

    #
    # ^   string 開頭
    # (\d{1,2})  # 第一個時間的「小時」部分，例如 9 或 12
    # (?::(\d{2}))?  # （可選）分鐘，例如 :00。會擷取 00，也可以省略
    # \s*  # 小時與 AM/PM 之間允許有空白 (\s為空白如 space, tab) (*表示前面可以 0 ~ 多個 空白)
    # (AM|PM)  # 上午或下午（區分大小寫由 re.IGNORECASE 處理）
    # \s+to\s+  # " to " 中間必須有空格（+表示可以是一個或多個）
    # (\d{1,2})  # 第二個時間的「小時」
    # (?::(\d{2}))?  # 第二個時間的分鐘（可選）
    # \s*  # 小時與 AM/PM 之間允許空白
    # (AM|PM)  # 第二個時間的 AM 或 PM
    # $   string 尾巴
    # 下方 CS50P 無法通過  9AM 不行 , 9 AM 才可
    #pattern = r'^(\d{1,2})(?::(\d{2}))?\s*(AM|PM)\s+to\s+(\d{1,2})(?::(\d{2}))?\s*(AM|PM)$'
    # 改成以下才可
    pattern = r'^(\d{1,2})(?::(\d{2}))?\s+(AM|PM)\s+to\s+(\d{1,2})(?::(\d{2}))?\s+(AM|PM)$'
    #pattern = r'^(\d{1,2})(?::(\d{2}))?\s{1}(AM|PM)\s+to\s+(\d{1,2})(?::(\d{2}))?\s{1}(AM|PM)$'
    #attern = r'^(\d{1,2})(?::(\d{2}))?\s{1}(AM|PM)\s{1}to\s{1}(\d{1,2})(?::(\d{2}))?\s{1}(AM|PM)$'
    match = re.match(pattern, s, re.IGNORECASE)

    if not match:
        raise ValueError("Invalid format")

    h1, m1, p1, h2, m2, p2 = match.groups()

    h1 = int(h1)
    m1 = int(m1) if m1 else 0
    h2 = int(h2)
    m2 = int(m2) if m2 else 0

    if not (1 <= h1 <= 12) or not (0 <= m1 < 60):
        raise ValueError("Invalid start time")
    if not (1 <= h2 <= 12) or not (0 <= m2 < 60):
        raise ValueError("Invalid end time")

    def to_24_hour(hour, minute, period):
        if period.upper() == "AM":
            if hour == 12:
                hour = 0
            pass
        elif period.upper() == "PM":
            if hour != 12:
                hour += 12
        return f"{hour:02}:{minute:02}"

    start = to_24_hour(h1, m1, p1)
    end = to_24_hour(h2, m2, p2)

    return f"{start} to {end}"

if __name__ == "__main__":
    main()
