import subprocess

def is_console():
    try:
        result = subprocess.run('tty'.split(), capture_output=True)
    except OSError as e:
        return false
    return result.stdout.startswith(b'/dev/tty')

print(is_console())
