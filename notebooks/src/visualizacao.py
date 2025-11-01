
import matplotlib.pyplot as plt
import pandas as pd

def plot_histograma(df: pd.DataFrame, coluna: str, titulo: str | None = None, salvar_em: str | None = None):
    serie = pd.to_numeric(df[coluna], errors="coerce")
    plt.figure(); serie.plot(kind="hist", bins=20)
    plt.xlabel(coluna); plt.ylabel("Frequência"); plt.title(titulo or f"Histograma de {coluna}")
    if salvar_em: plt.savefig(salvar_em, bbox_inches="tight")
    plt.show()

def plot_series(df: pd.DataFrame, coluna: str, titulo: str | None = None, salvar_em: str | None = None):
    serie = pd.to_numeric(df[coluna], errors="coerce")
    plt.figure(); plt.plot(serie.index, serie.values)
    plt.xlabel("Índice"); plt.ylabel(coluna); plt.title(titulo or f"Série de {coluna}")
    if salvar_em: plt.savefig(salvar_em, bbox_inches="tight")
    plt.show()

def plot_boxplot(df: pd.DataFrame, colunas: list[str], titulo: str | None = None, salvar_em: str | None = None):
    dados = [pd.to_numeric(df[c], errors="coerce") for c in colunas]
    plt.figure(); plt.boxplot(dados, labels=colunas); plt.title(titulo or f"Boxplot: {', '.join(colunas)}")
    if salvar_em: plt.savefig(salvar_em, bbox_inches="tight")
    plt.show()
