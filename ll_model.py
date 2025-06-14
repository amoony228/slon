from openai import AsyncOpenAI

from secure_key import KEY


class LLModel(AsyncOpenAI):
    __MODEL = "gpt-4o-mini-2024-07-18"
    __MAX_OUTPUT_TOKENS = 100

    def __init__(self, key):
        super().__init__(api_key=key)

    async def get_ai_answer(self, prompt:str) -> str:
        answer = await self.responses.create(model=self.__MODEL, input=f'''{prompt}''', max_output_tokens=self.__MAX_OUTPUT_TOKENS)
        return answer.output_text
    
llm_client = LLModel(key=KEY)