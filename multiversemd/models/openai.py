from .base import ModelInterface

class OpenAIModel(ModelInterface):
    async def generate_response(self, messages):
        return "OpenAI Response"
