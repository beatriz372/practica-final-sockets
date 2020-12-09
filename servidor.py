import socket
import threading

host = "127.0.0.1"
port = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket Creado")
sock.bind(("127.0.0.1", 9000))
print ("socket conexion establecida")
sock.listen(1)
print ("socket ahora puede ser escuchado")


def worker(*args):
    conn = args[0]
    addr = args[1]
    try:
        print('Conexion con {}.'.format(addr))
        conn.send("Cliente conectado".encode('UTF-8'))
        while True:
            datos = conn.recv(4096)
            if datos:
                print('Recibido: {}'.format(datos.decode('utf-8')))
                
            else:
                print("Cliente desconectado")              
                break
    finally:
        conn.close()
        	
while 1:
    conn, addr = sock.accept()
    threading.Thread(target=worker, args=(conn, addr)).start()
