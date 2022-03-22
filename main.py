# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

import platform

current_os = platform.system()

background='#189AB4'

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

    process = 'Working...'
    if command == 'ping':
      process = 'Pinging '
    elif command == 'tracert' or command == 'traceroute':
      process = 'Tracing route to '
    elif command == 'nslookup':
      process = 'Looking up '
    
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, process + (url_val + '...\n' if url_val != '::1' else 'localhost...\n'))
    command_textbox.update()

    p = subprocess.Popen(command + ' ' + url_val, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #v2

    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)

# Save function
def mSave():
  filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
  if filename is None:
    return
  file = open (filename, mode = 'w')
  text_to_save = command_textbox.get("1.0", tk.END)
  
  file.write(text_to_save)
  file.close()


root = tk.Tk()
root.title("INTERNET FAST - CHECK ANY WEBSITE!")
root.configure(background=background)

frame = tk.Frame(root)
frame.configure(background=background)
frame.pack()

title = tk.Label(frame, text='INTERNET FAST', font=('Times New Roman', 40), bg=background)
title.pack()

buttons = tk.Frame(frame)
buttons.configure(background=background)
buttons.pack()

# set up button to run the do_command function
ping_btn = tk.Button(buttons, text="PING", command=lambda:do_command(commands['ping']), height=5, width=15, font=("Times New Roman", 14), bg='#D4F1F4')
ping_btn.grid(row=0, column=0, sticky='N', padx=2)

tracert_btn = tk.Button(buttons, text="TRACE ROUTE", command=lambda:do_command(commands['traceroute']), height=5, width=15, font=("Times New Roman", 14), bg='#D4F1F4')
tracert_btn.grid(row=0, column=1, sticky='N', padx=2)

nslookup_btn = tk.Button(buttons, text="NSLOOKUP", command=lambda:do_command(commands['nslookup']), height=5, width=15, font=("Times New Roman", 14), bg='#D4F1F4')
nslookup_btn.grid(row=0, column=2, sticky='N', padx=2)

# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10, bg=background) # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL: ", 
    compound="center",
    font=("times new roman", 22),
    bd=0, 
    relief=tk.FLAT, 
    fg="black",
    bg=background)
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("Times New Roman", 22)) # change font
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root) # change frame color
frame.pack()

# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()

# creates the frame for save and clear buttons
frame_btn = tk.Frame(root, pady = 10, bg=background)
frame_btn.pack()

save_btn = tk.Button(frame_btn, text = "Save", command=lambda:mSave(), height=2, width=10, font=("Times New Roman", 14), bg='#D4F1F4')
save_btn.grid(column = 0, row = 0)

clear_btn = tk.Button(frame_btn, text = "Clear", command=lambda:command_textbox.delete('1.0', "end"), height=2, width=10, font=("Times New Roman", 14), bg='#D4F1F4')
clear_btn.grid(column = 1, row = 0)

root.mainloop()
