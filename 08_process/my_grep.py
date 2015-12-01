# some snippets are from task 15

import platform
import subprocess
from time import sleep
import sys
import os

windows = True if platform.system() == 'Windows' else False


def main(argv):
    if not os.path.isdir(argv[1]):
        print('The given path does not exist.')
    else:
        command = 'dir' if windows else ['ls', '-lha', argv[1]]

        # .stdout liefert einen Byte-String, der auf UTF8 dekodiert werden muss
        directorycontent = subprocess.run(
            command, check=True, stdout=subprocess.PIPE).stdout.decode('utf8')

        searchstring = argv[2]
        # split the process output at the newline character
        directorycontent = directorycontent.split('\n')

        # search through your directory content, print every match
        for item in directorycontent:
            if searchstring in item:
                print(item)


if __name__ == '__main__':
    main(sys.argv)
