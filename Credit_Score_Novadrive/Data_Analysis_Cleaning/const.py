# Lendo a consulta SQL do arquivo
sql_query = ""
with open(r"D:\Repositories\Data-Science\Credit_Score_Novadrive\queries\data_denormalization.sql", "r", encoding="utf-8") as file:
    sql_query = file.read()
