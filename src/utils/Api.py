import config

import asyncio
import aiohttp

import requests
import json


class STAGE:
    ALL_STAGE = "https://spla3.yuu26.com/api/schedule"
    NOW_STAGE = "https://spla3.yuu26.com/api/regular/now"

    NEXT_MATCH_OPEN = "https://spla3.yuu26.com/api/bankara-challenge/next"
    NOW_MATCH_CHARANGE = "https://spla3.yuu26.com/api/bankara-challenge/next"

    NOW_X_MATCH = "https://spla3.yuu26.com/api/x/schedule"
    NOW_FES_MATCH = "https://spla3.yuu26.com/api/fest/schedule"



def load(stage:STAGE):
    return  json.loads(json.dumps(requests.get(stage).json(), indent=4,  ensure_ascii=False))