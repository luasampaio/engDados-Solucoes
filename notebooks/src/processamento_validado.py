# e:\engDados-Solucoes\notebooks\src\processamento_validado.py
import pandas as pd
from src.processamento import processar
from src.contrato import schema_entrada, schema_saida

def processar_validado(df: pd.DataFrame, ao_dividir_zero: str = "nan") -> pd.DataFrame:
    """
    Valida entrada (tipos/coerção), processa, e valida saída.
    """
    df_ok = schema_entrada.validate(df, lazy=True)
    out = processar(df_ok, ao_dividir_zero=ao_dividir_zero)
    return schema_saida.validate(out, lazy=True)
