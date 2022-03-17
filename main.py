# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

import platform

current_os = platform.system()
print(f'{current_os=}')

commands = {
  'ping': 'ping',
  'traceroute': 'tracert' if current_os == 'Windows' else 'traceroute',
  'nslookup': 'nslookup'
}

# Modify the do_command function:
#   to use the new button as needed
def do_command(command):
    # Modify the do_command(command) function: 
    #   to use the text box for input to the functions
    global command_textbox, url_entry

    # If url_entry is blank, use localhost IP address 
    url_val = url_entry.get()
    if (len(url_val) == 0):
        # url_val = "127.0.0.1"
        url_val = "::1"
    
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    p = subprocess.Popen(command + ' ' + url_val, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #v2

    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# set up button to run the do_command function
ping_btn = tk.Button(frame, text="PING", command=lambda:do_command(commands['ping']))
ping_btn.pack()

tracert_btn = tk.Button(frame, text="TRACE ROUTE", command=lambda:do_command(commands['traceroute']))
tracert_btn.pack()

# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10,  bg="black") # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center",
    font=("comic sans", 14),
    bd=0, 
    relief=tk.FLAT, 
    cursor="heart",
    fg="mediumpurple3",
    bg="black")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("comic sans", 14)) # change font
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root,  bg="black") # change frame color
frame.pack()


# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()

root.mainloop()
