---
name: genpark-personal-agent-renal-calcium-creatinine-clearance-ratio-cccr-skill
version: 1.0.0
description: Calculates Calcium-to-Creatinine Clearance Ratio (CCCR) and Fractional Excretion of Calcium (FECa%) to differentiate Familial Hypocalciuric Hypercalcemia (FHH) from Primary Hyperparathyroidism (PHPT).
authors:
  - GenPark Ecosystem
tags:
  - personal-agent
  - nephrology
  - endocrinology
  - calcium
  - cccr
  - hypercalcemia
  - zero-dependency
---

# Renal Calcium-to-Creatinine Clearance Ratio (CCCR) Skill

## Mathematical Formulation

Calcium-to-Creatinine Clearance Ratio:

$$\text{CCCR} = \frac{C_{\text{Ca}}}{C_{\text{Cr}}} = \frac{U_{\text{Ca}} \times P_{\text{Cr}}}{P_{\text{Ca}} \times U_{\text{Cr}}}$$

Fractional Excretion of Calcium:

$$\text{FE}_{\text{Ca}} \, (\%) = \text{CCCR} \times 100$$

Where $U_{\text{Ca}}$, $P_{\text{Cr}}$, $P_{\text{Ca}}$, and $U_{\text{Cr}}$ are measured in matching mass units ($\text{mg/dL}$) or molar concentrations ($\text{mmol/L}$).

## Diagnostic Interpretation in Hypercalcemia
- **$\text{CCCR} < 0.01$ ($< 1\%$)**: Familial Hypocalciuric Hypercalcemia (FHH) — parathyroid surgery contraindicated.
- **$0.01 \le \text{CCCR} \le 0.02$ ($1\% - 2\%$)**: Indeterminate Gray Zone — check vitamin D repletion; consider CaSR gene sequencing.
- **$\text{CCCR} > 0.02$ ($> 2\%$)**: Primary Hyperparathyroidism (PHPT) — hypercalciuria; parathyroidectomy is curative.
