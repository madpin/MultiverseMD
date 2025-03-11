from .base import ModelInterface

class MistralModel(ModelInterface):
    async def generate_response(self, messages):
        return "Mistral Response"
