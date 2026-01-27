#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Optional, Union


class DataStream(ABC):
    """
    Abstract base class for data streams.

    Defines a common interface for processing batches of data
    and retrieving stream statistics.
    """

    def __init__(self, stream_id: str, stream_type: str) -> None:
        """
        Initialize a data stream.

        Args:
            stream_id (str): Unique identifier for the stream.
            stream_type (str): Human-readable stream type.
        """
        self.stream_id: str = stream_id
        self.stream_type: str = stream_type
        self.processed: int | float = 0
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}")

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process a batch of incoming data.

        Args:
            data_batch (List[Any]): Batch of raw data items.

        Returns:
            str: Human-readable processing result.
        """
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """
        Filter incoming data based on a key and numeric value.

        Supports string entries formatted as 'key: value'
        and dictionary entries with numeric values.

        Args:
            data_batch (List[Any]): Incoming data batch.
            criteria (Optional[str]): Filtering key.

        Returns:
            List[Any]: Filtered data matching the criteria.
        """

        def is_float(value: str) -> bool:
            """
            Check whether a string value can be converted to float.

            Args:
                value (str): Value to test.

            Returns:
                bool: True if convertible to float, False otherwise.
            """
            try:
                float(value)
                return True
            except ValueError:
                return False

        if criteria is None:
            return data_batch

        filtered_data: List[Any] = []
        for data in data_batch:
            if isinstance(data, str):
                splited = data.split(": ")
                if len(splited) == 2 and splited[0] == criteria \
                        and is_float(splited[1]):
                    filtered_data += [data]
            elif isinstance(data, dict):
                if criteria in data and is_float(data[criteria]):
                    filtered_data += [f"{criteria}: {data[criteria]}"]
        return filtered_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """
        Retrieve stream statistics.

        Returns:
            Dict[str, Union[str, int, float]]: Stream metadata and
            number of processed items.
        """
        return {
            "stream_id": self.stream_id,
            "type": self.stream_type,
            "processed": self.processed
        }


class SensorStream(DataStream):
    """
    Stream processor for environmental sensor data.

    Handles temperature, humidity, and pressure readings.
    """

    def __init__(self, stream_id: str) -> None:
        """
        Initialize a SensorStream.

        Args:
            stream_id (str): Unique stream identifier.
        """
        print("Initializing Sensor Stream...")
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process a batch of sensor readings.

        Computes average temperature and counts processed readings.

        Args:
            data_batch (List[Any]): Raw sensor data.

        Returns:
            str: Sensor processing summary or error message.
        """
        try:
            temp: List[str] = self.filter_data(data_batch, "temp")
            humidity: List[str] = self.filter_data(data_batch, "humidity")
            pressure: List[str] = self.filter_data(data_batch, "pressure")

            processed: list[str] = [
                value for values in (temp, humidity, pressure)
                if values for value in values
            ]

            avg_temp: float = sum(
                float(tmp.split(": ")[1]) for tmp in temp
            ) / len(temp)

            self.processed = len(processed)

            return (
                f"Processing sensor batch: [{', '.join(processed)}]\n"
                f"Sensor analysis: {len(processed)} readings processed, "
                f"avg temp: {avg_temp:.1f}°C"
            )
        except Exception as e:
            return f"Sensor processing error: {e}"


class TransactionStream(DataStream):
    """
    Stream processor for financial transaction data.

    Handles buy and sell operations and computes net flow.
    """

    def __init__(self, stream_id: str) -> None:
        """
        Initialize a TransactionStream.

        Args:
            stream_id (str): Unique stream identifier.
        """
        print("Initializing Transaction Stream...")
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process a batch of transaction data.

        Calculates net flow from buy and sell operations.

        Args:
            data_batch (List[Any]): Raw transaction data.

        Returns:
            str: Transaction processing summary or error message.
        """
        try:
            buy: List[str] = self.filter_data(data_batch, "buy")
            sell: List[str] = self.filter_data(data_batch, "sell")

            processed: list[str] = [
                value for values in (buy, sell)
                if values for value in values
            ]

            self.processed = len(processed)
            net_flow: float = 0

            for value in processed:
                action, quantity = value.split(": ")
                if action == "buy":
                    net_flow += float(quantity)
                if action == "sell":
                    net_flow -= float(quantity)

            sign: str = "+" if net_flow >= 0 else ""

            return (
                f"Processing transaction batch: [{', '.join(processed)}]\n"
                f"Transaction analysis: {len(processed)} operations, "
                f"net flow: {sign}{net_flow:.1f} units"
            )
        except Exception as e:
            return f"Transaction processing error: {e}"


class EventStream(DataStream):
    """
    Stream processor for system event data.

    Extracts events and detects error-related occurrences.
    """

    def __init__(self, stream_id: str) -> None:
        """
        Initialize an EventStream.

        Args:
            stream_id (str): Unique stream identifier.
        """
        print("Initializing Event Stream...")
        super().__init__(stream_id, "System Events")

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """
        Filter event data without numeric validation.

        Args:
            data_batch (List[Any]): Raw event data.
            criteria (Optional[str]): Event key.

        Returns:
            List[Any]: Filtered event entries.
        """
        if criteria is None:
            return data_batch

        filtered_data: List[Any] = []
        for data in data_batch:
            if isinstance(data, str):
                splited: List[str] = data.split(": ")
                if len(splited) == 2 and splited[0] == criteria:
                    filtered_data += [data]
            elif isinstance(data, dict):
                if criteria in data:
                    filtered_data += [f"{criteria}: {data[criteria]}"]
        return filtered_data

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process a batch of system events.

        Detects total events and error-related events.

        Args:
            data_batch (List[Any]): Raw event data.

        Returns:
            str: Event processing summary or error message.
        """
        try:
            events: List[str] = self.filter_data(data_batch, "event")
            events = [event.split(": ")[1] for event in events]

            self.processed += len(events)
            errors: List[str] = [
                e for e in events if "error" in e.lower()
            ]

            return (
                f"Processing event batch: [{', '.join(events)}]\n"
                f"Event analysis: {len(events)} events, "
                f"{len(errors)} error detected"
            )
        except Exception as e:
            return f"Event processing error: {e}"


class StreamProcessor:
    """
    High-level orchestrator for processing multiple stream types.

    Coordinates sensor, transaction, and event streams
    using a unified processing interface.
    """

    def __init__(self) -> None:
        """
        Initialize the StreamProcessor.
        """
        self.batch_number: int = 0

    def process_streams(self, batches: List[Any]) -> None:
        """
        Process a batch of mixed data through all stream types.

        Args:
            batches (List[Any]): Mixed input data batch.
        """
        self.batch_number += 1

        sensor: SensorStream = SensorStream(
            f"SENSOR_\
{'00' if self.batch_number < 10 else '0' if self.batch_number < 100 else ''}\
{self.batch_number}"
        )
        print(sensor.process_batch(batches))

        print()
        transaction: TransactionStream = TransactionStream(
            f"TRANSACTION_\
{'00' if self.batch_number < 10 else '0' if self.batch_number < 100 else ''}\
{self.batch_number}"
        )
        print(transaction.process_batch(batches))

        print()
        event: EventStream = EventStream(
            f"EVENT_\
{'00' if self.batch_number < 10 else '0' if self.batch_number < 100 else ''}\
{self.batch_number}"
        )
        print(event.process_batch(batches))

        print()
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")

        print()
        print(
            f"Batch {self.batch_number} Rsults:\n"
            f"- Sensor data: {sensor.get_stats()['processed']} \
readings processed\n"
            f"- Transaction data: {transaction.get_stats()['processed']} \
operations processed\n"
            f"- Event data: {event.get_stats()['processed']} events processed"
        )

        print()
        print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()

    batches = [
            "temp: 22.5",
            "buy: 100",
            "event: login",
            "humidity: 65",
            "pressure: 1013",
            {"event": "error"},
            {"sell": "150"},
            {"buy": "75"},
            "event: logout"
            ]

    processor = StreamProcessor()
    processor.process_streams(batches)
