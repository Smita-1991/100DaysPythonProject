def add(*args):
    sum=0
    for arg in args:
        if arg%2==0:
            sum+=arg
    print(sum)

add(7,8,9,8,4)


def calculate(n,**kwargs):
    n+=kwargs['add']
    n*=kwargs['mul']
    print(n)

calculate(6,add=3,mul=5)