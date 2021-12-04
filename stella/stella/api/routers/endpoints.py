import json
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()