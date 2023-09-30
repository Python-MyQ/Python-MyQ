import asyncio

from pymyq.api import API

api = API("user", "pass", None)

async def main():
    await api.authenticate()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
