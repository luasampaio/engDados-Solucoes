#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Descritivos Expandidos para Tabelas de Banco de Dados
Transforma descrições básicas em documentação completa e profissional
"""

import json
from datetime import datetime
from typing import Dict, List


class GeradorDescritivosTabelas:
    """Gera descritivos expandidos e profissionais para tabelas de banco de dados"""
    
    def __init__(self):
        self.tabelas = []
    
    def carregar_tabelas_json(self, caminho_arquivo: str):
        """Carrega dados das tabelas de um arquivo JSON"""
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            self.tabelas = json.load(f)
    
    def adicionar_tabela(self, nome_logico: str, descricao_basica: str):
        """Adiciona uma tabela manualmente"""
        self.tabelas.append({
            'nome_logico': nome_logico,
            'descricao_basica': descricao_basica
        })
    
    def _gerar_nome_amigavel(self, nome_logico: str) -> str:
        """Converte nome lógico em nome amigável"""
        # Remove prefixos comuns
        nome = nome_logico.replace('DADOS_', '').replace('TB_', '').replace('TBL_', '')
        # Substitui underscores por espaços e capitaliza
        nome = nome.replace('_', ' ').title()
        return nome
    
    def _inferir_contexto(self, nome_logico: str, descricao: str) -> Dict:
        """Infere informações contextuais sobre a tabela"""
        contexto = {
            'tipo_entidade': 'dados',
            'dominio': 'geral',
            'relacionamentos': [],
            'importancia': 'média'
        }
        
        nome_lower = nome_logico.lower()
        desc_lower = descricao.lower()
        
        # Identificar tipo de entidade
        if 'dependente' in nome_lower or 'dependente' in desc_lower:
            contexto['tipo_entidade'] = 'entidade dependente'
            contexto['relacionamentos'].append('relacionada a titular ou beneficiário principal')
        
        if 'endereco' in nome_lower or 'endereço' in desc_lower:
            contexto['tipo_entidade'] = 'dados de localização'
            contexto['relacionamentos'].append('pode estar vinculada a pessoas, empresas ou estabelecimentos')
        
        if 'faturamento' in nome_lower or 'fatura' in desc_lower:
            contexto['tipo_entidade'] = 'transação financeira'
            contexto['dominio'] = 'financeiro'
            contexto['importancia'] = 'alta'
            contexto['relacionamentos'].append('relacionada a apólices e seguros')
        
        if 'medico' in nome_lower or 'médico' in desc_lower:
            contexto['tipo_entidade'] = 'cadastro de profissional'
            contexto['dominio'] = 'saúde'
            contexto['relacionamentos'].append('referenciado em atendimentos e procedimentos')
        
        if 'apolice' in desc_lower or 'seguro' in desc_lower:
            contexto['dominio'] = 'seguros'
            contexto['importancia'] = 'alta'
        
        return contexto
    
    def _gerar_descritivo_expandido(self, tabela: Dict) -> str:
        """Gera descritivo expandido e profissional da tabela"""
        nome_logico = tabela['nome_logico']
        descricao_basica = tabela['descricao_basica']
        nome_amigavel = self._gerar_nome_amigavel(nome_logico)
        contexto = self._inferir_contexto(nome_logico, descricao_basica)
        
        # Construir descritivo expandido
        partes = []
        
        # Introdução
        partes.append(f"A tabela **{nome_logico}** ({nome_amigavel}) é responsável por armazenar {descricao_basica.lower()}")
        
        # Contexto e domínio
        if contexto['dominio'] != 'geral':
            partes.append(f" Esta tabela faz parte do domínio **{contexto['dominio']}** do sistema")
            if contexto['importancia'] == 'alta':
                partes.append(" e possui **importância crítica** para as operações do negócio")
            partes.append(".")
        else:
            partes.append(".")
        
        # Tipo de entidade
        if contexto['tipo_entidade'] != 'dados':
            partes.append(f" Trata-se de uma tabela de **{contexto['tipo_entidade']}**")
            partes.append(".")
        
        # Relacionamentos
        if contexto['relacionamentos']:
            partes.append(f" Esta tabela está {contexto['relacionamentos'][0]}")
            if len(contexto['relacionamentos']) > 1:
                partes.append(f", além de {', '.join(contexto['relacionamentos'][1:])}")
            partes.append(".")
        
        return ''.join(partes)
    
    def _gerar_finalidade_uso(self, tabela: Dict) -> str:
        """Gera descrição de finalidade e uso da tabela"""
        nome_lower = tabela['nome_logico'].lower()
        desc_lower = tabela['descricao_basica'].lower()
        
        finalidades = []
        
        if 'dependente' in nome_lower:
            finalidades.append("Cadastro e gestão de dependentes vinculados a titulares de planos ou seguros")
            finalidades.append("Controle de elegibilidade e direitos dos dependentes")
            finalidades.append("Geração de relatórios familiares e análises demográficas")
        
        elif 'endereco' in nome_lower:
            finalidades.append("Registro de endereços para correspondências e comunicações oficiais")
            finalidades.append("Validação de localização geográfica para cobertura de serviços")
            finalidades.append("Análises de distribuição geográfica e regionalização")
        
        elif 'faturamento' in nome_lower:
            finalidades.append("Registro de todas as transações de faturamento de apólices e seguros")
            finalidades.append("Controle financeiro e conciliação de pagamentos")
            finalidades.append("Base para relatórios gerenciais, auditorias e análises de receita")
            finalidades.append("Suporte a processos de cobrança e gestão de inadimplência")
        
        elif 'medico' in nome_lower:
            finalidades.append("Cadastro completo de médicos e profissionais de saúde credenciados")
            finalidades.append("Controle de especialidades, credenciamentos e vínculos")
            finalidades.append("Suporte à rede referenciada e direcionamento de atendimentos")
            finalidades.append("Base para análises de utilização e gestão da rede credenciada")
        
        else:
            finalidades.append("Armazenamento estruturado de informações essenciais ao negócio")
            finalidades.append("Suporte a operações transacionais e consultas do sistema")
            finalidades.append("Base para relatórios e análises gerenciais")
        
        return finalidades
    
    def _gerar_consideracoes_tecnicas(self, tabela: Dict) -> List[str]:
        """Gera considerações técnicas sobre a tabela"""
        consideracoes = []
        nome_lower = tabela['nome_logico'].lower()
        desc_lower = tabela['descricao_basica'].lower()
        
        # Considerações de segurança
        if any(palavra in nome_lower or palavra in desc_lower for palavra in ['faturamento', 'financeiro', 'pagamento']):
            consideracoes.append("**Segurança**: Esta tabela contém dados financeiros sensíveis e deve ter controles de acesso rigorosos e auditoria habilitada")
        
        if 'medico' in nome_lower or 'profissional' in desc_lower:
            consideracoes.append("**Privacidade**: Dados de profissionais de saúde estão sujeitos à LGPD e regulamentações do setor de saúde")
        
        if 'dependente' in nome_lower:
            consideracoes.append("**Privacidade**: Contém dados pessoais protegidos pela LGPD, especialmente quando envolvem menores de idade")
        
        # Considerações de performance
        if 'faturamento' in nome_lower:
            consideracoes.append("**Performance**: Tabela com alto volume de transações, recomenda-se particionamento por período e índices otimizados")
            consideracoes.append("**Retenção**: Definir política de arquivamento para dados históricos conforme requisitos legais e fiscais")
        
        # Considerações de integridade
        if 'endereco' in nome_lower:
            consideracoes.append("**Integridade**: Implementar validações de CEP, normalização de endereços e integração com APIs de geolocalização")
        
        if any(palavra in nome_lower for palavra in ['dependente', 'medico']):
            consideracoes.append("**Integridade Referencial**: Manter chaves estrangeiras e constraints para garantir consistência dos relacionamentos")
        
        return consideracoes
    
    def gerar_relatorio_completo(self, titulo: str = "Documentação de Tabelas do Banco de Dados") -> str:
        """Gera relatório completo em Markdown"""
        linhas = [
            f"# {titulo}\n",
            f"*Documentação gerada automaticamente em {self._obter_data_atual()}*\n",
            "---\n",
            "\n## Sumário Executivo\n",
            f"Este documento apresenta a documentação detalhada de **{len(self.tabelas)} tabelas** do banco de dados, ",
            "incluindo descritivos expandidos, finalidades de uso e considerações técnicas importantes.\n",
            "\n---\n"
        ]
        
        # Índice
        linhas.append("\n## Índice de Tabelas\n")
        for i, tabela in enumerate(self.tabelas, 1):
            nome_amigavel = self._gerar_nome_amigavel(tabela['nome_logico'])
            linhas.append(f"{i}. [{tabela['nome_logico']}](#{tabela['nome_logico'].lower()}) - {nome_amigavel}\n")
        
        linhas.append("\n---\n")
        
        # Detalhamento de cada tabela
        for i, tabela in enumerate(self.tabelas, 1):
            nome_logico = tabela['nome_logico']
            nome_amigavel = self._gerar_nome_amigavel(nome_logico)
            
            linhas.append(f"\n## {i}. {nome_logico}\n")
            linhas.append(f"### {nome_amigavel}\n")
            
            # Informações básicas
            linhas.append("\n#### 📋 Informações Básicas\n")
            linhas.append(f"**Nome Lógico:** `{nome_logico}`\n\n")
            linhas.append(f"**Descrição Original:** {tabela['descricao_basica']}\n")
            
            # Descritivo expandido
            linhas.append("\n#### 📖 Descritivo Detalhado\n")
            descritivo = self._gerar_descritivo_expandido(tabela)
            linhas.append(f"{descritivo}\n")
            
            # Finalidade e uso
            linhas.append("\n#### 🎯 Finalidade e Uso\n")
            finalidades = self._gerar_finalidade_uso(tabela)
            for finalidade in finalidades:
                linhas.append(f"- {finalidade}\n")
            
            # Considerações técnicas
            consideracoes = self._gerar_consideracoes_tecnicas(tabela)
            if consideracoes:
                linhas.append("\n#### ⚙️ Considerações Técnicas\n")
                for consideracao in consideracoes:
                    linhas.append(f"- {consideracao}\n")
            
            # Contexto adicional
            contexto = self._inferir_contexto(nome_logico, tabela['descricao_basica'])
            linhas.append("\n#### 🔗 Contexto no Sistema\n")
            linhas.append(f"- **Domínio:** {contexto['dominio'].title()}\n")
            linhas.append(f"- **Tipo de Entidade:** {contexto['tipo_entidade'].title()}\n")
            linhas.append(f"- **Importância:** {contexto['importancia'].title()}\n")
            
            if i < len(self.tabelas):
                linhas.append("\n---\n")
        
        # Rodapé
        linhas.append("\n---\n")
        linhas.append("\n## Notas Finais\n")
        linhas.append("Esta documentação foi gerada automaticamente com base nas informações fornecidas. ")
        linhas.append("Recomenda-se revisar e complementar com detalhes específicos sobre colunas, índices, ")
        linhas.append("relacionamentos e regras de negócio particulares de cada tabela.\n")
        
        return ''.join(linhas)
    
    def _obter_data_atual(self) -> str:
        """Retorna a data atual formatada"""
        return datetime.now().strftime("%d/%m/%Y às %H:%M")


def main():
    """Função principal para processar as tabelas"""
    print("=" * 80)
    print("GERADOR DE DESCRITIVOS EXPANDIDOS PARA TABELAS DE BANCO DE DADOS")
    print("=" * 80)
    print()
    
    # Criar instância do gerador
    gerador = GeradorDescritivosTabelas()
    
    # Carregar dados das tabelas
    print("📂 Carregando dados das tabelas...")
    gerador.carregar_tabelas_json('/home/ubuntu/tabelas_dados.json')
    print(f"✓ {len(gerador.tabelas)} tabelas carregadas com sucesso!\n")
    
    # Listar tabelas processadas
    print("📊 Tabelas que serão documentadas:")
    for i, tabela in enumerate(gerador.tabelas, 1):
        print(f"   {i}. {tabela['nome_logico']}")
    print()
    
    # Gerar relatório completo
    print("📝 Gerando documentação completa...")
    relatorio = gerador.gerar_relatorio_completo(
        "Documentação Detalhada de Tabelas - Bradesco Saúde"
    )
    
    # Salvar em arquivo
    caminho_saida = '/home/ubuntu/descritivos_tabelas_completo.md'
    with open(caminho_saida, 'w', encoding='utf-8') as f:
        f.write(relatorio)
    
    print(f"✓ Documentação gerada com sucesso!")
    print(f"✓ Arquivo salvo: {caminho_saida}")
    print()
    print("=" * 80)
    print("PROCESSO CONCLUÍDO COM SUCESSO!")
    print("=" * 80)


if __name__ == "__main__":
    main()
