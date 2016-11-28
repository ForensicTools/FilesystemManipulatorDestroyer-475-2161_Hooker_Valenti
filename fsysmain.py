"""
    authors: Steve Valenti, Jacob Hooker
    date: 11.17.16
    vers: 1.5.1
    py: python 3.5.2
"""
from fsysconf import load_config
import logging
import psutil
import os

# returns dictionary containing watched directories and files
while(True):
    watched = fsysconf.load_config()
    processes = []
        for p in psutil.process_iter():
            try:
                if p.name() == 'autopsy64.exe':
                    pythons_psutil.append(p)
                if p.name() == 'autopsy32.exe':
                    processes.append(p)
            except psutil.Error:
                pass

    # if forensic tool is detected
    if len(processes) > 1:
        update_watched = fsysconf.load_config()
        for e in watched['files']:
            # do something to file/directory
            finfo = os.stat(e)
            with open(e,'w') as f:
                for i in range(0,finfo.st_size):
                    f.write(0)
                    f.close
                    watched['files'].remove(e)
