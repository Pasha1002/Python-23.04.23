

try:
    with open('new file.txt', 'r') as f:
        file_cont = f.read().split()
    striing = 'hello'
    if striing in file_cont:
        print('String found')
    else:
        print('String not found')
except Exception as e:
    print(f'error: {e}')