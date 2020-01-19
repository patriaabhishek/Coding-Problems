def karatsuba(x, y):
    
    sign_x = 1 if x>=0 else -1 
    sign_y = 1 if y>=0 else -1
    prod_sign = sign_x*sign_y
    
    x = abs(x)
    y = abs(y)
    
    #Getting lengths of strings
    x_len = len(str(x))
    y_len = len(str(y))
    
    #Checking for base case of both x and y being single digits
    if ((x_len == 1) and (y_len == 1)):
        return x*y
    
    #Calculating half length and the various products
    
    n2 = max(x_len, y_len)//2
    
    b = x%(10**(n2))
    a = x//(10**(n2))
    d = y%(10**(n2))
    c = y//(10**(n2))
    
    #Recursive calls for multiplication
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    apb_cpd = karatsuba(a+b, c+d)
     
    return(((ac*10**(2*n2)) + ((apb_cpd-ac-bd)*10**(n2)) + bd)*prod_sign)
