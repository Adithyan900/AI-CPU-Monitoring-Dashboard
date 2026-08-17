def home(a):
    if a==25:
        return
    print(a)
    home(a+1)
    print('hi')
home(20)    