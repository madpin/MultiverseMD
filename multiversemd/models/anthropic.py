from .base import ModelInterface

class AnthropicModel(ModelInterface):
    async def generate_response(self, messages):
        return "Anthropic Response"
