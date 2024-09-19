import os
import sys
import subprocess
from datetime import datetime

def backup():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"/app/db_backups/backup_{timestamp}.sql"
    
    # Set PGPASSWORD as an environment variable for the subprocess
    env = os.environ.copy()
    env["PGPASSWORD"] = os.environ.get('POSTGRES_PASSWORD', '12qwaszx')
    
    subprocess.run([
        "pg_dump",
        "-h", os.environ.get('DATABASE_HOST', 'db'),
        "-p", os.environ.get('DATABASE_PORT', '5432'),
        "-U", os.environ.get('POSTGRES_USER', 'joro'),
        "-d", os.environ.get('POSTGRES_DB', 'elonfan'),
        "-f", backup_file
    ], env=env, check=True)
    
    print(f"Backup created: {backup_file}")

def restore(backup_file):
    # Set PGPASSWORD as an environment variable for the subprocess
    env = os.environ.copy()
    env["PGPASSWORD"] = os.environ.get('POSTGRES_PASSWORD', '12qwaszx')
    
    subprocess.run([
        "psql",
        "-h", os.environ.get('DATABASE_HOST', 'db'),
        "-p", os.environ.get('DATABASE_PORT', '5432'),
        "-U", os.environ.get('POSTGRES_USER', 'joro'),
        "-d", os.environ.get('POSTGRES_DB', 'elonfan'),
        "-f", backup_file
    ], env=env, check=True)
    
    print(f"Restored from: {backup_file}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "backup":
            backup()
        elif sys.argv[1] == "restore" and len(sys.argv) > 2:
            restore(sys.argv[2])
        else:
            print("Usage: python db_ops.py [backup|restore <backup_file>]")
    else:
        print("Usage: python db_ops.py [backup|restore <backup_file>]")
