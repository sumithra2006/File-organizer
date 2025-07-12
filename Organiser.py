import os
import shutil
from datetime import datetime

source_folder = os.path.join(os.path.expanduser("~"), "Desktop")

def organize_by_date():
    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)

        if os.path.isfile(file_path):
            timestamp = os.path.getmtime(file_path)
            date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

            folder_path = os.path.join(source_folder, date)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            shutil.move(file_path, os.path.join(folder_path, file_name))

if __name__ == "__main__":
    organize_by_date()
    print("Files organized into date-based folders successfully!")
