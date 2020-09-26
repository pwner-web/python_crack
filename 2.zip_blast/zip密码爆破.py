import zipfile
import traceback
import os
import shutil

def read_dicts(filename):
    dicts = []
    with open(filename, 'r')as fp:
        dicts = [pwd.strip() for pwd in fp.readlines()]
    return dicts

def blast(zip_f, pwd):
    try:
        zip_f.extractall('./temp', pwd=pwd.encode())
        return pwd
    except Exception as e:
        if "Bad password" in str(e):
            traceback.print_exc()

if __name__ == '__main__':
    dict_file = './zip_dict.txt'
    zip_file = zipfile.ZipFile('./test.zip')
    for password in read_dicts(dict_file):
        result = blast(zip_file, password)
        if result:
            print(f'[+] get password:{result}')
            break
        else:
            print('[-] not found password.')
        shutil.rmtree('./temp')
        os.mkdir('./temp')