"""Human-in-the-loop gates for sensitive mission steps (deploy, etc.)."""

from __future__ import annotations

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from ..helpers import _parse_body
from ....models import PhaseStatus

router = APIRouter()


def _deploy_phases(mission) -> list:
    phases = getattr(mission, "phases", None) or []
    out = []
    for p in phases:
        pid = (getattr(p, "phase_id", None) or "").lower()
        if "deploy" in pid or getattr(p, "gate", "") == "checkpoint":
            if "deploy" in pid or "release" in pid or "production" in pid:
                out.append(p)
    return out


@router.get("/api/missions/{mission_id}/hitl/deploy")
async def hitl_deploy_status(mission_id: str):
    """List deploy phases awaiting human approval."""
    from ....missions.store import get_mission_run_store

    run_store = get_mission_run_store()
    mission = run_store.get(mission_id)
    if not mission:
        return JSONResponse({"error": "Not found"}, status_code=404)

    pending = []
    for p in _deploy_phases(mission):
        status = getattr(p, "status", "")
        if status in (
            PhaseStatus.WAITING_VALIDATION,
            "waiting_validation",
            "WAITING_VALIDATION",
        ):
            pending.append(
                {
                    "phase_id": p.phase_id,
                    "status": str(status),
                    "gate": getattr(p, "gate", ""),
                }
            )
    return JSONResponse(
        {
            "mission_id": mission_id,
            "pending": pending,
            "requires_action": len(pending) > 0,
        }
    )


@router.post("/api/missions/{mission_id}/hitl/deploy")
async def hitl_deploy_decide(request: Request, mission_id: str):
    """Approve or reject a deploy HITL gate (GO / NOGO / PIVOT)."""
    from .execution import api_mission_validate

    data = await _parse_body(request)
    phase_id = data.get("phase_id", "")
    if not phase_id:
        from ....missions.store import get_mission_run_store

        mission = get_mission_run_store().get(mission_id)
        deploy = _deploy_phases(mission) if mission else []
        if deploy:
            phase_id = deploy[0].phase_id
    if phase_id:
        request._body = None  # force re-read if needed
    return await api_mission_validate(request, mission_id)
