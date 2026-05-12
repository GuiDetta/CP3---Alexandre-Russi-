temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

maior_criticos = 0
sala_mais_critica = 0

for i in range(len(temperaturas)):
    sala = temperaturas[i]

    media = sum(sala) / len(sala)
    criticos = sum(1 for temperatura in sala if temperatura >= 33)

    print(f"Sala {i + 1}:")
    print(f"  Média de temperatura: {media:.2f}°C")
    print(f"  Registros críticos: {criticos}\n")

    if criticos > maior_criticos:
        maior_criticos = criticos
        sala_mais_critica = i + 1

print(f"Sala com maior risco: Sala {sala_mais_critica}")