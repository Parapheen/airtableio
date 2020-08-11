import sys
sys.path.append('../')

from airtableio import Airtable
import asyncio

TOKEN = ""
APP_ID = ""

my_airtable = Airtable(TOKEN, APP_ID)

async def call():
    result = await my_airtable.get_fields("Users")
    print(result)

async def call_2():
    result = await my_airtable.get_fields("Tournaments")
    print(result)

if __name__=="__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(call())
    loop.create_task(call_2())

    loop.run_forever()
