import psutil
import time

def monitor_system():

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    print("System Metrics")
    print("CPU Usage:", cpu, "%")
    print("Memory Usage:", memory, "%")
    print("Disk Usage:", disk, "%")

    if cpu > 80:
        print("⚠ High CPU usage detected")

    if memory > 80:
        print("⚠ High memory usage detected")

    if disk > 90:
        print("⚠ Disk nearly full")

while True:

    monitor_system()

    print("---------------------")

    time.sleep(10)