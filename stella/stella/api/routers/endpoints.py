import json
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

from stella.controllers.stella_controller import *

class Exam(BaseModel):
    date_series: dict
    meta_fields: dict

class Login(BaseModel):
    username: str
    password: str

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

@router.get("/api/stella/exams/list", tags=["stella"])
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

@router.get("/api/stella/exams", tags=["stella"])
async def list_exam_by_exam_name(exam_name: str):
    try:
        exam_list = get_list_of_exams_by_exam_name(exam_name)
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

@router.post("/api/stella/login", tags=["stella"])
async def system_login(login_data : Login):
    try:
        print(login_data, flush=True)
        ret = login_medic(login_data)
        assert ret is not None
        return ret[0]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ocorreu um erro interno, tente novamente mais tarde",
            headers={"WWW-Authenticate": "Bearer"}
        )