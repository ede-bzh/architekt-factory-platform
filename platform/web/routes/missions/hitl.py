"""Human-in-the-loop (HITL) mission checkpoint endpoints."""

from __future__ import annotations

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from ..helpers import _parse_body

router = APIRouter()


@router.post("/api/missions/{mission_id}/validate")
async def api_mission_validate(request: Request, mission_id: str):
    """Human validates a checkpoint (GO/NOGO/PIVOT)."""
    from ....a2a.bus import get_bus
    from ....missions.store import get_mission_run_store
    from ....models import A2AMessage, MessageType, PhaseStatus
    from ....sessions.store import MessageDef, get_session_store

    data = await _parse_body(request)
    decision = str(data.get("decision", "GO")).upper()

    run_store = get_mission_run_store()
    mission = run_store.get(mission_id)
    if not mission:
        return JSONResponse({"error": "Not found"}, status_code=404)

    updated_phase = False
    if mission.current_phase:
        for p in mission.phases:
            if p.phase_id == mission.current_phase and p.status in (
                PhaseStatus.WAITING_VALIDATION,
                "waiting_validation",
            ):
                p.status = PhaseStatus.DONE if decision == "GO" else PhaseStatus.FAILED
                updated_phase = True
        run_store.update(mission)
        if updated_phase:
            new_status = "done" if decision == "GO" else "failed"
            run_store.update_phase(mission.id, mission.current_phase, status=new_status)

    orch_id = mission.cdp_agent_id or "chef_de_programme"
    if mission.session_id:
        session_store = get_session_store()
        session_store.add_message(
            MessageDef(
                session_id=mission.session_id,
                from_agent="user",
                to_agent=orch_id,
                message_type="response",
                content=f"DECISION: {decision}",
            )
        )
        bus = get_bus()
        import uuid
        from datetime import datetime

        await bus.publish(
            A2AMessage(
                id=uuid.uuid4().hex[:8],
                session_id=mission.session_id,
                from_agent="user",
                to_agent=orch_id,
                message_type=MessageType.RESPONSE,
                content=f"DECISION: {decision}",
                timestamp=datetime.utcnow(),
            )
        )

    return JSONResponse({"decision": decision, "phase": mission.current_phase})
