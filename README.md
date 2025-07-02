# File Integrity Monitor (FIM)

This is a simple File Integrity Monitor (FIM) that detects unauthorized changes to a monitored file. It calculates the file’s hash and checks if it changes over time. If a change is detected, the event is logged for security analysis.


## What is a File Integrity Monitor (FIM)?

A File Integrity Monitor (FIM) is a security tool that tracks changes to files to detect unauthorized modifications. It is commonly used in cybersecurity to ensure system integrity and protect against threats such as malware, unauthorized access, and data corruption.


### Why is FIM Important?

- **Detects Unauthorized Changes:** Alerts security teams if critical files are modified without approval.
- **Prevents Security Breaches:** Helps protect against malware, insider threats, and unauthorized access.
- **Ensures Compliance:** Many security regulations (like PCI DSS, HIPAA) require FIM as part of their guidelines.


## How the Script Works

1. The script calculates a **hash** (a unique fingerprint) of the monitored file.
2. It continuously checks the file at regular intervals.
3. If the file’s hash changes, the script logs the modification.
4. The log records **when the change happened** and the **new hash value**


## How to Use the Program

1. Open a terminal and navigate to the project folder
2. Run the script using Python: python fim.py
3. Modify the monitored file (e.g., open it in a text editor and add or remove some text).
4. Check the `logs` folder for any recorded changes.
To stop the program, press `CTRL + C`