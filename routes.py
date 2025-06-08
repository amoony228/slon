from typing import List
from fastapi import APIRouter

import methods

translation_router = APIRouter(prefix="/translate")


@translation_router.get("/text2text/{to_language}")
async def get_order_status(input_text:str, to_language:str) -> List[str]:
    return await methods.translate_text(input_text, to_language)
    
    
