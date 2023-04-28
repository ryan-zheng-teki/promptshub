1. 
Given src/communication/input_message_handler.py

import asyncio
import sys
from colorama import Fore, Style, init
import pyperclip

def get_input_message():
    print(Fore.GREEN + "INPUT: Start typing your message (press Enter to send):" + Style.RESET_ALL)
    message_lines = []
    while True:
        line = sys.stdin.readline().rstrip()
        if not line:
            break
        message_lines.append(line)
    message = "\n".join(message_lines)
    return message


async def wait_for_clipboard_content(current_clipboard):
    while True:
        await asyncio.sleep(0.1)
        new_clipboard = pyperclip.paste()
        if new_clipboard != current_clipboard:
            return new_clipboard

run comand: pytest -k src/communication/input_message_handler.py

error: 


Could you please update the tests, provide the whole test implementation in one copiable code block 
Please follow the PEP8 best practice for writting pytest. Please also have full test coverage according 
to the requirement. Please validate whether the current implementation fullfils each test
. If no, please provide the fix as well, and give the reason why.

Prompt: fix tests prompts
Given  src/communication/input_message_handler.py  
def _on_key_release_single_char(key):
    """
    Handles key releases in single character input mode.

    Args:
        key: The key released by the user.
    """
    global _user_confirmation_char

    if isinstance(key, pynput.keyboard.KeyCode):
        char = key.char.lower()
        _user_confirmation_char = char
        return False
    
current behavior: When i hit  y, and release y, then the logic immediately continues
additional requriement: After release y, the user should also hit enter, then to logic continues 
propose changes and give reason to validate your changes against the requirement.
hint: Please check previous conversation about similar code implementations
Output: the complete modified code in a single copiable code block, so i can copy and paste. 
