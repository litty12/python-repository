from datetime import datetime
current_time = datetime.now()
print(current_time)
format_1=current_time.strftime("%Y-%m-%d %H:%M:%S")
print(format_1)
format_2=current_time.strftime("%m/%d/%Y")
print(format_2)
format_3=current_time.strftime("%d,%m")