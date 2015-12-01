# task 15

import platform
import subprocess

# Step 1
windows = True if platform.system() == 'Windows' else False

'''
This is an inline if statement if you write it in multiple lines it would look
like this:

windows = None
if platform.system() == 'Windows':
    windows = True
else:
    windows = False
'''

# Step 2

command = ''

if windows:
    command = 'dir'
else:
    command = ['ls', '-lha']

'''
Again this could be done in a single line:

command = 'dir' if windows else ['ls', '-lha']
'''

subprocess.run(command)

# Step 3

from time import sleep

sleep(5)

clear = 'cls' if windows else 'clear'

subprocess.run(clear)
