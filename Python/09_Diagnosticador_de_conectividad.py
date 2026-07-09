import subprocess

IP_Local = "127.0.0.1"
result = subprocess.run(["ping", "-c", "1", IP_Local], capture_output=True,text=True)
print(result.stdout)