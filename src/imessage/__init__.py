from subprocess import Popen
import json
import os


TEMP_FILE_NAME = 'temp_py_imessage_shortcuts.json'
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMP_FILE_PATH = os.path.join(REPOSITORY_ROOT_DIR, TEMP_FILE_NAME)


def send(recipients, message):

    # Write message details to temp file (Shortcuts via command line only accepts files as inputs)
    with open(TEMP_FILE_PATH, 'w') as f:
        message_details = {'recipients': recipients, 'message': message}
        json.dump(message_details, f)

    # Run the shortcut
    Popen([
        'shortcuts',
        'run',
        'send-imessage',
        '--input-path',
        TEMP_FILE_PATH,
    ])
