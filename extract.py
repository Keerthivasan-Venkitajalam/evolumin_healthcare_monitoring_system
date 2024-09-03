import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import os
import requests
from collections.abc import MutableMapping


# Initialize Firebase Admin SDK with your JSON key file
cred = credentials.Certificate("sensor_data.json")
firebase_admin.initialize_app(cred)

# Create a Firestore client
db = firestore.client()

def retrieve_historical_data():
  selected_date_str = date_picker.get_date()
  selected_time = time_entry.get()
  # Parse the selected date string to a datetime object
  selected_datetime_str = f"{selected_date_str} {selected_time}"

  # Parse the combined date and time string to a datetime object
  selected_datetime = datetime.strptime(selected_datetime_str, "%m/%d/%Y %I:%M%p")

  # Format the selected date to match the Firestore timestamp format
  formatted_date = selected_datetime.strftime("%B %d, %Y at %I:%M%p")

  # Access a Firestore collection and retrieve data from documents with a specific timestamp
  collection_ref = db.collection("patientData")

  # Define a query to filter documents by the timestamp field
  query = collection_ref.where("timestamp", "==", formatted_date)

  # Retrieve matching documents
  docs = query.stream()

  data_str = ""
  for doc in docs:
    data = doc.to_dict()
    data_str += f"Data: {data}\n"

  if data_str:
    result_label.config(text=data_str)
  else:
    result_label.config(text=f"No documents found for {formatted_date}")

def SubmitData():
  config = {
    "apiKey": "AIz*************",
    "authDomain": "senso***********",
    "databaseURL": "https*****************",
    "storageBucket": "se*******************"
  }

  firebase = pyrebase.initialize_app(config)
  db_realtime = firebase.database()
  data = db_realtime.child("Patient Data").get().val()

  if data:
    HeartRate = data.get("Heart")
    SPO2 = data.get("Spo2")
    Temperature = data.get("Temp")

    webhook_url = "https://maker.ifttt.com/trigge*******************"
    data_to_send = {
      "value1": HeartRate,
      "value2": SPO2,
      "value3": Temperature
    }
    response = requests.post(webhook_url, json=data_to_send)
    if response.status_code == 200:
      print("Request Sent")
    else:
      print("Request Not Sent")
  else:
    print("Real-time data not found in the Realtime Database.")


def retrieve_realtime_data():
  def update_realtime_data():
    config = {

      "apiKey": "AIzaSyBeA6*************",
      "authDomain": "sensorda****************",
      "databaseURL": "https://sensordata-******************",
      "storageBucket": "sensorda****************"
    }


    firebase = pyrebase.initialize_app(config)
    db_realtime = firebase.database()

    data = db_realtime.child("Patient Data").get().val()

    if data is not None:
      ECG = data.get("ECG")
      HeartRate = data.get("Heart")
      SPO2 = data.get("Spo2")
      Temperature = data.get("Temp")

      # Update your Tkinter UI with the new data
      data_str = f"Real-time Data:\nHeart Rate: {HeartRate}\nSPO2: {SPO2}\nTemperature: {Temperature}\nECG: {ECG}"


      realtime_label.config(text=data_str, font=("Helvetica", 30), bg="black", fg="white")

    # Schedule the next update in milliseconds (e.g., every 1000ms for 1 second)
    root.after(1000, update_realtime_data)

  realtime_window = tk.Toplevel()
  realtime_window.title("Real-Time Data")

  window_width = 800
  window_height = 400
  screen_width = realtime_window.winfo_screenwidth()
  screen_height = realtime_window.winfo_screenheight()

  x = (screen_width - window_width) // 2
  y = (screen_height - window_height) // 2

  realtime_window.geometry(f"{window_width}x{window_height}+{x}+{y}")


  realtime_label = tk.Label(realtime_window, text="", font=("Helvetica", 30), bg="black", fg="white")
  #realtime_label.pack()
  realtime_label.grid(row=0, column=0, sticky="nsew")
  # Use grid layout and sticky to fill the window
  submit_button = tk.Button(realtime_window, text="Submit Data", command=SubmitData, font=("Helvetica", 16))
  submit_button.grid(row=1, column=0, padx=20, pady=10)
  # Configure the grid to expand and fill the available space
  realtime_window.grid_rowconfigure(0, weight=1)
  realtime_window.grid_columnconfigure(0, weight=1)
  update_realtime_data()

root = tk.Tk()
root.title("Firestore Data Retrieval")

#root.attributes('-fullscreen', True)
# Create a date picker widget

style = ttk.Style()
style.configure("TButton", background="black", foreground="white")
style.configure("TLabel", background="black", foreground="white")
style.layout("TButton", [("Button.focus", {"children": [("Button.padding", {"children": [("Button.label", {"side": "left", "expand": 1})]})]})])

# Configure the Calendar widget
date_picker = Calendar(root, date_pattern="mm/dd/yyyy", background="black", foreground="white", headersbackground="black", headersforeground="white", bordercolor="black", normalbackground="black", normalforeground="white", othermonthbackground="black", othermonthforeground="grey")
date_picker.pack(fill='both', expand=True)
date_picker.config(font=('Helvetica', 20))
# Create a time entry field
time_label = tk.Label(root, text="Select a Time (e.g., 12:00AM):", font=('Helvetica', 16))
time_label.pack()
time_entry = tk.Entry(root, font=('Helvetica', 16))
time_entry.pack()

# Create buttons for switching between historical and real-time data
historical_button = tk.Button(root, text="Historical Data", command=retrieve_historical_data, font=('Helvetica', 16))
historical_button.pack()

realtime_button = tk.Button(root, text="Real-Time Data", command=retrieve_realtime_data , font=('Helvetica', 16))
realtime_button.pack()
# Create buttons to show login and signup windows


result_label = tk.Label(root, text="", font=('Helvetica', 16))
result_label.pack()

root.mainloop()