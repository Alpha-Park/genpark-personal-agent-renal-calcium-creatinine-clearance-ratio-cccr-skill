"""
MCP Server for Renal Calcium-to-Creatinine Clearance Ratio (CCCR) Skill.
Provides standard Model Context Protocol JSON-RPC tool endpoints.
"""

import sys
import json
from client import CalciumCreatinineClearanceRatioClient


def main():
    client = CalciumCreatinineClearanceRatioClient()

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except Exception:
            continue

        method = req.get("method")
        msg_id = req.get("id")

        if method == "tools/list":
            res = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "tools": [
                        {
                            "name": "evaluate_cccr",
                            "description": "Calculates Calcium-to-Creatinine Clearance Ratio (CCCR) and Fractional Excretion of Calcium (FECa%) to differentiate Familial Hypocalciuric Hypercalcemia (FHH) from Primary Hyperparathyroidism (PHPT).",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "urine_calcium_mg_dl": {
                                        "type": "number",
                                        "description": "Urine calcium concentration in mg/dL."
                                    },
                                    "serum_creatinine_mg_dl": {
                                        "type": "number",
                                        "description": "Serum creatinine concentration in mg/dL."
                                    },
                                    "serum_calcium_mg_dl": {
                                        "type": "number",
                                        "description": "Total serum calcium concentration in mg/dL."
                                    },
                                    "urine_creatinine_mg_dl": {
                                        "type": "number",
                                        "description": "Urine creatinine concentration in mg/dL."
                                    },
                                    "serum_pth_pg_ml": {
                                        "type": "number",
                                        "description": "Serum PTH in pg/mL (optional)."
                                    },
                                    "serum_albumin_g_dl": {
                                        "type": "number",
                                        "description": "Serum albumin in g/dL for calcium correction (optional)."
                                    }
                                },
                                "required": [
                                    "urine_calcium_mg_dl",
                                    "serum_creatinine_mg_dl",
                                    "serum_calcium_mg_dl",
                                    "urine_creatinine_mg_dl"
                                ]
                            }
                        }
                    ]
                }
            }
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

        elif method == "tools/call":
            params = req.get("params", {})
            name = params.get("name")
            args = params.get("arguments", {})

            if name == "evaluate_cccr":
                try:
                    out = client.evaluate_cccr(**args)
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "content": [{"type": "text", "text": json.dumps(out, indent=2)}]
                        }
                    }
                except Exception as e:
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "isError": True,
                        "error": {"code": -32000, "message": str(e)}
                    }
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()


if __name__ == "__main__":
    main()
