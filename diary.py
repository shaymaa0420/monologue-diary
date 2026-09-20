#Diary!!! <3

import datetime as dt
import logging
logging.basicConfig(filename='diary log', level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%m/%d/%y %H:%M:%S')

print(" ")
print("⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔")
print("Welcome to your diary!!! :)")
print("Type 'BEGIN' to start writing.", end= " ")
print("Type 'END' to stop writing.")
print(" ")
diary_status = input("Enter your choice: ")
print(" ")

if diary_status == "END":
    print()
if diary_status == "BEGIN":
    print(" ")
    print("-> Type entry here: ")
    entry = input()
    logging.info("Entry saved: %s", entry)
    current_time = dt.datetime.now().strftime('%m/%d/%y %H:%M')
    print("-> Entry saved!")
    print("-> " + str(current_time))
    print(" ")
    print("[Type 'END' to stop writing. Type 'BEGIN' to write another entry.]")
    print(" ")
    diary_status = input(" ")

while diary_status != "END":
    print(" ")
    print("-> Type entry here: ")
    print(" ")
    entry = input()
    logging.info("Entry saved: %s", entry)
    current_time = dt.datetime.now().strftime('%m/%d/%y %H:%M')
    print("-> Entry saved!")
    print("-> " + str(current_time))
    print(" ")
    print("[Type 'END' to stop writing. Type 'BEGIN' to write another entry.]")
    print(" ")
    diary_status = input(" ")
else:
    print(" ")
    print("-> Thank you! Goodbye!")
    print("⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔")
    print(" ")