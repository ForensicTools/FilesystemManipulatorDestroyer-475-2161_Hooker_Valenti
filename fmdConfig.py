"""
    authors: Steve Valenti, Jacob Hooker
    date: 12.15.16
    vers: 1.5
    py: python 3.5.2

    Script to create a FMDer config file and pass it to the main
    function.
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

def load_perm_watched():

    pwatched = {'golden':set([]),
                'timer':set([]),
                'loop':set([])}

    with open('fmd.conf','r') as config:
        for line in config:
            if "golden" in line:
                new_golden = line.split(' ')
                pwatched['golden'].add(new_golden[1].strip())
            elif "timer" in line:
                new_timer = line.split(' ')
                pwatched['timer'].add(new_timer[1].strip())
            else:
                pass
    config.close()

    return pwatched

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
        Adds a directory to watch to the config file.
    """
    print("Warning: Directories added here will be deleted if processes detected.")
    print("Type 1 to return to menu")
    new_dir = input("Enter complete path of directory to watch: ")

    if new_dir is '1':
        return

    with open('fmd.conf','a') as config:
        config.write("directory: " + new_dir + '\n')
    config.close()

    return

def add_golden():
    """
        Adds a directory to permanent watch to the config file.
    """
    print("Warning: Directories added here will be monitored while program is running.")
    print("Contents will be deleted in user-specified intervals.")
    print("The directory structure will be preserved.")
    new_dir = input("Enter path of directory to watch all sub-files of: ")
    timeout = input("Enter interval (minutes) to wipe directory contents: ")

    with open('fmd.conf','a') as config:
        config.write("golden: " + new_dir + '\n')
        config.write("timer: " + timeout + '\n')
    config.close()

    return

def add_file():
    """
        Adds a file to watch to the config file.
    """
    print("Warning: Files added here will be deleted if processes detected.")
    print("Type 1 to return to menu")
    new_file = input("Enter path of file to watch: ")

    if new_file is '1':
        return

    with open('fmd.conf','a') as config:
        config.write("file: " + new_file + '\n')
    config.close()

    return

def cmd_branch(sw):
    """
        Navigation for adding entries to config file
    """
    while(True):
        print("\n---------- Config File Creator ----------")
        print("1. Add a directory to watch")
        print("2. Add a file to watch")
        print("3. Add an executable to blacklist")
        print("4. Add a folder tree to monitor (timed intervals)")
        if sw is not 1:
            print("5. Run program")
        print("6. Terminate program")

        try:
            case = int(input("Enter choice: "))
        except:
            case = 10
        if case == 1:
            add_dir()
        elif case == 2:
            add_file()
        elif case == 3:
            add_exe()
        elif case == 4:
            add_golden()
        elif case == 5:
            return
        elif case == 6:
            print("Goodbye")
            exit()
        else:
            print("\nInvalid option, please enter a number 1-4")

if __name__ == '__main__':
    cmd_branch(1)
