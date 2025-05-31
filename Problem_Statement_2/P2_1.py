import psutil

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 90
cpu = psutil.cpu_percent(interval=1)
mem = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

if cpu > CPU_THRESHOLD:
    print(f"Warning: CPU usage is high ({cpu}%)")

elif mem > MEMORY_THRESHOLD:
    print(f"Warning: Memory usage is high ({mem}%)")
elif disk > DISK_THRESHOLD:
    print(f"Warning: Disk usage is high ({disk}%)")
else:
    print(f"Your System is Functioning Normal:\nCPU Usage: {cpu}%  \nMemory Usage: {mem}% \nDisk Usage: {disk}%")


