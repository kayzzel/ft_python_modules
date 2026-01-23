from abc import ABC, abstractmethod
from typing import Any, List


class Datastream(ABC):
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None)
    -> List[Any]:
        pass
