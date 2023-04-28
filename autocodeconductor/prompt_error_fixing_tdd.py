1.
Previously you have written this file

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


Could you please update the tests, provide the whole test implementation in one copiable code block 
Please follow the PEP8 best practice for writting pytest. Please also have full test coverage according 
to the requirement. Please validate whether the current implementation fullfils each test
. If no, please provide the fix as well, and give the reason why.