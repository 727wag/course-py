faturamento = 1000 # tipo: int -> numero inteiro
custo = 700 # tipo float -> numero com casa decimal

novas_vendas = 100
faturamento = novas_vendas + faturamento

imposto = faturamento * 0.1

lucro = faturamento - custo - imposto

margem_lucro = lucro / faturamento

print("O faturamento foi de ", faturamento)
print("O custo foi de ", custo)
print("O lucro foi de ", lucro)
print("a margem de lucro foi de", round (margem_lucro, 2))

email = "wbastos2004@gmail.com" # tipo string -> texto

teve_lucro = True # variável do tipo booleana

# Mod -> # resto da divisão
tempo_contrato = 170
tempo_anos = 170 / 12
print("Tempo em anos", int(tempo_anos))
tempo_meses = 170 % 12
print("Tempo em meses", tempo_meses)