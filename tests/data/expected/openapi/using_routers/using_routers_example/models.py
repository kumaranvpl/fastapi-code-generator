# generated by fastapi-codegen:
#   filename:  using_routers_example.yaml
#   timestamp: 2023-04-11T00:00:00+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class Pet(BaseModel):
    id: int
    name: str
    tag: Optional[str] = None
