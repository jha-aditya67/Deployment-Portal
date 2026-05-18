# app.py
import time
import sys

print("====================================================")
print("Cloud Deployment Portal Base Engine Initialized Live!")
print("====================================================")

# This continuous loop keeps your container awake forever on AWS
try:
    while True:
        sys.stdout.flush() # Forces logs to write to CloudWatch instantly
        time.sleep(60)     # Sleeps for 1 minute, then stays awake
except KeyboardInterrupt:
    print("Server shutting down gracefully.")
