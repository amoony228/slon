import asyncio
from deepgram import DeepgramClient, SpeakOptions
import asyncio, aiofiles

from secure_key import TTS_KEY


class tts_LLModel(DeepgramClient):

    __FILENAME = "test.wav"
    __OPTIONS = SpeakOptions(model="aura-2-apollo-en")

    def __init__(self, key):
        super().__init__(key)

    async def say(self, text:str) -> str:
        response = await self.speak.asyncrest.v("1").stream_memory({"text": text}, self.__OPTIONS)
        
        async with aiofiles.open(self.__FILENAME, "wb") as out:
            await out.write(response.stream_memory.getbuffer())
            await out.flush()
        

tts_llm_client = tts_LLModel(key=TTS_KEY)


if __name__ == "__main__":
    asyncio.run(tts_llm_client.say("Well fuck a duck"))

    
    