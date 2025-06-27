import os
from groq import Groq
class GroqService:

    def __init__(self,model: str):
        self.model = model;
        self.key = os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=self.key)

    def request_prompt(self, context_system :str, message:str):
        messages = []
        if(context_system != None):
            messages.append({
                "role" : "system",
                "content": context_system
            })
        messages.append(
            {
                "role": 'user',
                "content": message
            })

        response = self.client.chat.completions.create(
            messages=messages,
            model=self.model,
            )
        return response.choices[0].message.content

