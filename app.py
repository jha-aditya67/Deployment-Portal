# app.py
import time
import sys

print("====================================================")
print("Cloud Deployment Portal Base Engine Initialized Live!")
print("====================================================")

try:
    while True:
        sys.stdout.flush() 
        time.sleep(60)     
except KeyboardInterrupt:
    print("Server shutting down gracefully.")
