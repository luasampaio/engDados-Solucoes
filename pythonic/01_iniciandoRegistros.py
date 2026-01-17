from datetime import datetime
import os

class FitnessTracker:
    def __init__(self):
        self.food_log = []
        self.activity_log = []

    def registrar_alimento(self, item, calorias, data=None):
        if data is None:
            data = datetime.now().strftime("%Y-%m-%d")

        with open("food.csv", "a", encoding="utf-8") as f:
            f.write(f"{data},{item},{calorias}\n")

        print(f"Alimento registrado: {item} ({calorias} kcal) em {data}")

    def registrar_atividade(self, atividade, calorias_gastas, data=None):
        if data is None:
            data = datetime.now().strftime("%Y-%m-%d")

        with open("activities.csv", "a", encoding="utf-8") as f:
            f.write(f"{data},{atividade},{calorias_gastas}\n")

        print(f"Atividade registrada: {atividade} ({calorias_gastas} kcal) em {data}")

    def resumo_do_dia(self, data):
        alimentos = []

        if os.path.exists("food.csv"):
            with open("food.csv", encoding="utf-8") as f:
                for linha in f:
                    partes = linha.strip().split(",")
                    if partes[0] == data:
                        alimentos.append(int(partes[2]))
        else:
            print("Arquivo food.csv não encontrado.")

        atividades = []

        if os.path.exists("activities.csv"):
            with open("activities.csv", encoding="utf-8") as f:
                for linha in f:
                    partes = linha.strip().split(",")
                    if partes[0] == data:
                        atividades.append(int(partes[2]))
        else:
            print("Arquivo activities.csv não encontrado.")

        total_consumido = sum(alimentos)
        total_gasto = sum(atividades)
        saldo = total_consumido - total_gasto

        print(f"\nResumo do dia {data}")
        print(f"  Calorias consumidas: {total_consumido} kcal")
        print(f"  Calorias gastas:     {total_gasto} kcal")
        print(f"  Saldo calórico:      {saldo} kcal")


# Execução
tracker = FitnessTracker()
tracker.registrar_alimento("Banana", 100)
tracker.registrar_atividade("Corrida", 300)
tracker.resumo_do_dia(datetime.now().strftime("%Y-%m-%d"))
