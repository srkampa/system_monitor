import os
import psutil
from psutil._common import bytes2human

def monitor_cpu():
    percentage = 0
    percentage = psutil.cpu_percent(percpu=False, interval= 1)
    print (percentage)

def monitor_memory():
    mem_total = None
    mem_used = None 
    mem_percent = None

    mem = psutil.virtual_memory()
    mem_total = mem.total
    mem_used = mem.used
    mem_percent = mem.percent
    print ("Memory Stat :: total : {} , used : {}, percent : {} ".format(mem_total, mem_used, mem_percent))

def monitor_network():
    net = psutil.net_io_counters()
    print net
    net2 = psutil.net_io_counters(pernic=True)
    print net2
    


    

if __name__ == "__main__":
    if not (psutil.WINDOWS or psutil.LINUX):
        raise Exception ("Your OS is not supported")
    while(True):
        monitor_cpu()
        monitor_memory()
        monitor_network()