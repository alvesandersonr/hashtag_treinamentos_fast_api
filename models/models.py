from sqlalchemy import create_engine

# cria a conexao do seu banco
db = create_engine("sqlite:///./../database/app.db")

# Pedido
# ItensPedido

# executa a criação dos metadados do seu banco (cria efetivamente o banco de dados)