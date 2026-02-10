import math


def jarak(x1, y1, x2, y2):

    selisih_x_kuadrat= (x2 -x1) ** 2
    selisih_y_kuadrat= (y2 -y1) ** 2

    hasilJarak= math.sqrt(selisih_x_kuadrat + selisih_y_kuadrat)
    return hasilJarak

x1, y1= 0, 0
x2, y2= 3, 4

hasil=jarak(x1, y1, x2, y2)

print('jarak = ',hasil)