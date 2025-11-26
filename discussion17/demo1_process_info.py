import os
import psutil

def get_process_info():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    cpu_times = process.cpu_times()
    
    info = {
        'Memory Info': {
            'RSS': mem_info.rss, # Resident Set Size
            'VMS': mem_info.vms, # Virtual Memory Size
        },
        'CPU Times': {
            'User Time': cpu_times.user, # user tasks
            'System Time': cpu_times.system, # kernel tasks
        },
        'Process Info': {
            'PID': process.pid,
            'Name': process.name(),
            'Status': process.status()
        }
    }
    
    return info

if __name__ == "__main__":
    info = get_process_info()
    for category, details in info.items():
        print(f"{category}:")
        for key, value in details.items():
            print(f"  {key}: {value}")