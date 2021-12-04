import json
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException, status

from stella.controllers.stella_controller import *

router = APIRouter()

@router.get("/api/stella", tags=["stella"])
async def test():
    try:
        return {"message": "Stella quote: 'Tecna, too technical!'"}
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ocorreu um erro interno, tente novamente mais tarde",
            headers={"WWW-Authenticate": "Bearer"}
        )

@router.get("/api/stella/list", tags=["stella"])
async def list_exams():
    try:
        exam_list = get_list_of_exams()
        return {'exams' : exam_list}
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ocorreu um erro interno, tente novamente mais tarde",
            headers={"WWW-Authenticate": "Bearer"}
        )
