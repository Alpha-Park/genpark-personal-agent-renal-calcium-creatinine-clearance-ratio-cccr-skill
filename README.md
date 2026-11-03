# Renal Calcium-to-Creatinine Clearance Ratio (CCCR) Personal Agent Skill

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python: 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen.svg)]()
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20JSON--RPC-orange.svg)]()
[![Production Ready](https://img.shields.io/badge/status-production--ready-green.svg)]()

Deterministic, zero-mock personal agent micro-skill for calculating Calcium-to-Creatinine Clearance Ratio (CCCR) and Fractional Excretion of Calcium (FECa%) to differentiate Familial Hypocalciuric Hypercalcemia (FHH) from Primary Hyperparathyroidism (PHPT).

## Architecture

```mermaid
flowchart TD
    A[Simultaneous Serum & Urine Ca and Cr] --> B[Correct Serum Ca for Albumin]
    B --> C[Compute CCCR = U_Ca*P_Cr / P_Ca*U_Cr]
    C --> D[Compute Fractional Excretion FECa%]
    D --> E[Stratify FHH < 0.01 vs PHPT > 0.02]
```

## Quickstart

```python
from client import CalciumCreatinineClearanceRatioClient

client = CalciumCreatinineClearanceRatioClient()
result = client.evaluate_cccr(
    urine_calcium_mg_dl=4.5,
    serum_creatinine_mg_dl=0.9,
    serum_calcium_mg_dl=10.8,
    urine_creatinine_mg_dl=95.0
)
print(result)
```

## License

Apache-2.0
