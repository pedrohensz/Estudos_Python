# ============================================================
# Regex em Python — Guia Completo
# ============================================================

import re

# ------------------------------------------------------------
# 1. Correspondência Simples (match e search)
# ------------------------------------------------------------

# re.search(): procura o padrão em qualquer parte da string
texto = "Meu número é 1234"
resultado = re.search(r"\d+", texto)
print(resultado.group())  # 1234

# re.match(): verifica apenas no início da string
resultado = re.match(r"Meu", texto)
print(bool(resultado))  # True

# ------------------------------------------------------------
# 2. Encontrar todas as ocorrências com findall()
# ------------------------------------------------------------

texto = "Códigos: 123, 456, 789"
numeros = re.findall(r"\d+", texto)
print(numeros)  # ['123', '456', '789']

# ------------------------------------------------------------
# 3. Substituição com sub()
# ------------------------------------------------------------

texto = "Telefone: 99999-0000"
novo = re.sub(r"\d", "*", texto)
print(novo)  # Telefone: *****-****

# ------------------------------------------------------------
# 4. Divisão de string com split()
# ------------------------------------------------------------

texto = "a,b;c|d"
partes = re.split(r"[,;|]", texto)
print(partes)  # ['a', 'b', 'c', 'd']

# ============================================================
# Principais Metacaracteres do Regex
# ============================================================

"""
.      -> qualquer caractere
\d     -> dígito (0–9)
\D     -> não dígito
\w     -> letras, números e _
\W     -> não \w
\s     -> espaços
+      -> 1 ou mais
*      -> 0 ou mais
?      -> 0 ou 1
{n}    -> exatamente n repetições
{n,m}  -> entre n e m repetições
^      -> início da string
$      -> fim da string
[]     -> conjunto de caracteres
()     -> grupo
|      -> operador OU
"""

# ============================================================
# Exemplos Práticos
# ============================================================

# 1. Validação básica de telefone
padrao = r"\d{5}-\d{4}"
print(bool(re.search(padrao, "99999-0000")))  # True

# 2. Validação simples de e-mail
email = r"^[\w\.-]+@[\w\.-]+\.\w+$"
print(bool(re.match(email, "pedro@gmail.com")))   # True
print(bool(re.match(email, "pedro@g@il.com")))    # False

# 3. Encontrar datas no formato DD/MM/AAAA
texto = "Hoje é 21/02/2025 e amanhã será 22/02/2025."
datas = re.findall(r"\d{2}/\d{2}/\d{4}", texto)
print(datas)  # ['21/02/2025', '22/02/2025']

# 4. Capturar partes de uma data usando grupos
data = "21/02/2025"
padrao = r"(\d{2})/(\d{2})/(\d{4})"

dia, mes, ano = re.match(padrao, data).groups()
print(dia, mes, ano)  # 21 02 2025

# 5. Remover tudo que não é número (ex.: CPF)
cpf = "123.456.789-00"
limpo = re.sub(r"\D", "", cpf)
print(limpo)  # 12345678900