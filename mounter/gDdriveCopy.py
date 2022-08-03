#!/usr/bin/python3
import sys 
import os
import signal

def mount(): 
    value = os.system("rclone mount gDrive: ~/drive/ &")
    print(value)

def unmount():
    try:
         
        # iterating through each instance of the process
        for line in os.popen("ps ax | grep rclone | grep -v grep"):
            fields = line.split()
                
            # extracting Process ID from the output
            pid = fields[0] 
                
            # terminating process
            os.kill(int(pid), signal.SIGINT)
        print("Process Successfully terminated")
         
    except:
        print("Error Encountered while running script")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: mounter.py [mount|unmount]")
        exit(1)

    if sys.argv[1] == "mount":
        mount()
    elif sys.argv[1] == "unmount":
        unmount()
    else: 
        print("Usage: mounter.py [mount|unmount]")
        exit(1)



