import time

log_file = "system.log"

def monitor_logs():
    with open(log_file, "r") as f:
        lines = f.readlines()

    for line in lines:
        if "ERROR" in line:
            print("Alert: error detected")
            print(line)

while True:
    monitor_logs()
    time.sleep(10)