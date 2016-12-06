"""
    authors: Steve Valenti, Jacob Hooker
    date: 12.05.16
    vers: 1.9
    py: python 3.5.2
"""
from fmdconf import load_config, update_config, cmd_branch
import subprocess
import psutil
import os

# returns dictionary containing watched directories and files
def monitor_loop():
    while(True):
        global watched
        try:
            watched = load_config()
            watched['default'] = ['autopsy64.exe','autopsy32.exe']
        except:
            # debug log that no config file detected
            print("No config file detected, creating one now...")
            cmd_branch()
            monitor_loop()
        processes = []
        for p in psutil.process_iter():
            try:
                if p.name().lower() in watched['exe']:
                    processes.append(p)
                elif p.name() in watched['exe']:
                    processes.append(p)
                elif p.name().lower() in watched['default']:
                    processes.append(p)
                elif p.name() in watched['default']:
                    processes.append(p)
            except psutil.Error:
                pass

        # if forensic tool is detected
        if len(processes) > 0:
            watched = load_config()
            file_remove = set([])
            dir_remove = set([])
            for filename in watched['files']:
                filename.strip()
                subprocess.check_call("cipher /a /f /i /e " + filename, shell=True)
                subprocess.check_call("del /f /q " + filename, shell=True)
                file_remove.add(filename)
            for directory in watched['dirs']:
                directory.strip()
                subprocess.check_call("cipher /f /i /e " + directory, shell=True)
                subprocess.check_call("rmdir /s /q " + directory, shell=True)
                dir_remove.add(directory)
            for element in file_remove:
                watched['files'].remove(element)
                update_config(element)
            for element in dir_remove:
                watched['dirs'].remove(element)
                update_config(element)
            processes = 0
            watched = load_config()
            subprocess.check_call("cipher /w:C:\ ", shell=True)

        if len(watched['files']) + len(watched['dirs']) == 0:
            exit()

if __name__ == '__main__':
    monitor_loop()
