import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("dados_consumo.csv", parse_dates=["date"])

print("\n=== ESTATÍSTICAS GERAIS ===")
print(df.describe())

plt.plot(df["date"], df["consumo_kwh"])
plt.title("Consumo diário (kWh)")
plt.xlabel("Data")
plt.ylabel("kWh")
plt.tight_layout()
plt.savefig("consumo_diario.png")
plt.close()

print("\nGráfico salvo como consumo_diario.png")