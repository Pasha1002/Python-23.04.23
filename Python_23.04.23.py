




            
try:
    with open('file.txt', 'r') as f:
        content = f.read()
        lines = content.split('\n')
        print(content)
        delete = int(input('delete line: '))
        del lines[delete - 1]

    with open('file.txt', 'w') as f:
        f.write('\n'.join(lines))
        print('\n'.join(lines))
        

except Exception as e:
    print( "Error: " + str(e) )
finally:
    print('done')
    f.close()