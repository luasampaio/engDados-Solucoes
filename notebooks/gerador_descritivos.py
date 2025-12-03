#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador Automático de Descritivos de Campos
Gera descrições completas e profissionais para campos de formulário/banco de dados
"""

import json
from typing import Dict, List, Optional


class GeradorDescritivos:
    """Classe para gerar descritivos automáticos de campos"""
    
    # Mapeamento de tipos para descrições em português
    TIPOS_DESCRICAO = {
        'string': 'texto',
        'text': 'texto',
        'varchar': 'texto',
        'char': 'caractere',
        'int': 'número inteiro',
        'integer': 'número inteiro',
        'float': 'número decimal',
        'decimal': 'número decimal',
        'double': 'número decimal',
        'boolean': 'valor booleano (verdadeiro/falso)',
        'bool': 'valor booleano (sim/não)',
        'date': 'data',
        'datetime': 'data e hora',
        'timestamp': 'registro de data e hora',
        'time': 'hora',
        'email': 'endereço de e-mail',
        'url': 'endereço URL',
        'phone': 'número de telefone',
        'cpf': 'CPF',
        'cnpj': 'CNPJ',
        'cep': 'CEP',
        'json': 'objeto JSON',
        'array': 'lista/array',
        'file': 'arquivo',
        'image': 'imagem',
        'password': 'senha'
    }
    
    def __init__(self):
        self.campos = []
    
    def adicionar_campo(self, nome: str, tipo: str, obrigatorio: bool = False,
                       tamanho_min: Optional[int] = None, tamanho_max: Optional[int] = None,
                       valor_min: Optional[float] = None, valor_max: Optional[float] = None,
                       padrao: Optional[str] = None, unico: bool = False,
                       descricao_customizada: Optional[str] = None,
                       opcoes: Optional[List[str]] = None) -> Dict:
        """
        Adiciona um campo e gera seu descritivo automaticamente
        
        Args:
            nome: Nome do campo
            tipo: Tipo do campo (string, int, email, etc.)
            obrigatorio: Se o campo é obrigatório
            tamanho_min: Tamanho mínimo (para strings)
            tamanho_max: Tamanho máximo (para strings)
            valor_min: Valor mínimo (para números)
            valor_max: Valor máximo (para números)
            padrao: Valor padrão
            unico: Se o valor deve ser único
            descricao_customizada: Descrição adicional customizada
            opcoes: Lista de opções válidas (para campos de seleção)
        
        Returns:
            Dicionário com informações do campo e descritivo gerado
        """
        campo = {
            'nome': nome,
            'tipo': tipo,
            'obrigatorio': obrigatorio,
            'tamanho_min': tamanho_min,
            'tamanho_max': tamanho_max,
            'valor_min': valor_min,
            'valor_max': valor_max,
            'padrao': padrao,
            'unico': unico,
            'descricao_customizada': descricao_customizada,
            'opcoes': opcoes
        }
        
        campo['descritivo'] = self._gerar_descritivo(campo)
        self.campos.append(campo)
        return campo
    
    def _gerar_descritivo(self, campo: Dict) -> str:
        """Gera o descritivo completo do campo"""
        partes = []
        
        # Nome formatado
        nome_formatado = campo['nome'].replace('_', ' ').title()
        
        # Tipo do campo
        tipo_desc = self.TIPOS_DESCRICAO.get(campo['tipo'].lower(), campo['tipo'])
        partes.append(f"**{nome_formatado}** é um campo do tipo {tipo_desc} ")
        
        # Obrigatoriedade
        if campo['obrigatorio']:
            partes.append("de preenchimento **obrigatório** ")
        else:
            partes.append("de preenchimento **opcional** ")
        
        # Restrições de tamanho para strings
        if campo['tamanho_min'] or campo['tamanho_max']:
            restricoes = []
            if campo['tamanho_min']:
                restricoes.append(f"mínimo de {campo['tamanho_min']} caracteres")
            if campo['tamanho_max']:
                restricoes.append(f"máximo de {campo['tamanho_max']} caracteres")
            partes.append(f", com {' e '.join(restricoes)}")
        
        # Restrições de valor para números
        if campo['valor_min'] is not None or campo['valor_max'] is not None:
            restricoes = []
            if campo['valor_min'] is not None:
                restricoes.append(f"valor mínimo de {campo['valor_min']}")
            if campo['valor_max'] is not None:
                restricoes.append(f"valor máximo de {campo['valor_max']}")
            partes.append(f", com {' e '.join(restricoes)}")
        
        # Opções válidas
        if campo['opcoes']:
            opcoes_str = ', '.join([f'"{op}"' for op in campo['opcoes']])
            partes.append(f". As opções válidas são: {opcoes_str}")
        else:
            partes.append(".")
        
        # Unicidade
        if campo['unico']:
            partes.append(f" O valor deste campo deve ser **único** no sistema, não podendo haver duplicatas.")
        
        # Valor padrão
        if campo['padrao']:
            partes.append(f" Caso não seja informado, o valor padrão será: **{campo['padrao']}**.")
        
        # Descrição customizada
        if campo['descricao_customizada']:
            partes.append(f" {campo['descricao_customizada']}")
        
        return ''.join(partes)
    
    def gerar_relatorio_markdown(self, titulo: str = "Documentação de Campos") -> str:
        """Gera um relatório completo em Markdown com todos os campos"""
        linhas = [
            f"# {titulo}\n",
            f"*Gerado automaticamente em {self._obter_data_atual()}*\n",
            "---\n"
        ]
        
        for i, campo in enumerate(self.campos, 1):
            linhas.append(f"\n## {i}. {campo['nome']}\n")
            linhas.append(f"{campo['descritivo']}\n")
            
            # Tabela de especificações técnicas
            linhas.append("\n### Especificações Técnicas\n")
            linhas.append("| Propriedade | Valor |")
            linhas.append("|-------------|-------|")
            linhas.append(f"| **Nome do Campo** | `{campo['nome']}` |")
            linhas.append(f"| **Tipo de Dados** | `{campo['tipo']}` |")
            linhas.append(f"| **Obrigatório** | {'Sim' if campo['obrigatorio'] else 'Não'} |")
            
            if campo['tamanho_min']:
                linhas.append(f"| **Tamanho Mínimo** | {campo['tamanho_min']} caracteres |")
            if campo['tamanho_max']:
                linhas.append(f"| **Tamanho Máximo** | {campo['tamanho_max']} caracteres |")
            if campo['valor_min'] is not None:
                linhas.append(f"| **Valor Mínimo** | {campo['valor_min']} |")
            if campo['valor_max'] is not None:
                linhas.append(f"| **Valor Máximo** | {campo['valor_max']} |")
            if campo['padrao']:
                linhas.append(f"| **Valor Padrão** | `{campo['padrao']}` |")
            if campo['unico']:
                linhas.append(f"| **Único** | Sim |")
            if campo['opcoes']:
                linhas.append(f"| **Opções Válidas** | {', '.join([f'`{op}`' for op in campo['opcoes']])} |")
            
            linhas.append("")
        
        return '\n'.join(linhas)
    
    def gerar_json(self) -> str:
        """Exporta os campos em formato JSON"""
        return json.dumps(self.campos, indent=2, ensure_ascii=False)
    
    def _obter_data_atual(self) -> str:
        """Retorna a data atual formatada"""
        from datetime import datetime
        return datetime.now().strftime("%d/%m/%Y às %H:%M")


def exemplo_uso():
    """Exemplo de uso do gerador de descritivos"""
    print("=" * 70)
    print("GERADOR AUTOMÁTICO DE DESCRITIVOS DE CAMPOS")
    print("=" * 70)
    print()
    
    gerador = GeradorDescritivos()
    
    # Exemplo 1: Campo de nome
    gerador.adicionar_campo(
        nome="nome_completo",
        tipo="string",
        obrigatorio=True,
        tamanho_min=3,
        tamanho_max=100,
        descricao_customizada="Este campo armazena o nome completo do usuário para identificação no sistema."
    )
    
    # Exemplo 2: Campo de email
    gerador.adicionar_campo(
        nome="email",
        tipo="email",
        obrigatorio=True,
        unico=True,
        descricao_customizada="Utilizado para login e comunicações oficiais."
    )
    
    # Exemplo 3: Campo de idade
    gerador.adicionar_campo(
        nome="idade",
        tipo="integer",
        obrigatorio=True,
        valor_min=18,
        valor_max=120,
        descricao_customizada="A idade mínima permitida é 18 anos."
    )
    
    # Exemplo 4: Campo de CPF
    gerador.adicionar_campo(
        nome="cpf",
        tipo="cpf",
        obrigatorio=True,
        unico=True,
        tamanho_min=11,
        tamanho_max=14,
        descricao_customizada="Deve ser informado apenas números ou no formato XXX.XXX.XXX-XX."
    )
    
    # Exemplo 5: Campo de status
    gerador.adicionar_campo(
        nome="status",
        tipo="string",
        obrigatorio=True,
        padrao="ativo",
        opcoes=["ativo", "inativo", "pendente", "bloqueado"],
        descricao_customizada="Define a situação atual do cadastro no sistema."
    )
    
    # Exemplo 6: Campo de salário
    gerador.adicionar_campo(
        nome="salario",
        tipo="decimal",
        obrigatorio=False,
        valor_min=0.01,
        valor_max=999999.99,
        descricao_customizada="Valor em reais (R$)."
    )
    
    # Gerar relatório
    relatorio = gerador.gerar_relatorio_markdown("Documentação de Campos do Sistema")
    
    # Salvar em arquivo
    with open('/home/ubuntu/descritivos_campos.md', 'w', encoding='utf-8') as f:
        f.write(relatorio)
    
    print("✓ Relatório gerado com sucesso!")
    print("✓ Arquivo salvo: /home/ubuntu/descritivos_campos.md")
    print()
    print("Campos processados:")
    for campo in gerador.campos:
        print(f"  • {campo['nome']}")
    print()
    
    # Também salvar JSON
    with open('/home/ubuntu/descritivos_campos.json', 'w', encoding='utf-8') as f:
        f.write(gerador.gerar_json())
    print("✓ Arquivo JSON salvo: /home/ubuntu/descritivos_campos.json")
    print()


if __name__ == "__main__":
    exemplo_uso()
