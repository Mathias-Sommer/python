import re
import time
import pyperclip
import keyboard
import random

puzzle_string = ""
run_script_bind = 'f5'

def on_keypress(event):
    if event.name == run_script_bind:
        puzzle_solver()

def puzzle_solver():
    global puzzle_string, direction
    move_counter = 0
    time_check = 0
    time_check_stop = 0
    time_check_calc = 0

    clipboard_content = pyperclip.paste()
    formatted_string = re.sub(r'(left|right|up|down)', r'\1 ', clipboard_content)
    directions = re.findall(r'(left|right|up|down)', formatted_string)
    puzzle_string += f"\n\n{clipboard_content}\n\n"

    time.sleep(0.2)
    time_check = time.time()
    for direction in directions:        
        move_counter += 1

        if direction == 'left':
            key = 'left'
        elif direction == 'right':
            key = 'right'
        elif direction == 'up':
            key = 'up'
        elif direction == 'down':
            key = 'down'        

        time.sleep(random.uniform(0.0693, 0.15)) #0.0487, 0.0845
        keyboard.press(key)
        
        time.sleep(random.uniform(0.0693, 0.15)) #0.0487, 0.0845
        keyboard.release(key)

    time_check_stop = time.time() 
    time_check_calc = time_check_stop - time_check
   
		#removed movecounter from the print
    print(f"Puzzle solved in {round(time_check_calc, 2)} seconds!")
    clipboard_content = pyperclip.copy('')

print("Puzzle Solver v1.0 | Made by Thiesen")
print("Select everything from ALT1 arrowkey guide: CTRL + A.")
print("Copy ALT1 arrowkey guide: CTRL + C.")
print("Right-click anywhere on Runescape client and press F5 to solve puzzle!")
keyboard.on_press_key(run_script_bind, on_keypress)

keyboard.wait('F8')
