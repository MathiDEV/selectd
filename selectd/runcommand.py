import subprocess

def run_command(command):
    stdout, stderr = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    return stdout.decode('utf-8').strip()