def jumlah_digit(n):
    if n < 10:
        return n
    else:
        digit_terakhir= n % 10
        sisa_angka= n // 10

        return digit_terakhir + jumlah_digit(sisa_angka)
    
input =1234
hasil = jumlah_digit(input)

print('input = ',input)
print('output = ',hasil)