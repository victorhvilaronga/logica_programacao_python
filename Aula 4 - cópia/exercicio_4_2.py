#criar tabuada do 1 ao 10

x = 1
res = 0
while (x <=10):
    for i in range (1,11,1):
        res = x * i
        print(f'{x}x{i} = {res}')
    x += 1


        