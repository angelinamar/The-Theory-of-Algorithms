x=raw_input('first number=')
y=raw_input('second number=')
def karatsuba(x,y):
    if len(str(x)) == 1 and len(str(y)) == 1:
        x=int(x)
        y=int(y)
        return x*y
    else:
        x=int(x)
        y=int(y)
        n = max(len(str(x)),len(str(y)))
        z = n / 2            
        a = x / 10**(z)
        b = x % 10**(z)
        c = y / 10**(z)
        d = y % 10**(z)              
        ac = karatsuba(a,c)
        bd = karatsuba(b,d)        
        ad_plus_bc = karatsuba(a+b,c+d) - ac - bd
        prod = ac * 10**(2*z) + (ad_plus_bc * 10**z) + bd
            
    return prod
     
print(karatsuba(x,y))
