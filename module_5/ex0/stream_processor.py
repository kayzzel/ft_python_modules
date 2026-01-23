from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """
    Abstract base class for data processors.

    Defines a common interface for processing, validating,
    and formatting different types of data.
    """

    @abstractmethod
    def process(self, data: Any) -> str:
        """
        Process the provided data and return a result string.

        Args:
            data (Any): Input data to be processed.

        Returns:
            str: Result of the processing operation.
        """
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        Validate the provided data before processing.

        Args:
            data (Any): Input data to validate.

        Returns:
            bool: True if data is valid, False otherwise.
        """
        pass

    @abstractmethod
    def format_output(self, result: str) -> str:
        """
        Format the processed result for output.

        Args:
            result (str): Raw processing result.

        Returns:
            str: Formatted output string.
        """
        pass


class NumericProcessor(DataProcessor):
    """
    Processor for numeric data.

    Handles lists of integers or floats and computes
    their sum and average.
    """

    def __init__(self) -> None:
        """
        Initialize the NumericProcessor and internal counters.
        """
        print("Initializing Numeric Processor...")
        self.__count_numbers: int = 0
        self.__sum: int | float = 0
        self.__avg: float = 0

    def process(self, data: list[int | float]) -> str:
        """
        Process a list of numeric values.

        Calculates the sum and average of the numbers.

        Args:
            data (list[int | float]): List of numeric values.

        Returns:
            str: Summary of the processed numeric data.

        Raises:
            ValueError: If the input data is invalid.
        """
        if not self.validate(data):
            raise ValueError("Invalide Data")
        self.__sum = 0
        self.__count_numbers = len(data)
        for item in data:
            self.__sum += item
        self.__avg = self.__sum / self.__count_numbers
        return f"Processed {self.__count_numbers} numeric values, \
sum={self.__sum}, avg={self.__avg}"

    def validate(self, data: list[int | float]) -> bool:
        """
        Validate numeric input data.

        Ensures the data is a list containing only
        integers or floats.

        Args:
            data (list[int | float]): Data to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        if type(data) is not list:
            return False
        for item in data:
            if type(item) is not int and type(item) is not float:
                return False
        return True

    def format_output(self, result: str) -> str:
        """
        Format numeric processing output.

        Args:
            result (str): Raw result string.

        Returns:
            str: Formatted output.
        """
        return f"Output: {result}"


class TextProcessor(DataProcessor):
    """
    Processor for text data.

    Counts characters and words in a text string.
    """

    def __init__(self) -> None:
        """
        Initialize the TextProcessor and counters.
        """
        print("Initializing Text Processor...")
        self.__count_char: int = 0
        self.__count_words: int = 0

    def process(self, data: str) -> str:
        """
        Process text data.

        Counts the number of characters and words.

        Args:
            data (str): Text to process.

        Returns:
            str: Summary of the processed text.

        Raises:
            ValueError: If the input data is invalid.
        """
        if not self.validate(data):
            raise ValueError("Invalide Data")
        self.__count_char = len(data)
        self.__count_words = len(data.split(" "))
        return f"Processed text: {self.__count_char} characteres, \
{self.__count_words} words"

    def validate(self, data: str) -> bool:
        """
        Validate text input data.

        Args:
            data (str): Data to validate.

        Returns:
            bool: True if data is a string, False otherwise.
        """
        return (type(data) is str)

    def format_output(self, result: str) -> str:
        """
        Format text processing output.

        Args:
            result (str): Raw result string.

        Returns:
            str: Formatted output.
        """
        return f"Output: {result}"


class LogProcessor(DataProcessor):
    """
    Processor for log data.

    Extracts log level and message from structured log strings.
    """

    def __init__(self) -> None:
        """
        Initialize the LogProcessor.
        """
        print("Initializing Log Processor...")
        self.__level: str = ""
        self.__message: str = ""

    def process(self, data: str) -> str:
        """
        Process a log entry.

        Splits the log string into a level and message.

        Args:
            data (str): Log entry in 'LEVEL: message' format.

        Returns:
            str: Formatted alert message.

        Raises:
            ValueError: If the input data is invalid.
        """
        if not self.validate(data):
            raise ValueError("Invalide Data")
        self.__level, self.__message = data.split(": ", 2)
        return f"[ALERT] {self.__level} level detected: {self.__message}"

    def validate(self, data: str) -> bool:
        """
        Validate log input data.

        Ensures the log is a string with a single ': ' separator.

        Args:
            data (str): Data to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        if type(data) is not str:
            return False
        if len(data.split(": ")) != 2:
            return False
        return True

    def format_output(self, result: str) -> str:
        """
        Format log processing output.

        Args:
            result (str): Raw result string.

        Returns:
            str: Formatted output.
        """
        return f"Output: {result}"


if __name__ == "__main__":
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
