import asyncio
from concurrent.futures import ThreadPoolExecutor

from passlib.context import CryptContext


executor = ThreadPoolExecutor(thread_name_prefix='hashing')
pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")


async def verify_password(plain_password: str, hashed_password: str) -> bool:
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(
        executor,
        pwd_context.verify,
        plain_password,
        hashed_password
        )


async def get_password_hash(password: str) -> str:
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(executor, pwd_context.hash, password)
