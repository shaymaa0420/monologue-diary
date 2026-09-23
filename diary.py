#Personal diary program.
#Allows users to write entries.
#Entries are dated and saved to a log file.

import datetime as dt
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

#Saving diary entries to a log file with timestamp.
def save_entry_to_log(entry_text):
    timestamp = dt.datetime.now().strftime('%m/%d/%y %H:%M')
    with open('diary log', 'a', encoding='utf-8') as diary_file:
        diary_file.write(f'{timestamp} - {entry_text}\n')

#Creating a new window for diary entry.
def open_entry_window(root):
    entry_window = tk.Toplevel(root)
    entry_window.title('Diary Entry')
    entry_window.configure(background='#FFE6EA')
    entry_window.geometry('450x500+500+200')

    custom_font = font.Font(family='Helvetica', size=20, weight='bold')
    title_style = {'bg': '#FFE6EA', 'fg': 'black', 'highlightthickness': 0, 'bd': 0}
    tk.Label(entry_window, text='⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔', font=custom_font, **title_style).pack(pady=(10, 0))
    tk.Label(entry_window, text='Start writing here!', font=custom_font, **title_style).pack(pady=10)

    diary_entry = tk.Text(
        entry_window,
        height=12,
        width=30,
        font=('Helvetica', 14),
        bg='#FFF7F8',
        fg='black',
        selectbackground='#FFF7F8',
        selectforeground='black',
        highlightthickness=0,
        highlightbackground='#FFF7F8',
        highlightcolor='#FFF7F8',
        insertbackground='black'
    )
    diary_entry.pack(padx=20, pady=10)

    status_label = tk.Label(entry_window, text='', fg='green', font=('Helvetica', 12, 'bold'), bg='#FFE6EA', highlightthickness=0, bd=0)
    status_label.pack()

    #Function to save the diary entry when the button is clicked.
    def save_entry():
        text = diary_entry.get('1.0', 'end-1c').strip()
        if not text:
            status_label.config(text='Please type something first.', fg='red')
            return

        save_entry_to_log(text)
        status_label.config(text='Entry saved!', fg='green')
        status_label.after(3000, status_label.destroy)

    tk.Button(entry_window, text='Save Entry', font=('Helvetica', 14, 'bold'), command=save_entry, bg='#F9BCC5', width=20, height=2).pack(pady=10)

#Main function to create the main window of the diary application.
def main():
    root = tk.Tk()
    root.title('My Diary')
    root.configure(background='#FFE6EA')
    root.minsize(width=1000, height=1000)
    root.geometry('400x400+200+200')

    custom_font = font.Font(family='Helvetica', size=20, weight='bold')
    title_style = {'bg': '#FFE6EA', 'fg': 'black', 'highlightthickness': 0, 'bd': 0}

    tk.Label(root, text='⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔', font=custom_font, **title_style).pack()
    tk.Label(root, text='Welcome to your diary!', font=custom_font, **title_style).pack()
    tk.Label(root, text='Made by Shaymaa M.', font=custom_font, **title_style).pack()
    tk.Label(root, text=' ', **title_style).pack()
    tk.Label(root, text=' ', **title_style).pack()
    tk.Label(root, text=' ', **title_style).pack()

    img = Image.open('deardiarycute.png')
    timg = img.resize((400, 400), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(timg)
    tk.Label(root, image=photo, bg='#FFE6EA', highlightthickness=0, bd=0).pack()
    tk.Label(root, text=' ', **title_style).pack()
    tk.Label(root, text='Image Credit: https://pin.it/4NwBkQqpN', font=custom_font, **title_style).pack()

    tk.Label(root, text=' ', **title_style).pack()
    tk.Label(root, text=' ', **title_style).pack()
    tk.Label(root, text=' ', **title_style).pack()
    button = tk.Button(root, text='Start Writing', font=custom_font, command=lambda: open_entry_window(root), bg='#F9BCC5', width=20, height=2)
    button.pack()

    root.mainloop()

#Entry point of the program.
if __name__ == '__main__':
    main()