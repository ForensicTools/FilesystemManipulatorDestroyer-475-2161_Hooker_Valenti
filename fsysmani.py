"""
    authors: Steve Valenti, Jacob Hooker
    date: 10.21.16
    vers: 1.0
    py: python 3.5.2
"""

def load_config():
    """
        Loads the config file setting the directories to watch.
    """
    return

def add_dir():
    """
        Adds a directory to watch to the config file.
    """
    return

def add_file():
    """
        Adds a file to watch to the config file.
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

if __name__ == '__main__':
    while(True):
        print("\nWhat would you like to do?")
        print("1. Add a directory to watch")
        print("2. Add a file to watch")
        print("3. Exit")

        try:
            case = int(input("Enter choice: "))
        except:
            case = 4
        if case == 1:
        elif case == 2:
        elif case == 3:
            print("Goodbye")
            exit()
        else:
            print("\nInvalid option, please enter a number 1-3")
