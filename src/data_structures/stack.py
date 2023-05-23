import socket

host = 'localhost'

def take_picture():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, 5000))
        s.sendall(b'take_picture')
        data = s.recv(1024)
        print('Received', repr(data))
        

def get_camera_data():
  port = 5000
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((host, port))
  take_picture()
  reponse = s.recv(1024)
  decoded_response = reponse.decode()
  print(f"{decoded_response.split(',')}")
  s.close()
  
  if __name__ == "__main__":
    get_camera_data()