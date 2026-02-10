def bilangan_prima(n):
    list_prima = []
    for angka in range(2,n+1):
        prima = True
        for i in range(2,angka):
            if angka % i == 0:
                prima = False
        
        if prima:
            list_prima.append(angka)
    return list_prima 

n = 50
hasil = bilangan_prima(n)

print(f'bilangan prima dari 1 sampai n adalah = ',hasil)




    