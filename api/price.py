import os
import aiohttp
from asyncio import Semaphore

from tests.api.api_error_handler import api_error_handler

POS_BASE_URL = os.getenv("POS_BASE_URL")

service_rate_limiter = Semaphore(1)

async def price_api(token, payload):
    async with service_rate_limiter:
        service = "price_api"
        service_data = f"{service}_data"
        result = {}

        body = {"payload": payload}

        api_url = f"{POS_BASE_URL}/price"

        headers = {
            # "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(api_url, headers=headers, json=body) as response:
                    response.raise_for_status()
                    payload = await response.json()

                    data = payload[0] if isinstance(payload, list) and payload else {}
                    print("🛠️ API Payload:", data)

                    result[service_data] = {
                        "API status": f"✅ {response.status}",
                        "data": data,
                    }

        except aiohttp.ClientResponseError as error:
            return await api_error_handler(error, payload, service)

        except Exception as error:
            return await api_error_handler(error, payload, service)
        
        return result
