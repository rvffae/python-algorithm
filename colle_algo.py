# Entrainement pour la colle d'algorithmie du 19/11/25

# 1. Somme de série (somme des termes d'une suite)
# suite définie par u0 = 2 et un+1 = 0.2un + 1
# Calculer S = u0 + u1 + u2 + ... + u10 

def somme(n):
    u = 2
    s = 0
    for i in range(0, n+1):
        s = s + u 
        u = 0.2*u + 1
    return(s)



#avec u0 = 5 et un+1 = 2un + 3 

def somme_bis(n):
    u = 5
    s= 0
    for i in range(0, n+1):
        s = s+u
        u = 2*u + 3 
    return(s)


# 2 résultion d'une équation du second degré
# de la forme ax²+bx+c = 0

def equation(a, b, c):
    d = (b**2) -4 * a *c
    
    if d < 0 : 
        print("pas de solution")
        
    elif d == 0 :
        x = (-b) / (2 * a)
        print(x)
    else : 
        racine_d = d ** 0.5 
        x1 = (-b - racine_d) / (2**a)
        x2 = (-b + racine_d) / (2**a)
        print (f"les solutions sont : {x1} et {x2}")
        
        
            
