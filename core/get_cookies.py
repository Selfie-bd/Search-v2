

from core.login import doodstream_login

PDisk_DB = {}


async def get_cookies(username: str, password: str) -> str:
    if not PDisk_DB:
        user_id, cookies = await doodstream_login(username, password)
        PDisk_DB["cookies"] = cookies
        PDisk_DB["user_id"] = user_id
        PDisk_DB["username"] = username
        PDisk_DB["password"] = password

    return PDisk_DB["cookies"]


async def set_cookies(data: dict):
    PDisk_DB["username"] = data["username"]
    PDisk_DB["password"] = data["password"]
    PDisk_DB["user_id"] = data["user_id"]
    PDisk_DB["cookies"] = data["cookies"]
