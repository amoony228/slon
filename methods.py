from typing import List

from ll_model import llm_client


async def translate_text(input_text:str, to_language:str) -> List[str]: 
    translation_responce = await llm_client.get_ai_answer(f'''translate the following into {to_language}: "{input_text}". The result should be only a line with the translation''')
        
    explanation_response = await llm_client.get_ai_answer(f'''Please provide the BRIEFEST POSSIBLE explanation in {to_language} of the puns, jokes, etc. (if any) that were implied in this text: "{input_text}" 
                    if something in this text has lost its meaning or significance during translation. 
                    The result should be ONLY a brief explanation of the text, without text translation. DO NOT explain cultural norms.
                    If there is nothing to explain in the text, answer ONLY as follows: "Nothing to explain." ''')
    
    return translation_responce, explanation_response
