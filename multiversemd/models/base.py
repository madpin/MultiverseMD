from abc import ABC, abstractmethod

class ModelInterface(ABC):
    @abstractmethod
    async def generate_response(self, messages):
        pass
