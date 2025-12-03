# Gerador Automático de Descritivos de Campos

Esta ferramenta permite gerar descritivos completos e profissionais de campos de formulário ou banco de dados de forma automática, economizando tempo na documentação de sistemas.

## Características

A ferramenta gera automaticamente:

- **Descrições textuais completas** em linguagem natural e profissional
- **Tabelas de especificações técnicas** com todos os detalhes do campo
- **Relatórios em Markdown** prontos para documentação
- **Exportação em JSON** para integração com outros sistemas

## Como Usar

### Uso Básico

```python
from gerador_descritivos import GeradorDescritivos

# Criar instância do gerador
gerador = GeradorDescritivos()

# Adicionar campos
gerador.adicionar_campo(
    nome="nome_completo",
    tipo="string",
    obrigatorio=True,
    tamanho_min=3,
    tamanho_max=100,
    descricao_customizada="Este campo armazena o nome completo do usuário."
)

# Gerar relatório em Markdown
relatorio = gerador.gerar_relatorio_markdown("Minha Documentação")

# Salvar em arquivo
with open('documentacao.md', 'w', encoding='utf-8') as f:
    f.write(relatorio)
```

### Parâmetros Disponíveis

Ao adicionar um campo, você pode especificar:

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| `nome` | string | Nome do campo (obrigatório) |
| `tipo` | string | Tipo do campo (obrigatório) |
| `obrigatorio` | boolean | Se o campo é obrigatório (padrão: False) |
| `tamanho_min` | int | Tamanho mínimo em caracteres |
| `tamanho_max` | int | Tamanho máximo em caracteres |
| `valor_min` | float | Valor mínimo para campos numéricos |
| `valor_max` | float | Valor máximo para campos numéricos |
| `padrao` | string | Valor padrão do campo |
| `unico` | boolean | Se o valor deve ser único (padrão: False) |
| `descricao_customizada` | string | Descrição adicional personalizada |
| `opcoes` | list | Lista de opções válidas para o campo |

### Tipos de Campos Suportados

A ferramenta reconhece automaticamente os seguintes tipos:

**Textuais:**
- `string`, `text`, `varchar`, `char`

**Numéricos:**
- `int`, `integer`, `float`, `decimal`, `double`

**Booleanos:**
- `boolean`, `bool`

**Data e Hora:**
- `date`, `datetime`, `timestamp`, `time`

**Especializados:**
- `email`, `url`, `phone`, `cpf`, `cnpj`, `cep`

**Outros:**
- `json`, `array`, `file`, `image`, `password`

## Exemplos de Uso

### Exemplo 1: Campo de Email

```python
gerador.adicionar_campo(
    nome="email",
    tipo="email",
    obrigatorio=True,
    unico=True,
    descricao_customizada="Utilizado para login e comunicações oficiais."
)
```

**Resultado gerado:**

> **Email** é um campo do tipo endereço de e-mail de preenchimento **obrigatório**. O valor deste campo deve ser **único** no sistema, não podendo haver duplicatas. Utilizado para login e comunicações oficiais.

### Exemplo 2: Campo de Seleção com Opções

```python
gerador.adicionar_campo(
    nome="status",
    tipo="string",
    obrigatorio=True,
    padrao="ativo",
    opcoes=["ativo", "inativo", "pendente", "bloqueado"],
    descricao_customizada="Define a situação atual do cadastro no sistema."
)
```

**Resultado gerado:**

> **Status** é um campo do tipo texto de preenchimento **obrigatório**. As opções válidas são: "ativo", "inativo", "pendente", "bloqueado". Caso não seja informado, o valor padrão será: **ativo**. Define a situação atual do cadastro no sistema.

### Exemplo 3: Campo Numérico com Restrições

```python
gerador.adicionar_campo(
    nome="idade",
    tipo="integer",
    obrigatorio=True,
    valor_min=18,
    valor_max=120,
    descricao_customizada="A idade mínima permitida é 18 anos."
)
```

**Resultado gerado:**

> **Idade** é um campo do tipo número inteiro de preenchimento **obrigatório**, com valor mínimo de 18 e valor máximo de 120. A idade mínima permitida é 18 anos.

### Exemplo 4: Campo de CPF

```python
gerador.adicionar_campo(
    nome="cpf",
    tipo="cpf",
    obrigatorio=True,
    unico=True,
    tamanho_min=11,
    tamanho_max=14,
    descricao_customizada="Deve ser informado apenas números ou no formato XXX.XXX.XXX-XX."
)
```

**Resultado gerado:**

> **Cpf** é um campo do tipo CPF de preenchimento **obrigatório**, com mínimo de 11 caracteres e máximo de 14 caracteres. O valor deste campo deve ser **único** no sistema, não podendo haver duplicatas. Deve ser informado apenas números ou no formato XXX.XXX.XXX-XX.

## Exportação de Dados

### Gerar Relatório em Markdown

```python
relatorio = gerador.gerar_relatorio_markdown("Título da Documentação")
```

O relatório incluirá:
- Título e data de geração
- Descrição completa de cada campo
- Tabela de especificações técnicas
- Formatação profissional em Markdown

### Exportar para JSON

```python
json_data = gerador.gerar_json()
```

Útil para integração com outras ferramentas ou sistemas de documentação automatizada.

## Executando o Exemplo Completo

Para ver a ferramenta em ação com exemplos prontos:

```bash
python3.11 gerador_descritivos.py
```

Isso irá gerar:
- `descritivos_campos.md` - Relatório completo em Markdown
- `descritivos_campos.json` - Dados estruturados em JSON

## Casos de Uso

Esta ferramenta é ideal para:

1. **Documentação de APIs** - Gerar descrições de parâmetros e campos de requisição/resposta
2. **Especificação de Banco de Dados** - Documentar estrutura de tabelas e colunas
3. **Formulários Web** - Criar documentação de campos de formulários
4. **Sistemas Corporativos** - Padronizar documentação de campos em sistemas internos
5. **Validação de Dados** - Documentar regras de validação e restrições

## Vantagens

- **Economia de Tempo**: Gera descritivos automaticamente em segundos
- **Padronização**: Mantém consistência na documentação
- **Completude**: Não esquece nenhum detalhe técnico importante
- **Profissionalismo**: Produz textos bem escritos e formatados
- **Flexibilidade**: Permite customização com descrições adicionais
- **Integração**: Exporta em formatos padrão (Markdown e JSON)

## Personalização

Você pode facilmente estender a ferramenta:

1. **Adicionar novos tipos**: Edite o dicionário `TIPOS_DESCRICAO`
2. **Modificar o formato**: Altere o método `_gerar_descritivo()`
3. **Criar novos relatórios**: Implemente novos métodos de exportação

## Requisitos

- Python 3.6 ou superior
- Nenhuma dependência externa necessária

## Licença

Ferramenta de uso livre para fins educacionais e comerciais.
