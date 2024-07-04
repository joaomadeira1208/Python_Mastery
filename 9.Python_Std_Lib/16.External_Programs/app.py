import subprocess

# for linux/mac, search for the windows how to do the equivalent code
# completed = subprocess.run(["ls", "-l"])


completed = subprocess.run(["python", "other.py"],
                           capture_output=True,
                           text=True)
print("args", completed.args)
print("returncode", completed.returncode)
print("stderr", completed.stderr)  # Standart Error
print("stdout", completed.stdout)  # Standart Output


# Legacies Methods
# subprocess.call
# subprocess.check_call
# subprocess.check_output
# subprocess.Popen
