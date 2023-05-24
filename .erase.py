i = 1
while True:
    filename = f'file_{i}.00'
    with open(filename, 'wb') as f:
        f.write(b'\x00' * 200000000)
        i += 1


