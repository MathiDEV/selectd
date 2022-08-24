from selectd.runcommand import run_command

def get_active_window():
    pid = run_command("xdotool getactivewindow getwindowpid")
    if pid != "0":
        process = run_command("ps -p {} -o comm=".format(pid))
        return process
    return None

def focus_process(name):
    run_command("xdotool search --name {} windowactivate".format(name))