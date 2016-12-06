"""
    authors: Steve Valenti, Jacob Hooker
    date: 12.05.16
    vers: 1.5
    py: python 3.5.2

"""

def load_config():
    """
        Loads the config file setting the directories to watch.
    """
    watched = {'dirs':set([]),
               'files':set([]),
               'exe':set([])}

    with open('fmd.conf','r') as config:
        for line in config:
            line.lower()
            if "directory" in line:
                new_dir = line.split(' ')
                watched['dirs'].add(new_dir[1].strip())
            elif "file" in line:
                new_file = line.split(' ')
                watched['files'].add(new_file[1].strip())
            elif "exe" in line:
                new_exe = line.split(' ')
                watched['exe'].add(new_exe[1].strip())
            else:
                pass
    config.close()

    return watched

def update_config(del_line):
    """
        Removes config entries when they are actioned upon by the
        main script
    """
    with open('fmd.conf','r') as config:
        lines = []
        for line in config:
            lines.append(line)
    config.close()
    with open('fmd.conf','w') as config:
        for line in lines:
            if del_line not in line:
                config.write(line)
            else:
                pass
    config.close()

    return load_config()

def add_exe():
    """
        Adds an executable to blacklist
    """
    new_exe = input("Enter name of executable to blacklist: \nExample: tool.exe\n")
    with open('fmd.conf','a') as config:
        config.write("exe: " + new_exe + '\n')
        config.close()

def add_dir():
    """
        TODO: add error checking/input validation

        Adds a directory to watch to the config file.
    """
    new_dir = input("Enter path of directory to watch: ")

    with open('fmd.conf','a') as config:
        config.write("directory: " + new_dir + '\n')
    config.close()

def add_file():
    """
        TODO: add error checking/input validation

        Adds a file to watch to the config file.
    """
    new_file = input("Enter path of file to watch: ")

    with open('fmd.conf','a') as config:
        config.write("file: " + new_file + '\n')
    config.close()

def cmd_branch():
    while(True):
        print("\n---------- Config File Creator ----------")
        print("1. Add a directory to watch")
        print("2. Add a file to watch")
        print("3. Add an executable to blacklist")
        print("4. Run program")
        print("5. Terminate program")

        try:
            case = int(input("Enter choice: "))
        except:
            case = 4
        if case == 1:
            add_dir()
        elif case == 2:
            add_file()
        elif case == 3:
            add_exe()
        elif case == 4:
            return
        elif case == 5:
            print("Goodbye")
            exit()
        else:
            print("\nInvalid option, please enter a number 1-4")

if __name__ == '__main__':
    cmd_branch()
