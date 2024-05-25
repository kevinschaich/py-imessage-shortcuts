from subprocess import Popen, run
import json
import os

TEMP_FILE_NAME = 'temp_py_imessage_shortcuts.json'
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMP_FILE_PATH = os.path.join(REPOSITORY_ROOT_DIR, TEMP_FILE_NAME)

SHORTCUT_NAME = 'send-imessage'

def _dump_file(recipients: list[str], message: str) -> None:
    with open(TEMP_FILE_PATH, 'w') as f:
        message_details = {
            'recipients': recipients, 
            'message': message
            }
        json.dump(message_details, f)

def send_image(recipients: list[str], message: str | None, image_path: str) -> None:
    """enables an image to be sent from an absolute file path

    Args:
        recipients (list[str]): The phone numbers to address the iMessage to
        message (str | None): the message to send with the photo, if no message should be included, pass None
        image_path (str): file path to image, must be absolute
    """
    if len(message) == 0:
        message = None
    _dump_file(recipients, message)

    Popen([
        'shortcuts',
        'run',
        SHORTCUT_NAME,
        '--input-path',
        TEMP_FILE_PATH,
        '--input-path',
        image_path,
    ])

def check_shortcut_exists(shortcut_name:str = SHORTCUT_NAME) -> bool:
    """ Validates that the shortcut exists
    Args:
        shortcut_name (str) :   an optional parameter that specifies which shortcut
                                to look for

    Returns:
        bool: True if shortcut_name exists in shortcuts, False if not. 
    """
    result = run(["shortcuts", "list"], capture_output=True, text=True)
    
    if result.returncode != 0:
        return False
    
    shortcut_list = result.stdout.splitlines()
    
    return shortcut_name in shortcut_list


def send(recipients: list[str], message: str) -> None:
    # Write message details to temp file (Shortcuts via command line only accepts files as inputs)
    _dump_file(recipients, message)

    # Run the shortcut
    Popen([
        'shortcuts',
        'run',
        SHORTCUT_NAME,
        '--input-path',
        TEMP_FILE_PATH,
    ])
