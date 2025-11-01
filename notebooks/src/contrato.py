# e:\engDados-Solucoes\notebooks\src\contrato.py
import pandera.pandas as pa

schema_entrada = pa.DataFrameSchema({
    "val1": pa.Column(float, coerce=True, nullable=True),
    "val2": pa.Column(float, coerce=True, nullable=True),
})

schema_saida = pa.DataFrameSchema({
    "val1": pa.Column(float, nullable=True),
    "val2": pa.Column(float, nullable=True),
    "val3": pa.Column(float, nullable=True),  # pode ser NaN se zero/zero
})