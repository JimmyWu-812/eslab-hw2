import socket 
import json
import numpy as np
import matplotlib.pyplot as plot
HOST = '192.168.43.36' # IP address
PORT = 8000 # Port to listen on (use ports > 1023)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Starting server at: ", (HOST, PORT))
    conn, addr = s.accept()
    with conn:
        print("Connected at", addr)
        while True:
            data = conn.recv(1024).decode('utf-8')
            print("Received from socket server:", data)
            if (data.count('{') != 1):
                pass
                # Incomplete data are received.
                # Some codes here
    obj = json.loads(data)
    t = obj['s']
    plot.scatter(t, obj['x'], c='blue') # x, y, z, gx, gy, gz
    # some codes here
    plot.xlabel("sample num")
    plot.pause(0.0001)
