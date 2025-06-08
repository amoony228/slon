from openai import AsyncOpenAI
from typing import List

from secure_key import KEY
from config import MODEL, MAX_OUTPUT_TOKENS


client = AsyncOpenAI(api_key=KEY)

async def translate_text(input_text:str, to_language:str) -> List[str]: 
    translation_responce = await client.responses.create(
                model=MODEL,
                input=f'''translate the following into {to_language}: "{input_text}". The result should be only a line with the translation''',
                max_output_tokens=MAX_OUTPUT_TOKENS)
    
    explanation_response = await client.responses.create(
                model=MODEL,
                input=f'''Please provide the BRIEFEST POSSIBLE explanation in {to_language} of the puns, jokes, etc. (if any) that were implied in this text: "{input_text}" 
                if something in this text has lost its meaning or significance during translation. 
                The result should be ONLY a brief explanation of the text, without text translation. DO NOT explain cultural norms.
                If there is nothing to explain in the text, answer ONLY as follows: "Nothing to explain." ''',
                max_output_tokens=MAX_OUTPUT_TOKENS
                )
    return translation_responce.output_text, explanation_response.output_text
