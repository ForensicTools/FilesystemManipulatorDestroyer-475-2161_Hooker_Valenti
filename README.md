Windows Filesystem Manipulator & Destroyer
==========================================


**Authors:** Steven Valenti, Jacob Hooker
**Version:** 1.0
**Date:**    10.11.2016


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

## TODO:

- add file removing/shredding support for systemd devices
- increase number of watched executables in windows
- set a flag to differentiate between operating systems
