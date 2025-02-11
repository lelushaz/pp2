import datetime

date1 = datetime.datetime(2024, 2, 10, 12, 0, 0)  
date2 = datetime.datetime(2025, 2, 18, 9, 30, 0)  
time_difference = date2 - date1

difference_in_seconds = time_difference.total_seconds()

print("Differnce in seconds: ", difference_in_seconds)