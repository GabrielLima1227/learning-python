# Laços 'for' executam um bloco de código um número fixo de vezes.
# Você pode iterar sobre um intervalo, string, sequência, etc.

credit_card = "1234-5678-9012-3456"

for x in range(1, 11, 3):
    print(x)

for x in credit_card:
    print(x)

for x in range(1, 21):
    if x == 13:
        break
else:
    print(x)