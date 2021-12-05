import json
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

from stella.controllers.stella_controller import *

class Exam(BaseModel):
    date_series: dict
    meta_fields: dict

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

@router.get("/api/stella/exams", tags=["stella"])
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

@router.post("/api/stella/exams", tags=["stella"])
async def insert_exam(exam_data: Exam):
    try:
        assert insert_one_exam(exam_data)
        return {'message' : 'Exam added successfully'}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ocorreu um erro interno, tente novamente mais tarde",
            headers={"WWW-Authenticate": "Bearer"}
        )
