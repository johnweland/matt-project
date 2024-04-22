import tkinter as tk
import cv2
from PIL import Image, ImageTk
import serial

# Initialize serial connection with Arduino
ser = serial.Serial('/dev/ttyACM0', 9600)  # Use appropriate port and baud rate

# Create GUI window
root = tk.Tk()
root.title("Camera Viewer")

# Create a frame for holding the camera feed
frame = tk.Frame(root)
frame.pack()

# Create a label to display the camera feed
label = tk.Label(frame)
label.pack()

# Function to update the camera feed
def update_camera():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=img)
        label.imgtk = img
        label.configure(image=img)
    label.after(10, update_camera)

# Function to send command to Arduino
def send_command():
    command = command_entry.get()
    ser.write(command.encode())

# Create entry and button for sending commands to Arduino
command_entry = tk.Entry(root, width=20)
command_entry.pack()

send_button = tk.Button(root, text="Send Command", command=send_command)
send_button.pack()

# Initialize camera
cap = cv2.VideoCapture(0)

# Start camera feed
update_camera()

# Run the GUI
root.mainloop()

# Release the camera and close the serial port
cap.release()
ser.close()
