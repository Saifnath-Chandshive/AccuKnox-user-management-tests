import os
import shutil
from datetime import datetime

# Set source folder and backup (destination) folder
source_folder = "my_data"
backup_folder = "backup_storage"

# Create a unique backup filename with date and time
date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_filename = f"backup_{date_str}.zip"
backup_path = os.path.join(backup_folder, backup_filename)

try:
        # Make sure destination folder exists
    os.makedirs(backup_folder, exist_ok=True)
    # Create zip file from source folder
    shutil.make_archive(backup_path.replace('.zip', ''), 'zip', source_folder)
    print(f"Backup successful: {backup_filename}")
except Exception as e:
    print("Backup failed:", e)