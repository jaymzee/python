import socket
from datetime import datetime

now = datetime.utcnow().isoformat().encode('ascii')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("localhost", 8080))
    s.send(b"hello " + now + b"\n")
