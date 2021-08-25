import subprocess

result = subprocess.check_output('echo hello', shell=False)
print(result.decode('utf-8'))
