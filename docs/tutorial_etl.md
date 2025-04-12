# 🧪 ETL Tutorial: Extract, Transform, Load

Este tutorial detalha como realizar o processo ETL (Extract, Transform, Load) usando Python, Scrapy, Pandas e SQLite, com base no projeto de pesquisa de notebooks no Mercado Livre.

---

## 📥 1. Extract (Extração de Dados com Scrapy)

A extração é feita por meio de um Spider Scrapy que acessa as páginas do Mercado Livre e coleta informações sobre notebooks.

### Passos:

1. Acesse o diretório do projeto e ative seu ambiente virtual (se necessário).
2. Execute o Spider com o seguinte comando:

```bash
scrapy crawl notebook -o data/data.jsonl
```

Este comando cria um arquivo `data.jsonl` contendo os dados brutos em formato JSON por linha.

---

## 🧼 2. Transform (Limpeza e Processamento com Pandas)

Após a extração, transformamos os dados utilizando o Pandas, aplicando regras de limpeza e formatação.

### O que é feito:

- Remoção de nulos e substituições com valores padrão.
- Conversão de valores monetários (de string para float).
- Conversão de avaliações (de string para float/int).
- Filtros para remover preços fora da faixa R$1000 a R$10000.
- Adição de colunas de metadados como `_source` e `_datetime`.

### Comando:

```bash
python main.py
```

Esse script lê o `data.jsonl`, aplica todas as transformações e salva os dados limpos no banco `mercadolivre.db`.

---

## 💾 3. Load (Carga dos Dados no SQLite)

No passo final, o DataFrame tratado é carregado em uma tabela SQLite chamada `notebook`.

### O que acontece:

- O banco `mercadolivre.db` é criado (caso não exista).
- Os dados são inseridos na tabela `notebook`.
- Conexão com SQLite é encerrada ao final.

---

## ✅ Resultado Final

Você terá:

- Um arquivo `data.jsonl` com os dados brutos.
- Um banco `mercadolivre.db` com a tabela `notebook`.
- A base pronta para ser usada por dashboards ou análises futuras.

---

## 💡 Dica

Após o ETL, execute a interface gráfica com:

```bash
streamlit run app.py
```

Assim você poderá visualizar os KPIs e insights extraídos!

---