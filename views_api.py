from http import HTTPStatus

import httpx
from fastapi import APIRouter, Depends, HTTPException
from lnbits.decorators import require_invoice_key

from .models import Example

mysuperplugin_ext_api = APIRouter()

# views_api.py is for you API endpoints that could be hit by another service


@mysuperplugin_ext_api.get("/api/v1/test/{mysuperplugin_data}", description="Example API endpoint")
async def api_mysuperplugin(mysuperplugin_data: str) -> Example:
    if mysuperplugin_data != "00000000":
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Invalid mysuperplugin data",
        )
    # Do some python things and return the data
    return Example(id="2", wallet=mysuperplugin_data)


@mysuperplugin_ext_api.get(
    "/api/v1/vetted",
    description="Get the vetted extension readme",
    dependencies=[Depends(require_invoice_key)],
)
async def api_get_vetted():
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            "https://raw.githubusercontent.com/lnbits/lnbits-extensions/main/README.md"
        )
        return resp.text
