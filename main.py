import sqlite3
import pandas as pd

# (9) Conecta o banco de dados;
conn = sqlite3.connect('/home/nayaraosorio/PycharmProjects/ProjetoDeBloco/PB_Housing_Data.db')

query = "SELECT * FROM 'New_PB_Housing_Data'"
df = pd.read_sql_query(query, conn)


# (10) Exibe as primeiras 10 linhas das colunas "Garage Type" e "Garage Area";
print("Conteúdo de Garage Type:")
print(df['Garage Type'].head(10))
print('\nConteúdo de Garage Area:')
print(df['Garage Area'].head(10))

# Converte a coluna "Garage Area" para tipo numérico;
df['Garage Area'] = pd.to_numeric(df['Garage Area'], errors='coerce')

# Verifica valores nulos ou em branco na coluna "Garage Type";
null_values = df['Garage Type'].isnull().sum()
empty_values = (df['Garage Type'] == '').sum()
total_missing_values = null_values + empty_values

# Fecha a conexão com o banco de dados;
print('\nValores nulos na coluna "Garage Type":', null_values)
print('Valores em branco na coluna "Garage Type":', empty_values)
print('Total de valores ausentes na coluna "Garage Type":', total_missing_values)

#(11) Apresenta os valores max, min e medio;
max_value = df['Garage Area'].max()
min_value = df['Garage Area'].min()
mean_value = df['Garage Area'].mean()

print('Valor maximo', max_value)
print('Valor mínimo', min_value)
print('Valor Medio', mean_value)

# (12) Exibir os itens únicos da coluna 'Garage Type;
unique_items = df['Garage Type'].unique()
print('\nItens únicos da coluna "Garage Type": ')
for item in unique_items:
    print(item)

# (13) Lista de variável númerica;
garage_area = df['Garage Area'].tolist()

# (14) Lista de variável categórica;
garage_type = df['Garage Type'].tolist()

# (15) Estrutura de repetição da soma dos valores acima da méida da própria váriavel;
sum_above_mean = 0

for value in garage_area:
    if value > mean_value:
        sum_above_mean += value

print('Soma dos acima da média:', sum_above_mean)

# (16) Função para contar a ocorrencia dos itens individuais da variável categórica;

def count_occurrences(data_list):
    occurrences = pd.Series(data_list).value_counts()
    return occurrences

garage_type_counts = count_occurrences(garage_type)

print('Contagem de ocorrência dos itens da variável categórica: ', garage_type_counts)

conn.close()