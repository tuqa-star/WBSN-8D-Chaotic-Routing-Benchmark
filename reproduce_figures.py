import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create output directory for figures
os.makedirs("figures", exist_ok=True)

# ==========================================
# 1. OFFICIAL BENCHMARK DATA (TABLE III & IV)
# ==========================================
protocols = ["Proposed", "M-ATTEMPT", "ATTEMPT", "Swarm", "DQN", "EEHCHR", "EOCGS"]

data_table3 = {
    "Protocol": protocols,
    "Lifetime_Rounds": [3150, 2650, 2500, 2800, 2800, 2720, 2750],
    "Lifetime_CI95": [47, 50, 48, 52, 50, 49, 50],
    "FND": [1850, 1420, 1350, 1580, 1620, 1510, 1540],
    "HND": [2780, 2180, 2050, 2410, 2350, 2290, 2320],
    "LND": [3450, 3000, 2710, 3040, 2980, 2950, 2980],
    "Energy_J_per_node": [0.28, 0.41, 0.46, 0.35, 0.33, 0.37, 0.36],
    "Energy_CI95": [0.012, 0.018, 0.020, 0.015, 0.014, 0.016, 0.015],
    "PDR_Percent": [96.5, 91.2, 89.8, 93.1, 92.5, 91.8, 92.0],
    "PDR_CI95": [0.8, 1.2, 1.5, 1.0, 1.1, 1.2, 1.2],
    "Delay_ms": [41.3, 58.7, 62.1, 49.2, 47.5, 52.4, 51.1],
    "Delay_CI95": [1.5, 2.3, 2.6, 1.9, 1.8, 2.1, 2.0],
    "Throughput_Kbps": [156.2, 128.7, 121.5, 141.7, 136.4, 132.5, 134.8],
    "Throughput_CI95": [3.5, 4.1, 4.5, 3.8, 4.0, 4.2, 3.9],
    "Overhead_Percent": [4.2, 7.8, 8.5, 5.9, 6.1, 6.8, 6.5],
    "Overhead_CI95": [0.3, 0.5, 0.6, 0.4, 0.4, 0.5, 0.4],
}

df_main = pd.DataFrame(data_table3)
df_main.to_csv("benchmark_results.csv", index=False)

# Table V: Ablation Study
ablation_data = {
    "Configuration": ["8D-CSS only", "TRA only", "CBRP only", "8D-CSS + TRA", "Full Framework"],
    "Lifetime_Rounds": [2680, 2850, 2720, 3020, 3150],
    "PDR_Percent": [92.1, 93.8, 91.5, 95.1, 96.5],
    "Energy_J": [0.36, 0.32, 0.38, 0.30, 0.28],
    "Delay_ms": [53.2, 48.5, 51.7, 44.8, 41.3],
}
pd.DataFrame(ablation_data).to_csv("ablation_study.csv", index=False)

# ==========================================
# 2. BAR CHARTS (FIGS. 2 - 7)
# ==========================================
colors = ["#1f4e79", "#c0392b", "#e67e22", "#27ae60", "#8e44ad", "#2980b9", "#d4ac0d"]
hatches = ["//", "", "\\\\", "xx", "..", "--", "++"]

def plot_bar_metric(values, errors, ylabel, filename, ylim=None, fmt="{:.1f}"):
    plt.figure(figsize=(8, 5))
    bars = plt.bar(
        protocols, values, yerr=errors, capsize=5,
        color=colors, edgecolor="black", linewidth=1.1
    )
    for bar, h in zip(bars, hatches):
        bar.set_hatch(h)
    for bar, val, err in zip(bars, values, errors):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            val + err + (max(values) * 0.02),
            fmt.format(val),
            ha="center", va="bottom", fontsize=9, fontweight="bold"
        )
    plt.ylabel(ylabel, fontsize=11, fontweight="bold")
    plt.xticks(rotation=25, ha="right", fontsize=10)
    if ylim:
        plt.ylim(ylim)
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(f"figures/{filename}", dpi=300, bbox_inches="tight")
    plt.close()

plot_bar_metric(df_main["Lifetime_Rounds"], df_main["Lifetime_CI95"], "Network Lifetime (rounds)", "Fig2_Network_Lifetime.png", (0, 3600), "{:.0f}")
plot_bar_metric(df_main["Energy_J_per_node"], df_main["Energy_CI95"], "Avg. Energy Consumption (J/node)", "Fig3_Energy_Consumption.png", (0, 0.55), "{:.2f}")
plot_bar_metric(df_main["PDR_Percent"], df_main["PDR_CI95"], "Packet Delivery Ratio (%)", "Fig4_PDR.png", (85, 102), "{:.1f}")
plot_bar_metric(df_main["Delay_ms"], df_main["Delay_CI95"], "End-to-End Delay (ms)", "Fig5_Delay.png", (0, 75), "{:.1f}")
plot_bar_metric(df_main["Throughput_Kbps"], df_main["Throughput_CI95"], "Network Throughput (Kbps)", "Fig6_Throughput.png", (0, 185), "{:.1f}")
plot_bar_metric(df_main["Overhead_Percent"], df_main["Overhead_CI95"], "Routing Overhead (%)", "Fig7_Overhead.png", (0, 11), "{:.1f}")

# ==========================================
# 3. ALIVE NODES OVER ROUNDS (FIG. 8 - TABLE IV)
# ==========================================
rounds = [0, 1000, 2000, 3000, 3450]
alive_curves = {
    "Proposed": [100, 100, 94, 52, 0],
    "M-ATTEMPT": [100, 100, 78, 28, 0],
    "ATTEMPT": [100, 100, 71, 12, 0],
    "Swarm": [100, 100, 85, 35, 0],
    "DQN": [100, 100, 82, 30, 0],
    "EEHCHR": [100, 100, 80, 25, 0],
    "EOCGS": [100, 100, 82, 27, 0],
}
markers = ["o", "s", "^", "D", "*", "v", "P"]

plt.figure(figsize=(8, 5))
for (name, vals), col, m in zip(alive_curves.items(), colors, markers):
    plt.plot(rounds, vals, label=name, color=col, marker=m, linewidth=2, markersize=6)
plt.xlabel("Simulation Rounds", fontsize=11, fontweight="bold")
plt.ylabel("Number of Alive Nodes", fontsize=11, fontweight="bold")
plt.xlim(0, 3550)
plt.ylim(0, 105)
plt.legend(ncol=2, fontsize=9)
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig("figures/Fig8_Alive_Nodes.png", dpi=300, bbox_inches="tight")
plt.close()

# ==========================================
# 4. SCALABILITY ANALYSIS (FIG. 9)
# ==========================================
nodes_density = [50, 100, 150, 200]
scalability = {
    "Proposed": [2850, 3150, 3050, 2910],
    "M-ATTEMPT": [2450, 2650, 2380, 2150],
    "ATTEMPT": [2350, 2500, 2200, 1950],
    "Swarm": [2600, 2800, 2550, 2350],
    "DQN": [2580, 2800, 2520, 2300],
}

plt.figure(figsize=(8, 5))
for (name, vals), col, m in zip(scalability.items(), colors[:5], markers[:5]):
    plt.plot(nodes_density, vals, label=name, color=col, marker=m, linewidth=2.2, markersize=7)
plt.xlabel("Number of Sensor Nodes", fontsize=11, fontweight="bold")
plt.ylabel("Network Lifetime (rounds)", fontsize=11, fontweight="bold")
plt.xticks(nodes_density)
plt.ylim(1800, 3400)
plt.legend(fontsize=9)
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig("figures/Fig9_Scalability.png", dpi=300, bbox_inches="tight")
plt.close()

print("Done! Generated benchmark_results.csv, ablation_study.csv, and Figs 2-9 in /figures.")
