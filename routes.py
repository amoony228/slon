from fastapi import APIRouter

from LL_Models.text_llm import text_llm_client
from LL_Models.prompts import LlmPrompts as prompts


translation_router = APIRouter(prefix="/translate")

@translation_router.get("/text2text/{to_language}")
async def get_order_status(text:str, to_language:str) -> str:
    return await text_llm_client.get_ai_answer(prompts.translation.format(to_language, text))
    
    
    
