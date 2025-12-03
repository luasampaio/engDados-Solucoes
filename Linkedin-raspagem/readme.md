# LinkedIn Job Scraper (Buscador Vagas)

Script em Python para buscar vagas no LinkedIn usando o endpoint público de jobs e salvar os resultados em **Excel**, com as colunas automaticamente ajustadas ao tamanho do conteúdo.

> ⚠️ **Aviso importante**  
> Este projeto é apenas para fins educacionais.  
> Respeite sempre os **Termos de Uso do LinkedIn**, as leis de proteção de dados e limites de acesso (rate limits).  
> Não use este código para automações agressivas ou que quebrem as políticas da plataforma.

---

## 📌 Funcionalidades

- Busca **IDs de vagas** a partir de:
  - palavra-chave (ex.: `"engineer"`, `"scientist"`)
  - localização (ex.: `"Brazil"`, `"Lisbon, Portugal"`)
- Faz scrape dos **detalhes da vaga**:
  - Título da vaga (`job_title`)
  - Nome da empresa (`company_name`)
  - Nível de experiência (`experience_level`)
  - Tipo de contrato (`type_of_contract`)
  - Se é **Easy Apply** ou não (`easy_apply`)
  - Tempo desde a postagem (`time_posted`)
  - Número de candidatos (`num_applicants`)
  - Link da vaga (`job_link`)
- Gera um **DataFrame (pandas)** com os dados.
- Salva tudo em **arquivo Excel (.xlsx)** com:
  - colunas auto-ajustadas ao conteúdo
  - opção de definir larguras personalizadas por coluna
  - opção de quebra de linha automática em textos longos

---

## 🧩 Tecnologias usadas

- Python 3.9+
- [requests](https://pypi.org/project/requests/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [pandas](https://pypi.org/project/pandas/)
- [openpyxl](https://pypi.org/project/openpyxl/) (para escrever Excel)

---

## 📦 Instalação

1. Clone o repositório (ou copie os arquivos para uma pasta):

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

2. (Opcional, mas recomendado) Crie e ative um ambiente virtual: 

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

##  Estrutura básica do código

As principais funções são:

- fetch_job_ids(title, location, num_pages, ...)
- Busca os job_id das vagas a partir da busca no LinkedIn.

- scrape_jobs(id_list, ...)
- Recebe uma lista de job_id e busca os detalhes de cada vaga.

- run_linkedin_pipeline(title, location, num_pages, out_xlsx, verbose)
- Faz tudo: busca IDs, scrape dos detalhes e retorna um DataFrame.

- salvar_em_excel_ajustado(df, caminho_arquivo, sheet_name, col_widths, auto_row_height)
- Salva o DataFrame em Excel com colunas ajustadas e tamanhos personalizados.


