# ENGDADOS-SOLUCOES

> Validação e **deduplicação** de dados com **Pandas**, **Pandera** e **spaCy** – notebooks prontos para uso no VS Code/Jupyter.

## 📌 Visão geral

Este repositório contém notebooks e utilitários para:

* Limpeza e normalização de dados CSV (separador `;`).
* **Deduplicação** por chaves (e-mail, CPF, etc.), com regras de comparação configuráveis.
* **Validação de qualidade** com **Pandera** (schema e checks).
* Auxílios de NLP com **spaCy** (tokenização, NER/dep) para campos textuais (ex.: `descricao`).

## 🗂️ Estrutura do projeto

```
ENGDADOS-SOLUCOES/
├─ datasets/
│  └─ LOGINS.csv            # dataset de exemplo (sep=';')
├─ notebooks/
│  ├─ 00.criaValidacao.ipynb
│  ├─ 01.QualidadeDados.ipynb
│  ├─ 02.Deduplicacao.ipynb
│  ├─ 03.QualidadePandera.ipynb
│  ├─ 04.validacao.ipynb
│  ├─ 05.TestesEntrada.ipynb
│  ├─ app.ipynb
│  ├─ argparse.ipynb
│  └─ path.ipynb
├─ src/                     # (opcional) scripts auxiliares
├─ tests/
├─ .env                     # variáveis locais (opcional)
├─ environment.yml          # ambiente conda (opcional)
├─ pyproject.toml           # projeto Python (opcional)
└─ readme.md                # este arquivo
```

## ✅ Pré-requisitos

* **Python 3.10+**
* **VS Code** com Jupyter e Python extensions (ou Jupyter Notebook/Lab)
* (Opcional) **Conda/Mamba**

## 🧪 Ambiente

### Via `venv`

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# Linux/macOS
# source .venv/bin/activate

python -m pip install -U pip
python -m pip install pandas numpy pandera spacy ipywidgets matplotlib openpyxl pyarrow typer streamlit spacy-streamlit

# modelos spaCy (PT)
python -m spacy download pt_core_news_md
# (ou pt_core_news_lg, se preferir)
```

### Via `conda` (opcional)

```bash
mamba env create -f environment.yml
mamba activate engdados-solucoes
```

## 📥 Entrada de dados

* Coloque seus arquivos em `datasets/`.
* Exemplo de leitura (Windows):

```python
import pandas as pd
from pathlib import Path
caminho = Path(r"E:/engDados-Solucoes/datasets/LOGINS.csv")
df = pd.read_csv(caminho, sep=';', encoding='utf-8')  # tente 'utf-8-sig' ou 'cp1252' se der erro de acento
```

**Colunas esperadas no exemplo**: `cpf`, `email`, `senha`, `data_de_nascimento`, `estado`, `data_cadastro`, `ipv4`, `cor_favorita`, `profissao`, `telefone`.

## 🔁 Deduplicação (notebook `02.Deduplicacao.ipynb`)

### Passos típicos

1. **Normalizar** e-mail/CPF (trim, lowercase, remover máscara de CPF).
2. Criar chaves de comparação (ex.: `email` limpo, `cpf` numérico).
3. Usar `drop_duplicates` ou métricas de similaridade, conforme necessidade.

```python
import re

def clean_email(s):
    s = str(s).strip().lower()
    return s if '@' in s else None

def clean_cpf(s):
    s = re.sub(r'\D', '', str(s))  # só dígitos
    return s if len(s) == 11 else None

# chaves normalizadas
df['email_norm'] = df['email'].apply(clean_email)
df['cpf_norm']   = df['cpf'].apply(clean_cpf)

# regra base: duplicado se email OU cpf coincidem
duplicados = df.duplicated(subset=['email_norm', 'cpf_norm'], keep='first')
base_sem_dup = df[~duplicados].copy()
```

> **Dica:** para comparação por “apenas e-mail” ou “apenas CPF”, ajuste `subset`. Para similaridade fuzzy, considere `rapidfuzz`.

## 🧰 Qualidade de dados com **Pandera** (notebook `03.QualidadePandera.ipynb`)

```python
import pandera as pa
from pandera import Column, Check

schema = pa.DataFrameSchema({
    'cpf': Column(str, nullable=False),
    'email': Column(str, Check.str_contains(r"@"), nullable=False),
    'data_cadastro': Column(str, nullable=True),
    'estado': Column(str, Check.isin({'AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO'})),
})

validado = schema.validate(df, lazy=True)
```

## 🖥️ App Streamlit (opcional)

Arquivo mínimo com **spaCy Streamlit** para visualizar `ner/textcat`:

```python
# streamlit_app.py
import spacy, spacy_streamlit

def app(model='pt_core_news_md', text='Digite um texto aqui…'):
    spacy_streamlit.visualize([model], text, visualizers=['ner'])

if __name__ == '__main__':
    app()
```

Executar:

```bash
streamlit run streamlit_app.py
```

## 🧪 Testes rápidos

* Use o notebook `05.TestesEntrada.ipynb` para exercitar leitura/normalização de entradas.
* Crie asserts simples ou adicione testes com `pytest` em `tests/`.

## ⚠️ Troubleshooting

* **`ImportError: cannot import name 'display' from IPython.core.display`**: renderize displaCy **sem** Jupyter e salve como HTML (`jupyter=False`).
* **Modelos spaCy**: use `pt_core_news_md`/`lg` (melhor NER/dep). Baixe com `python -m spacy download pt_core_news_md`.
* **Encoding no Windows**: tente `utf-8-sig` ou `cp1252`.
* **Separador `;`**: lembre de `sep=';'` no `read_csv`.

## 📝 Licença

MIT. Sinta-se à vontade para adaptar e reutilizar.

---

**Autora** Luciana Sampaio – Engenharia de Dados
