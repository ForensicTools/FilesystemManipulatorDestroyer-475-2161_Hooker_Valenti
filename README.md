Windows Filesystem Manipulator & Destroyer
==========================================


**Authors:** Steven Valenti, Jacob Hooker
**Version:** 2.0
**Date:**    12.15.2016


## Overview:

An anti-forensics tool intended to detect attempts to analyze certain files or filesystems
and act by disrupting data collection. This tool is meant to monitor and destroy predetermined
files that are deemed sensitive.

The goal will to be to provide a lightweight service that can run in the background or be armed
at the users request. It will monitor for use of tools such as sleuthkit, ftk or command line
hashing functions and respond by removing sensitive material in preconfigured file locations.

## Files:

- fmdConfig.py - called directly to add files/directories to the watchlist
- fmder.py - ran as an executable to perform actions on watched files and directories
- fmd.conf - required configuration file, can be created by running fmdConfig.py
- fmder.exe - tool packaged into Windows executable

## Requires:

- from threading import Timer
- from fmdConfig import *
- import sys
- import subprocess
- import psutil
- import time

## User guide

fmder is now packaged as an executable. To run it a fmd.conf file must first be created in the same
directory as fmder.exe. To create it run the included fmdConfig.py as so:

`python fmdConfig.py`

Directories and files added there will be deleted if a default executable (Autopsy/FTK) or
a user-specified executable is detected. If a directory to monitor by timed interval is added
then the contents of that directory will be wiped after a user-specified amount of time. This
process will repeat until the program exits which by default is only triggered by a blacklisted
executable being ran.

## TODO:

- improve stability
- increase number of watched executables in windows
