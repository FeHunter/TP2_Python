def criar_pa(primeiro, segundo):
    razao = segundo - primeiro
    pa = [primeiro]
    for i in range(1, 10):
        proximo = pa[i-1] + razao
        pa.append(proximo)
    print(pa)

criar_pa(3, 30)