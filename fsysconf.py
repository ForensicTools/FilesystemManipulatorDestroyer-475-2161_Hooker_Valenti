"""
    authors: Steve Valenti, Jacob Hooker
    date: 11.07.16
    vers: 1.0
    py: python 3.5.2

"""

def load_config():
    """
        TODO: test line parsing

        Loads the config file setting the directories to watch.
    """
    watched = {'dirs':set([]),
             'files':set([])}

    with open('fsysconfig.txt','r') as config:
        for line.lower() in config:
            if "directory" in line:
                new_dir = line.split(' ')
                watched['dirs'].append(new_dir[1])
            elif "file" in line:
                new_file = line.split(' ')
                watched['files'].append(new_line[1])
    config.closed()
    
    return watched

def add_dir():
    """
        TODO: add error checking/input validation

        Adds a directory to watch to the config file.
    """
    new_dir = input("Enter path of directory to watch: ")

    with open('fsysconfig.txt','a') as config:
        config.write("directory: " + new_dir)
    config.closed()
    load_config()

def add_file():
    """
        TODO: add error checking/input validation

        Adds a file to watch to the config file.
    """
    new_file = input("Enter path of file to watch: ")

    with open('fsysconfig.txt','a') as config:
        config.write("file: " + new_file)
    config.closed()
    load_config()

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
            add_dir()
        elif case == 2:
            add_file()
        elif case == 3:
            print("Goodbye")
            exit()
        else:
            print("\nInvalid option, please enter a number 1-3")
