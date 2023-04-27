try:
   
    my_file = open('test.txt','r')
    text = my_file.read()
    print(text)
except Exception as e:
    print('Error:', + e)

finally:

    my_file.close()






try:
   
    with open ('test.txt','r') as my_file:
        for line in my_file:
            print(line, end= "")
except Exception as e:
    print('Error:', + e)

finally:

    my_file.close()