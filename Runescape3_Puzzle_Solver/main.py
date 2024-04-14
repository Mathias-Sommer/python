import re
import time
import pyperclip
import keyboard
import random
import tkinter as tk

puzzle_string = ""
run_script_bind = 'f5'
value = 25  # Default value
form_open = False

def create_speed_selector():
    global value, form_open
    root = tk.Tk()
    root.title("Select Speed")
    root.geometry("160x130")
    root.resizable(False, False)
    window_width = root.winfo_reqwidth()
    window_height = root.winfo_reqheight()
    position_right = int(root.winfo_screenwidth()/2 - window_width/2)
    position_down = int(root.winfo_screenheight()/2 - window_height/2)
    root.geometry("+{}+{}".format(position_right, position_down))

    def save_value():
        global value, form_open
        value = slider.get()
        print(f"Speed: {value}")
        root.destroy()
        form_open = False 

    frame = tk.Frame(root)
    frame.pack(pady=10)

    label = tk.Label(frame, text="The higher the slower it gets")
    label.pack()

    slider = tk.Scale(frame, from_=1, to=100, orient="horizontal")
    slider.set(value)
    slider.pack()

    save_button = tk.Button(frame, text="Save", command=save_value)
    save_button.pack(pady=10)

    root.mainloop()

def toggle_speed_selector():
    global form_open
    if form_open:
        keyboard.remove_hotkey('f5')
        form_open = False
        print("Speed selector closed")
    else:
        keyboard.add_hotkey('f5', create_speed_selector)
        form_open = True
        print("Speed selector opened")

def on_keypress(event):
    global form_open
    if event.name == run_script_bind and not form_open:
        puzzle_solver()

def puzzle_solver():
    global puzzle_string, value
    move_counter = 0
    time_check = 0
    time_check_stop = 0
    time_check_calc = 0
    print("Solving puzzle ...")

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
            #print("Left")
        elif direction == 'right':
            key = 'right'
            #print("Right")
        elif direction == 'up':
            key = 'up'
            #print("Up")
        elif direction == 'down':
            key = 'down'      
            #print("Down") 

        multiplier = 1 / value
        mathValue = random.uniform(0.005, 0.010) / multiplier
        #print(round(mathValue,2))
        time.sleep(mathValue)
        keyboard.press(key)

        mathValue = random.uniform(0.005, 0.010) / multiplier
        #print(round(mathValue,2))        
        time.sleep(mathValue)
        keyboard.release(key)

    time_check_stop = time.time() 
    time_check_calc = time_check_stop - time_check
    
    print(f"Puzzle solved in {move_counter} moves and {round(time_check_calc, 2)} seconds!")
    clipboard_content = pyperclip.copy('')

keyboard.add_hotkey('f6', toggle_speed_selector)
toggle_speed_selector()

keyboard.on_press_key(run_script_bind, on_keypress)

print(f"Puzzle Solver | Made by Thiesen")
print("Speed selector: F6 then F5")
print("Select everything from ALT1 arrowkey guide: CTRL + A.")
print("Copy ALT1 arrowkey guide: CTRL + C.")
print("Right-click anywhere on Runescape client and press F5 to solve puzzle!")
keyboard.wait('F12')
