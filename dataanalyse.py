# Importar a base de dados
import pandas as pd

tabela_clientes = pd.read_csv(r"telecom_users.csv")
# Visualizar a base de dados para entender o que temos disponível
print(tabela_clientes.columns)

for coluna in tabela_clientes:
    grafico
# tabela_clientes['NomeDaColuna'] = 21 //-> cria ou substitui coluna, e adiciona o valor 21
# Tratamento de dados
# Olhar como estão distribuídos os Churns(cancelamentos)
# Análisar as causas dos cancelamentos
