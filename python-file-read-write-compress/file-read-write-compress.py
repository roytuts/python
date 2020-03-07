import os, gzip

def read_file(fname, compress=False):
    if compress:
        f = gzip.GzipFile(fname, 'rb')
    else:
        f = open(fname, 'rb')
    try:
        data = f.read()
    finally:
        f.close()
    return data
  
def write_file(data, fname, compress=True):
    #print(os.getcwd())

    if compress:
        f = gzip.GzipFile(fname, 'wb')
    else:
        f = open(fname, 'wb')
    try:
        f.write(data)
    finally:
        f.close()

data = read_file('hey.txt')
print(data)

data = read_file('hey.gz', True)
print(data)

write_file(b'This is a hello string', 'hello.txt', False)
write_file(b'This is a hello string in compress format', 'hello.txt.gz')