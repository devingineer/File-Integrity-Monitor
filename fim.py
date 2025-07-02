import hashlib
import os
import time

def calculate_file_hash(file_path):
    """
    Calculate and return the SHA-256 hash of a file.
    """
    hash_object = hashlib.sha256()
    with open(file_path, 'rb') as file:
        file_data = file.read()
        hash_object.update(file_data)
    return hash_object.hexdigest()

files_to_monitor = ["test.txt", "test2.txt"]

def monitor_files():
    """
    Monitor files for changes by comparing their hashes.
    """
    previous_hashes = {}

    while True:
        for file_path in files_to_monitor:
            if os.path.exists(file_path):
                current_hash = calculate_file_hash(file_path)
                if file_path not in previous_hashes or previous_hashes[file_path] != current_hash:
                    print(f"File has changed: {file_path}")
                    log_change(file_path)
                    previous_hashes[file_path] = current_hash
                else:
                    print(f"No change detected for {file_path}")
            else:
                print(f"File does not exist: {file_path}")
        time.sleep(5)

def log_change(file_path):
    """
    Log the change to a file in the log folder.
    """
    log_directory = "logs"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    
    log_file_path = os.path.join(log_directory, "file_changes.log")

    with open(log_file_path, 'a') as log_file:
        log_file.write(f"{time.ctime()}: {file_path} has changed.\n")

if __name__ == "__main__":
    monitor_files()