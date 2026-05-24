"""FinOps API — margin summary and alerts."""

from __future__ import annotations

from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/api/finops/summary")
async def finops_summary_api():
    """JSON FinOps summary with margin and alerts."""
    from ....metrics.finops_summary import global_summary, margin_alerts, missions_summary

    return JSONResponse(
        {
            "global": global_summary(),
            "missions": missions_summary(),
            "alerts": margin_alerts(),
        }
    )
