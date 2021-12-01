"""                                                                    
          _____                    _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                  /\    \         
        /::\    \                /::\____\                /::\    \                /::\    \        
       /::::\    \              /:::/    /               /::::\    \              /::::\    \       
      /::::::\    \            /:::/    /               /::::::\    \            /::::::\    \      
     /:::/\:::\    \          /:::/    /               /:::/\:::\    \          /:::/\:::\    \     
    /:::/__\:::\    \        /:::/____/               /:::/__\:::\    \        /:::/  \:::\    \    
   /::::\   \:::\    \      /::::\    \              /::::\   \:::\    \      /:::/    \:::\    \   
  /::::::\   \:::\    \    /::::::\    \   _____    /::::::\   \:::\    \    /:::/    / \:::\    \  
 /:::/\:::\   \:::\____\  /:::/\:::\    \ /\    \  /:::/\:::\   \:::\____\  /:::/    /   \:::\ ___\ 
/:::/  \:::\   \:::|    |/:::/  \:::\    /::\____\/:::/  \:::\   \:::|    |/:::/____/     \:::|    |
\::/    \:::\  /:::|____|\::/    \:::\  /:::/    /\::/    \:::\  /:::|____|\:::\    \     /:::|____|
 \/_____/\:::\/:::/    /  \/____/ \:::\/:::/    /  \/_____/\:::\/:::/    /  \:::\    \   /:::/    / 
          \::::::/    /            \::::::/    /            \::::::/    /    \:::\    \ /:::/    /  
           \::::/    /              \::::/    /              \::::/    /      \:::\    /:::/    /   
            \::/____/               /:::/    /                \::/____/        \:::\  /:::/    /    
             ~~                    /:::/    /                  ~~               \:::\/:::/    /     
                                  /:::/    /                                     \::::::/    /      
                                 /:::/    /                                       \::::/    /       
                                 \::/    /                                         \::/____/        
                                  \/____/                                           ~~              
                                                                                                                                                                           
@Tchoow
"""                                                                          


# Importing the libraries
from pynput.mouse import Listener
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageGrab
import cv2
import pytesseract
import subprocess


# Creating the GUI
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


# execute os command and get result
def executeCommand():
    process = subprocess.Popen("php prog.php", stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output


# extract text from a screenshot
def extractText():
    img = cv2.imread("screenshot.png")
    # recognize text with pytesseract
    
    text = pytesseract.image_to_string(img)
    text = cleanString(text)
    print(text)
    return text

# create a txt file with content
def createPhpFile(content):
    file = open("prog.php", "w")
    file.write(content)
    file.close()

def takeCapture(click1, click2):
    xCLick1 = click1[0]
    yCLick1 = click1[1]
    xCLick2 = click2[0]
    yCLick2 = click2[1]
    img = ImageGrab.grab(bbox =(xCLick1, yCLick1, xCLick2, yCLick2))
    # img to black and white
    img = img.convert('L')
    img.save("screenshot.png")

def fillTextField(text):
    textField.insert("1.0",text)

def cleanString(string):
    string = string.replace("<2php", "<?php")
    string = string.replace("\x0c", "")
    return string

# start the capture mode
def startCapture():
    clicks = []
    def on_click(x, y, button, pressed):
        if pressed:
            clicks.append((x, y))
            print(clicks)

        if len(clicks) == 2:
            takeCapture(clicks[0], clicks[1])
            createPhpFile(extractText())
            listener.stop()
            listener.stop()
            fillTextField(executeCommand())
            print(executeCommand())
            


    with Listener(on_click=on_click) as listener:
        listener.join()



# fill the txt field with the result


# Frame
root = tk.Tk()
root.geometry("300x400")
root.title("PHPD")

label = ttk.Label(root, padding=10, text="PHPD")
label.config(font=("Arial",40), foreground="#6c5ce7", background="#a29bfe")
label.pack()

label = ttk.Label(root, padding=10, text="@Tchoow")
label.config(font=("Arial",10), foreground="#6c5ce7", background="#a29bfe")
label.pack()

# Add buttons
button1 = tk.Button(root, text="Commencer a capturer", command=startCapture)
button1.config(font=("Arial",20), foreground="#6c5ce7", background="#a29bfe")
button1.pack()

label = ttk.Label(root, padding=10, text="Resultat")
label.config(font=("Arial",15), foreground="#6c5ce7", background="#a29bfe")
label.pack()


# fill the textField with the result


textField = tk.Text(root, height=10, width=30)
textField.config(font=("Arial",15), foreground="#6c5ce7", background="#a29bfe")
textField.pack()



# change frame color


root.configure(background='#a29bfe')

# console set Text
root.mainloop()
