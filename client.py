"""
Renal Calcium-to-Creatinine Clearance Ratio (CCCR) Client.
Zero-mock pure Python standard library implementation.
Calculates Calcium-to-Creatinine Clearance Ratio (CCCR), Fractional Excretion of Calcium (FECa%),
and differentiates Familial Hypocalciuric Hypercalcemia (FHH) from Primary Hyperparathyroidism (PHPT).
"""

import math
from typing import Dict, Any, Optional


class CalciumCreatinineClearanceRatioClient:
    """
    Evaluates renal calcium handling and calcium-sensing receptor (CaSR) function:
    CCCR = (U_Ca * P_Cr) / (P_Ca * U_Cr)
    Where:
    - U_Ca: Urine calcium (mg/dL)
    - P_Cr: Serum creatinine (mg/dL)
    - P_Ca: Total serum calcium (mg/dL)
    - U_Cr: Urine creatinine (mg/dL)
    FECa% = CCCR * 100.0
    """

    def __init__(self):
        pass

    def evaluate_cccr(
        self,
        urine_calcium_mg_dl: float,
        serum_creatinine_mg_dl: float,
        serum_calcium_mg_dl: float,
        urine_creatinine_mg_dl: float,
        serum_pth_pg_ml: Optional[float] = None,
        serum_albumin_g_dl: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Calculates CCCR ratio and hypercalcemia differential.
        urine_calcium_mg_dl: spot or 24-hr urine calcium (mg/dL).
        serum_creatinine_mg_dl: serum creatinine (mg/dL).
        serum_calcium_mg_dl: serum total calcium (mg/dL).
        urine_creatinine_mg_dl: urine creatinine (mg/dL).
        serum_pth_pg_ml: parathyroid hormone in pg/mL (optional).
        serum_albumin_g_dl: serum albumin in g/dL for calcium correction (optional).
        """
        if urine_calcium_mg_dl <= 0 or serum_creatinine_mg_dl <= 0 or serum_calcium_mg_dl <= 0 or urine_creatinine_mg_dl <= 0:
            raise ValueError("All biochemical concentrations must be strictly positive.")

        # Albumin-corrected calcium if albumin provided
        corrected_serum_ca = serum_calcium_mg_dl
        if serum_albumin_g_dl is not None:
            if serum_albumin_g_dl < 4.0:
                corrected_serum_ca = serum_calcium_mg_dl + 0.8 * (4.0 - serum_albumin_g_dl)

        # CCCR calculation
        cccr = (urine_calcium_mg_dl * serum_creatinine_mg_dl) / (corrected_serum_ca * urine_creatinine_mg_dl)
        feca_pct = cccr * 100.0

        # Clinical diagnostic stratification:
        # CCCR < 0.01 (< 1.0%): Familial Hypocalciuric Hypercalcemia (FHH) highly likely
        # CCCR 0.01 - 0.02 (1.0% - 2.0%): Diagnostic Gray Zone / Indeterminate
        # CCCR > 0.02 (> 2.0%): Primary Hyperparathyroidism (PHPT) highly likely
        if cccr < 0.01:
            differential_diagnosis = "Familial Hypocalciuric Hypercalcemia (FHH) Suspected"
            clinical_recommendation = "Low renal calcium excretion despite hypercalcemia. Highly suspicious for inactivating CaSR gene mutation. Parathyroidectomy contraindicated; test first-degree relatives and CASR sequencing."
        elif cccr <= 0.02:
            differential_diagnosis = "Indeterminate / Diagnostic Gray Zone (CCCR 0.01 - 0.02)"
            clinical_recommendation = "Overlap zone between mild PHPT and atypical FHH. Evaluate 25-OH vitamin D repletion (deficiency can falsely lower CCCR in PHPT) and consider genetic analysis."
        else:
            differential_diagnosis = "Primary Hyperparathyroidism (PHPT) Highly Probable"
            clinical_recommendation = "High calcium clearance ratio consistent with parathyroid adenoma or hyperplasia. Surgical neck exploration / parathyroidectomy indicated if symptomatic."

        return {
            "status": "success",
            "biochemical_parameters": {
                "serum_calcium_measured_mg_dl": round(serum_calcium_mg_dl, 2),
                "serum_calcium_corrected_mg_dl": round(corrected_serum_ca, 2),
                "serum_creatinine_mg_dl": round(serum_creatinine_mg_dl, 2),
                "urine_calcium_mg_dl": round(urine_calcium_mg_dl, 2),
                "urine_creatinine_mg_dl": round(urine_creatinine_mg_dl, 2),
                "serum_pth_pg_ml": serum_pth_pg_ml
            },
            "indices": {
                "calcium_creatinine_clearance_ratio_cccr": round(cccr, 4),
                "fractional_excretion_calcium_pct": round(feca_pct, 2)
            },
            "interpretation": {
                "differential_diagnosis": differential_diagnosis,
                "clinical_recommendation": clinical_recommendation
            }
        }
