# contracts.py

from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/contracts")
def get_contract_info(address: str = Query(...)):
    return {
        "address": address,
        "verified": True,
        "compiler_version": "v0.8.19+commit",
        "source_code_lines": 327,
        "owner": "0xAbc123...Def"
    }
