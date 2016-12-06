Windows Filesystem Manipulator & Destroyer
==========================================


**Authors:** Steven Valenti, Jacob Hooker
**Version:** 1.9
**Date:**    12.05.2016


## Overview:

An antiforensics tool intended to detect attempts to analyze certain files or filesystems
and act by disrupting data collection. This tool is meant to monitor and destroy predetermined
files that are deemed sensitive.

The goal will to be to provide a lightweight service that can run in the background or be armed
at the users request. It will monitor for use of tooks such as sleuthkit, ftk or command line
hashing functions and respond by removing sensitive material in preconfigured file locations.

## Files:

- fsyconf.py - called directly to add files/directories to the watchlist
- fsysmain.py - ran as a service to perform actions on watched files and directories
- fsysmain.service - systemd file for daemonizing on systemd enabled OS

## Requires:

- from fmdconf import load_config, update_config, cmd_branch
- import subprocess
- import psutil
- import os

## User guide


## TODO:

- increase number of watched executables in windows
- write guide
