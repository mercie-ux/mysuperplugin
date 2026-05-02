import asyncio

from fastapi import APIRouter
from loguru import logger

from .crud import db
from .tasks import wait_for_paid_invoices
from .views import mysuperplugin_ext_generic
from .views_api import mysuperplugin_ext_api

mysuperplugin_ext: APIRouter = APIRouter(prefix="/mysuperplugin", tags=["mysuperplugin"])
mysuperplugin_ext.include_router(mysuperplugin_ext_generic)
mysuperplugin_ext.include_router(mysuperplugin_ext_api)

mysuperplugin_static_files = [
    {
        "path": "/mysuperplugin/static",
        "name": "mysuperplugin_static",
    }
]

scheduled_tasks: list[asyncio.Task] = []


def mysuperplugin_stop():
    for task in scheduled_tasks:
        try:
            task.cancel()
        except Exception as ex:
            logger.warning(ex)


def mysuperplugin_start():
    from lnbits.tasks import create_permanent_unique_task

    task = create_permanent_unique_task("ext_testing", wait_for_paid_invoices)
    scheduled_tasks.append(task)


__all__ = [
    "db",
    "mysuperplugin_ext",
    "mysuperplugin_start",
    "mysuperplugin_static_files",
    "mysuperplugin_stop",
]
