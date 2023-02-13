from tkinter import *
from PIL import Image, ImageTk
import cv2

window = Tk()
cap = cv2.VideoCapture(-1)

# Window Properties
Title = "ASCIIcam"
Width = str(1080)
Height = str(720)
Xoffset = str(0)
Yoffset = str(0)

# Text Properies
Font = "Times New Roman"
TextSize = 11
TextColor = "black"

window.title(Title)
window.geometry(Width + "x" + Height + "+" + Xoffset + "+" + Yoffset)
label = Label(window, text="hi kian\nwasdsssssshi", fg=TextColor, font=(Font, TextSize))
label.grid(row=0, column=0)
label.place(x=int(Width) / 2, y=int(Height) / 2)


def show_frames():
    # Get the latest frame and convert into Image
    cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    # Convert image to PhotoImage
    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.configure(image=imgtk)
    # Repeat after an interval to capture continuously
    label.after(20, show_frames)


ret, frame = cap.read()

# Display the resulting frame
cv2.imshow('frame', frame)
window.mainloop()
