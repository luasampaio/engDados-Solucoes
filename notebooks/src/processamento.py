
import numpy as np
import pandas as pd

def processar(df: pd.DataFrame, ao_dividir_zero: str = "nan") -> pd.DataFrame:
    if ao_dividir_zero not in {"nan", "inf", "raise"}:
        raise ValueError("ao_dividir_zero deve ser 'nan', 'inf' ou 'raise'.")
    d = df.copy()
    d["val1"] = pd.to_numeric(d["val1"], errors="coerce")
    d["val2"] = pd.to_numeric(d["val2"], errors="coerce")
    if ao_dividir_zero == "raise" and (d["val2"] == 0).any():
        raise ZeroDivisionError("val2 contém zero, impossível dividir.")
    d["val3"] = d["val1"] / d["val2"]
    if ao_dividir_zero == "nan":
        d.loc[~np.isfinite(d["val3"]), "val3"] = np.nan
    return d
