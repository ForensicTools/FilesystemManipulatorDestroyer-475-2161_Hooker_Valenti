"""
    authors: Steve Valenti, Jacob Hooker
    date: 12.15.16
    vers: 2.0
    py: python 3.5.2

    Loads config file of blacklisted directories, files
    and executables. Monitors processes with PSUtil and acts accordingly
    if one is running. If a perma watch directory is present it will
    maintain the directory structure and securely delete everything
    present on specified intervals.
"""
from threading import Timer
from fmdConfig import *
import sys
import subprocess
import psutil
import time

global loops
loops = 2

def monitor_loop():
    """
        Main loop

        Args:
            None

        Returns:
            None
    """
    global pwatched, loops

    pwatched = load_perm_watched()
    for e in pwatched['timer']:
        timeout = int(e)
    timeout = timeout * 60
    t = Timer(timeout, purge)
    t.start()

    while(True):
        try:
            watched = load_config()
            watched['default'] = ['autopsy64.exe','autopsy32.exe','ftk.exe','EnCase.exe','FTK Imager.exe']
        except:
            # only works if ran as a script, NOT for .exe
            # debug log that no config file detected
            print("No config file detected, creating one now...")
            cmd_branch(0)
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
                subprocess.check_output("cipher /a /f /i /e " + filename, shell=True, stderr=subprocess.STDOUT)
                subprocess.check_output("del /f /q " + filename, shell=True, stderr=subprocess.STDOUT)
                file_remove.add(filename)
            for directory in watched['dirs']:
                directory.strip()
                subprocess.check_output("cipher /f /i /e " + directory, shell=True, stderr=subprocess.STDOUT)
                subprocess.check_output("rmdir /s /q " + directory, shell=True, stderr=subprocess.STDOUT)
                dir_remove.add(directory)
            for element in file_remove:
                watched['files'].remove(element)
                update_config(element)
            for element in dir_remove:
                watched['dirs'].remove(element)
                update_config(element)
            processes = 0
            watched = load_config()

        if len(watched['files']) + len(watched['dirs']) == 0:
            #sys.exit(0)
            purge(1)

def purge(x=0):
    """
        Purges permanent folder if time limit is reached. Clears free space every
        2nd interval

        Args:
            None

        Returns:
            None
    """
    global loops
    loops = loops - 1

    for directory in pwatched['golden']:
        directory.strip()
        filename = directory + "\*.*"
        subprocess.check_output("cipher /a /f /i /e " + filename, shell=True)
        subprocess.check_output("del /f /q " + filename, shell=True)
    if loops <= 0:
        subprocess.check_output("cipher /w:C:\ ", shell=True)
        monitor_loop()
    if x == 1:
        subprocess.check_output("cipher /w:C:\ ", shell=True)
        sys.exit(0)
    else:
        monitor_loop()

if __name__ == '__main__':
    monitor_loop()
