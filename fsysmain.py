"""
    authors: Steve Valenti, Jacob Hooker
    date: 11.07.16
    vers: 1.4
    py: python 3.5.2

    TODO: create as service
"""
from fsysconf import load_config

def logger():
    """
       Logs actions taken by script
    """

def detect_hashing():
    """
        Montiors for use of hash functions from the command line.
    """
    return

def detect_sleuthkit():
    """
        Monitors for loading of the sleuthkit.
    """

def detect_ftk():
    """
        Montiors for use of ftk tools.
    """

# returns dictionary containing watched directories and files
watched = fsysconf.load_config()
