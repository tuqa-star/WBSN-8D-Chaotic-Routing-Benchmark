# WBSN-8D-Chaotic-Routing-Benchmark

Official benchmark dataset, ablation study results, and high-resolution figure reproduction scripts for the **IEEE Sensors Journal (2026)** article:

> **A Hybrid 8-D-Chaotic Search and Bioinspired Rejuvenation Framework for Energy-Efficient Routing in Wireless Body Sensor Networks**  
> *Tuqa K. Jebur, Lourdes Peñalver, Jaime Lloret, and Haider K. Hoomod*  
> IEEE Sensors Journal, Vol. 26, No. 11, pp. 17845–17852, June 2026.  
> **DOI:** [10.1109/JSEN.2026.3680837](https://doi.org/10.1109/JSEN.2026.3680837)

---

## Key Performance Highlights (8-D-CSS-TRA-CBRP)
Evaluated across 100 sensor nodes over a $250 \times 250\text{ m}$ area (0.5 J initial energy, 6,000 rounds, 30 independent runs):

| Metric | Proposed (8-D-CSS-TRA-CBRP) | Improvement over Baselines |
| :--- | :---: | :---: |
| **Network Lifetime** | **3,150 rounds** (FND: 1,850 \| HND: 2,780 \| LND: 3,450) | +18.9% to +26.0% |
| **Avg. Energy Consumption** | **0.28 J/node** | -31.7% to -39.1% |
| **Packet Delivery Ratio (PDR)** | **96.5%** | Highest among all baselines |
| **End-to-End Delay** | **41.3 ms** | -29.6% to -33.5% |
| **Network Throughput** | **156.2 kbps** | +10.2% to +21.4% |
| **Routing Overhead** | **4.2%** | Lowest control overhead |

---

## Repository Contents
* `benchmark_results.csv` — Complete performance comparison metrics (Table III & Table IV) with 95% confidence intervals against M-ATTEMPT, ATTEMPT, Swarm, DQN, EEHCHR, and EOCGS.
* `ablation_study.csv` — Component-wise ablation study results (Table V).
* `reproduce_figures.py` — Standalone Python script to regenerate all publication figures (Figs. 2–9) at 300 DPI.
* `figures/` — High-resolution (300 DPI) PNG plots of all comparative, lifetime, and scalability results.

---

## How to Cite
If you use these benchmark datasets or figures in your research, please cite our paper:

```bibtex
@ARTICLE{Jebur2026Hybrid8D,
  author={Jebur, Tuqa K. and Peñalver, Lourdes and Lloret, Jaime and Hoomod, Haider K.},
  journal={IEEE Sensors Journal}, 
  title={A Hybrid 8-D-Chaotic Search and Bioinspired Rejuvenation Framework for Energy-Efficient Routing in Wireless Body Sensor Networks}, 
  year={2026},
  volume={26},
  number={11},
  pages={17845-17852},
  doi={10.1109/JSEN.2026.3680837}
}# WBSN-8D-Chaotic-Routing-Benchmark
Benchmark simulation dataset for IEEE Sensors Journal 2026 paper
