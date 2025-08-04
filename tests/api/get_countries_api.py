import os
import aiohttp
import urllib.parse
from asyncio import Semaphore

from tests.api.handle_api_error import handle_api_error

POS_BASE_URL = os.getenv("POS_BASE_URL")

service_rate_limiter = Semaphore(1)

async def get_countries_api(token, country_id):
    async with service_rate_limiter:
        service = "get_countries_api"
        service_data = f"{service}_data"
        result = {"country_id": country_id}

        api_params = urllib.parse.urlencode({"country_id": country_id})
        api_url = f"{POS_BASE_URL}/countries?{api_params}"

        headers = {
            # "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(api_url, headers=headers) as response:
                    response.raise_for_status()
                    payload = await response.json()

                    data = payload[0] if isinstance(payload, list) and payload else {}
                    # print("🛠️ api_countrues Payload:", data)
                    
                    country_id = data.get("country_id", [{}])[0]

                    extracted_data = {
                        "country_id": country_id.get("country_id", "N/A"),
                    }

                    print(f"✅ get_countries_api: {response.status} country:{extracted_data['country_id']}")

                    result[service_data] = {
                        "get_countries_api_status": f"✅ {response.status}",
                        **extracted_data,  # Expands dictionary to maintain consistency
                    }

        except aiohttp.ClientResponseError as error:
            return await handle_api_error(error, country_id, service)

        except Exception as error:
            return await handle_api_error(error, country_id, service)
        
        return result
