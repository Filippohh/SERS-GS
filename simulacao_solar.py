import pandas as pd
import matplotlib.pyplot as plt

irr = pd.read_csv("dados_irradiance.csv", parse_dates=["date"])

system_kwp = 5.0
eff = 0.18
area_per_kwp = 6.5
area = system_kwp * area_per_kwp

irr["geracao_kwh"] = irr["irradiance_kwh_m2"] * area * eff

print("\n=== RESUMO DA GERAÇÃO ===")
print("Geração anual estimada (kWh):", irr["geracao_kwh"].sum())

plt.plot(irr["date"], irr["geracao_kwh"])
plt.title("Geração diária estimada (kWh)")
plt.xlabel("Data")
plt.ylabel("kWh")
plt.tight_layout()
plt.savefig("geracao_diaria.png")
plt.close()

print("Gráfico salvo como geracao_diaria.png")