#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        ...

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        print("Initializing Numeric Processor...")
        self.__count_numbers: int = 0
        self.__sum: int | float = 0
        self.__avg: float = 0

    def process(self, data: list[int | float]) -> str:
        if not self.validate(data):
            return "Error: Invalide Data"
        self.__sum = 0
        self.__count_numbers = len(data)
        for item in data:
            self.__sum += item
        self.__avg = self.__sum / self.__count_numbers
        return f"Processed {self.__count_numbers} numeric values, \
sum={self.__sum}, avg={self.__avg}"

    def validate(self, data: list[int | float]) -> bool:
        if type(data) is not list:
            return False
        for item in data:
            if type(item) is not int and type(item) is not float:
                return False
        return True


class TextProcessor(DataProcessor):

    def __init__(self) -> None:
        print("Initializing Text Processor...")
        self.__count_char: int = 0
        self.__count_words: int = 0

    def process(self, data: str) -> str:
        if not self.validate(data):
            return "Error: Invalide Data"
        self.__count_char = len(data)
        self.__count_words = len(data.split(" "))
        return f"Processed text: {self.__count_char} characteres, \
{self.__count_words} words"

    def validate(self, data: str) -> bool:
        return (type(data) is str)


class LogProcessor(DataProcessor):

    def __init__(self) -> None:
        print("Initializing Log Processor...")
        self.__level: str = ""
        self.__message: str = ""

    def process(self, data: str) -> str:
        if not self.validate(data):
            return "Error: Invalide Data"
        self.__level, self.__message = data.split(": ", 2)
        return f"[ALERT] {self.__level} level detected: {self.__message}"

    def validate(self, data: str) -> bool:
        if type(data) is not str:
            return False
        if len(data.split(": ")) != 2:
            return False
        return True


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    numeric_data: list[int | float] = [1, 2, 3, 4, 5]
    text_data: str = "Hello Nexus World"
    log_data: str = "Error: Connection timeout"

    print()
    numeric = NumericProcessor()
    print(f"Processing data: {numeric_data}")
    print(f"Validation: numeric data \
{'verified' if numeric.validate(numeric_data) else 'invalide'}")
    print(numeric.format_output(numeric.process(numeric_data)))

    print()
    text = TextProcessor()
    print(f"Processing data: {text_data}")
    print(f"Validation: text data \
{'verified' if text.validate(text_data) else 'invalide'}")
    print(text.format_output(text.process(text_data)))

    print()
    log = LogProcessor()
    print(f"Processing data: {log_data}")
    print(f"Validation: Log entry \
{'verified' if log.validate(log_data) else 'invalide'}")
    print(log.format_output(log.process(log_data)))

    print()
    print("=== Polymorphic Processing Demo ===")

    print()
    print("Processing multiple data types through same interface...")
    print(f"Result 1: {numeric.process([1, 2, 3])}")
    print(f"Result 2: {text.process('Hello World!')}")
    print(f"Result 3: {log.process('INFO: System ready')}")

    print()
    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
