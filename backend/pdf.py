import time
import subprocess
import os

dropbox_folder_path = "dropboxfolder/"
log_file_max_lines = 3
log_file_counter = 1

def start_api():
    process = subprocess.Popen(['python','manage.py','runserver'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    return process

def write_logs(process):
    global log_file_counter
    line_count = 0
    current_log_file = f"api_logs_{log_file_counter}.txt"
    with open(current_log_file, 'a') as file:
        while process.poll() is None:
            output = process.stdout.readline()
            error = process.stderr.readline()
            if output:
                file.write(output.strip() + '\n')
                line_count += 1
            if error:
                file.write(error.strip() + '\n')
                line_count += 1
            if line_count >= log_file_max_lines:
                file.close()
                line_count = 0
                log_file_counter += 1
                current_log_file = f"api_logs_{log_file_counter}.txt"
                with open(current_log_file, 'a') as file:
                    pass  # Just to create a new log file
            time.sleep(3)

def main():
    api_process = start_api()
    write_logs(api_process)

if __name__ == "__main__":
    main()
