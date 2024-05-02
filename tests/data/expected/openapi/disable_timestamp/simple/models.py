# generated by fastapi-codegen:
#   filename:  simple.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class Pet(BaseModel):
    id: int
    name: str
    tag: Optional[str] = None


class Error(BaseModel):
    code: int
    message: str
