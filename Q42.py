import datetime

# 1. Open a file in append mode "log.txt"
with open("log.txt", "a") as file:
    # Adding a timestamp makes the log entry look more realistic (optional, but good practice)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 2. Add a new log entry
    file.write(f"[{current_time}] Program run successfully\n")

print("--- Current Log File Contents ---")

# 3. Open the file in read mode and print all logs
with open("log.txt", "r") as file:
    log_content = file.read()
    # Using strip() to remove any trailing empty lines when printing
    print(log_content.strip())