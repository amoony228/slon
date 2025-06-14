from openai import AsyncOpenAI

from openai import PermissionDeniedError

from secure_key import KEY
from config import MODEL, MAX_OUTPUT_TOKENS


class my_request_model(AsyncOpenAI):

    async def get_ai_answer(self, prompt:str) -> str:
        try:
            answer = await self.responses.create(
                        model=MODEL,
                        input=f'''{prompt}''',
                        max_output_tokens=MAX_OUTPUT_TOKENS)
            
        except PermissionDeniedError:
            print('[ERROR] Failed to complete request to ChatGPT. Possible cause: Invalid server region.')
            
        return answer.output_text
    
llm_client = my_request_model(api_key=KEY)