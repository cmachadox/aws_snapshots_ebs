# Criar Snapshots

Função responsável por criar Snapshots automatizados

**Simplesmente copie e cole o código do arquivo main.py no console do AWS Lambda e defina também todos os parâmetros necessários para o funcionamento correto dessa função (como timeout, roles, etc)**
#### Requerimentos instances tag
**Key =** snapshot

 **Value =** yes

#### Requerimentos functions
+ **Runtime:** Python 3.6
+ **LambdaHandler:** main.handler
+ **Timeout:** 30

**Obs:**
Essa função faz backup de TODAS as instâncias do parque quais tiverem a tag **snapshot** configurada:D
