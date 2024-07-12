import time
import re
from rich.console import Console

console = Console()

def print_tf(*texts, delay=0.05):
    for text in texts:
        if isinstance(text, list):
            text = "\n".join(text)
        
        text = str(text)
        
        typing_index = 0
        
        while typing_index < len(text):
            match_pause = re.match(r'\{pause:(\d+(\.\d+)?)\}', text[typing_index:])
            if match_pause:
                pause_duration = float(match_pause.group(1))
                time.sleep(pause_duration)
                typing_index += match_pause.end()
            else:
                console.print(text[typing_index], end='', markup=True)
                time.sleep(delay)
                typing_index += 1
        
        console.print()  # Move to the next line after printing the text