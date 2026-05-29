import psutil
import time
from datetime import datetime

# Threshold values
CPU_LIMIT = 80
MEMORY_LIMIT = 80
DISK_LIMIT = 80


def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


def get_memory_usage():
    return psutil.virtual_memory().percent


def get_disk_usage():
    return psutil.disk_usage('/').percent


def show_alert(message):
    print(f"ALERT: {message}")


def display_system_status():
    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disk = get_disk_usage()

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n==============================")
    print(f"Time: {current_time}")
    print("==============================")
    print(f"CPU Usage    : {cpu}%")
    print(f"Memory Usage : {memory}%")
    print(f"Disk Usage   : {disk}%")

    # Check limits
    if cpu > CPU_LIMIT:
        show_alert(f"High CPU Usage ({cpu}%)")

    if memory > MEMORY_LIMIT:
        show_alert(f"High Memory Usage ({memory}%)")

    if disk > DISK_LIMIT:
        show_alert(f"High Disk Usage ({disk}%)")


def main():
    print("System Health Monitor Started...")
    print("Press CTRL + C to stop")

    while True:
        display_system_status()

        # Wait 5 seconds
        time.sleep(5)


if __name__ == "__main__":
    main()
