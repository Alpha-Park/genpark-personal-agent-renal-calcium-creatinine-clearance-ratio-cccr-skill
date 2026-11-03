"""
Example usage of Renal Calcium-to-Creatinine Clearance Ratio (CCCR) Skill.
Demonstrates Familial Hypocalciuric Hypercalcemia (FHH) vs Primary Hyperparathyroidism (PHPT).
"""

import json
from client import CalciumCreatinineClearanceRatioClient


def main():
    print("=== Testing Renal CCCR Skill ===")
    client = CalciumCreatinineClearanceRatioClient()

    # 1. Asymptomatic hypercalcemic patient with FHH (Ca=10.8 mg/dL, Cr=0.9 mg/dL, U_Ca=4.5 mg/dL, U_Cr=95 mg/dL -> CCCR = (4.5*0.9)/(10.8*95) = 4.05/1026 = 0.0039 < 0.01)
    res_fhh = client.evaluate_cccr(
        urine_calcium_mg_dl=4.5,
        serum_creatinine_mg_dl=0.9,
        serum_calcium_mg_dl=10.8,
        urine_creatinine_mg_dl=95.0,
        serum_pth_pg_ml=55.0,
        serum_albumin_g_dl=4.1
    )
    print("\n[Case 1: Familial Hypocalciuric Hypercalcemia (FHH)]")
    print(json.dumps(res_fhh, indent=2))

    # 2. Patient with symptomatic parathyroid adenoma / PHPT (Ca=11.2 mg/dL, Cr=0.85 mg/dL, U_Ca=32.0 mg/dL, U_Cr=80 mg/dL -> CCCR = (32.0*0.85)/(11.2*80) = 27.2/896 = 0.0304 > 0.02)
    res_phpt = client.evaluate_cccr(
        urine_calcium_mg_dl=32.0,
        serum_creatinine_mg_dl=0.85,
        serum_calcium_mg_dl=11.2,
        urine_creatinine_mg_dl=80.0,
        serum_pth_pg_ml=118.0,
        serum_albumin_g_dl=4.0
    )
    print("\n[Case 2: Primary Hyperparathyroidism (PHPT)]")
    print(json.dumps(res_phpt, indent=2))

    # Assertions
    assert res_fhh["indices"]["calcium_creatinine_clearance_ratio_cccr"] < 0.01
    assert "FHH" in res_fhh["interpretation"]["differential_diagnosis"]
    assert res_phpt["indices"]["calcium_creatinine_clearance_ratio_cccr"] > 0.02
    assert "PHPT" in res_phpt["interpretation"]["differential_diagnosis"]
    print("\n[SUCCESS] Renal CCCR tests passed!")


if __name__ == "__main__":
    main()
