import os
import shutil
from datetime import datetime

# Define the file paths
recipes_file = 'recipes.sqlite'
backup_file = 'recipes_backup.sqlite'
backup_dir = 'DB backups'

# Get the current date and time
now = datetime.now()
date_time_str = now.strftime('%Y-%m-%d_%H-%M-%S')

# Create a copy of the recipes file with the current date and time
new_backup_file = f'recipes_{date_time_str}.sqlite'
shutil.copy(recipes_file, new_backup_file)

# Move the copied file to the backup directory
shutil.move(new_backup_file, os.path.join(backup_dir, new_backup_file))

# Move the existing backup file to the backup directory
if os.path.exists(backup_file):
    shutil.move(backup_file, os.path.join(backup_dir, backup_file)) 