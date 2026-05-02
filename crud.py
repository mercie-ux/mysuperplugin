# crud.py is for communication with your extensions database

# add your dependencies here
# from .models import createExample, Example
from lnbits.db import Database

db = Database("ext_mysuperplugin")

# add your fnctions here

# async def create_a_record(data: Example) -> createExample:
#     mysuperplugin_id = urlsafe_short_hash()
#     mysuperplugin = Example(id=mysuperplugin_id, **data.dict())
#     await db.insert("mysuperplugin.mysuperplugin", mysuperplugin)
#     return mysuperplugin


# async def get_a_record(mysuperplugin_id: str) -> Optional[Example]:
#     return await db.fetchone(
#         "SELECT * FROM mysuperplugin.mysuperplugin WHERE id = :id", {"id": mysuperplugin_id}, Example
#     )
