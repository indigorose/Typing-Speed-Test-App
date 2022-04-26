# Import tkinter library

from tkinter import *
# import keyboard

# Create an instance of tkinter frame
win = Tk()
win.geometry("750x450")

# Good highlight
high_bg = "#E7FBBE"
high_fg = "#125C13"

# Bad Highlight
bad_bg = "#FFCBCB"
bad_fg = "#B20600"


# Define a function to highlight the text

def add_highlighter():
    text.tag_add("start", "1.0", "1.10")
    text.tag_config("start", background="#FFCBCB", foreground="#B20600")
    content = text.get("1.0", "1.10")
    print(type(content))


# Create a Tex Field
text = Text(win, exportselection=True)
text.insert(INSERT, "Hey there! Howdy?")
text.pack()
# Create a Button to highlight text
Button(win, text="Highlight", command=add_highlighter).pack()
win.mainloop()
