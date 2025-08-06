import os
import aiohttp
from asyncio import Semaphore

from tests.api.api_error_handler import api_error_handler

POS_BASE_URL = os.getenv("POS_BASE_URL")

service_rate_limiter = Semaphore(1)

async def get_state_by_postcode_api(token, postcode):
    async with service_rate_limiter:
        service = "get_state_by_postcode_api"
        service_data = f"{service}_data"
        result = {}

        body = {"postcode": postcode}

        api_url = f"{POS_BASE_URL}/getStateByPostcode"

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
            return await api_error_handler(error, postcode, service)

        except Exception as error:
            return await api_error_handler(error, postcode, service)
        
        return result
