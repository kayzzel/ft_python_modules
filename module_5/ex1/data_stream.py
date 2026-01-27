from abc import ABC, abstractmethod
from typing import Any, List, Dict, Optional, Union


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id: str = stream_id
        self.stream_type: str = stream_type
        self.processed: int | float = 0
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}\n")

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None
                    ) -> List[Any]:

        def is_float(value: str) -> bool:
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
                    filtered_data[f"{criteria}: {data[criteria]}"]
        return filtered_data

    def get_stats(self) -> Dict[str, Union(str, int, float)]:
        return {
            "stream_id": self.stream_id,
            "type": self.stream_type,
            "processed": self.processed
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        print("Initializing Sensor Stream...")
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            temp: List[str] = self.filtered_data(data_batch, "temp")
            humidity: List[str] = self.filtered_data(data_batch, "humidity")
            pressure: List[str] = self.filtered_data(data_batch, "pressure")
            processed: list[str] = [values
                                    for values in (temp, humidity, pressure)
                                    if values]
            avg_temp = sum([float(tmp.split(": ")[1])
                            for tmp in temp]) / len(temp)
            self.processed = len(processed)
            return (
                f"Stream ID: {self.stream_id}, Type: {self.stream_type}\n"
                f"Processing sensor batch: {processed}\n"
                f"Sensor analysis: {len(processed)} readings processed, "
                f"avg temp: {avg_temp:.1f}°C"
            )
        except Exception as e:
            return f"Sensor processing error: {e}"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        print("Initializing Transaction Stream...")
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            buy: List[str] = self.filtered_data(data_batch, "buy")
            sell: List[str] = self.filtered_data(data_batch, "sell")
            processed: list[str] = [values
                                    for values in (buy, sell)
                                    if values]

            self.processed = len(processed)
            net_flow = sum([-float(value.split(": ")[1])
                            if value.split(": ")[0] == "sell"
                            else float(value.split(": ")[1])
                            for value in processed]) / len(processed)
            sign: str = "+" if net_flow >= 0 else ""
            return (
                f"Stream ID: {self.stream_id}, Type: {self.stream_type}\n"
                f"Processing transaction batch: {processed}\n"
                f"Transaction analysis: {len(processed)} operations, "
                f"net flow: {sign}{net_flow:.1f} units"
            )
        except Exception as e:
            return f"Transaction processing error: {e}"


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        print("Initializing Event Stream...")
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            events: List[str] = [e for e in data_batch if isinstance(e, str)]
            self.processed += len(events)

            errors: List[str] = [e for e in events if "error" in e.lower()]
            return (
                f"Stream ID: {self.stream_id}, Type: {self.stream_type}\n"
                f"Processing event batch: {data_batch}\n"
                f"Event analysis: {len(events)} events, "
                f"{len(errors)} error detected"
            )
        except Exception as e:
            return f"Event processing error: {e}"


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def register_stream(self, stream: DataStream) -> None:
        if not isinstance(stream, DataStream):
            raise TypeError("Invalid stream")
        self.streams += [stream]

    def process_streams(
        self,
        batches: Dict[str, List[Any]]
    ) -> None:
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")
        print()

        for stream in self.streams:
            try:
                data = batches.get(stream.stream_id, [])
                print(stream.process_batch(data))
                print()
            except Exception as e:
                print(f"Stream failure [{stream.stream_id}]: {e}")
                print()

    def batch_result(self, batch_id: int) -> str:
        sensor_data: int = 0
        transaction_data: int = 0
        event_data: int = 0

        for stream in self.streams:
            if isinstance(stream, SensorStream):
                sensor_data += stream.get_stats()["processed"]
            elif isinstance(stream, TransactionStream):
                transaction_data += stream.get_stats()["processed"]
            elif isinstance(stream, EventStream):
                event_data += stream.get_stats()["processed"]

        return (
                f"Batch {batch_id} Rsults:\n"
                f"- Sensor data: {sensor_data} readings processed\n"
                f"- Transaction data: {sensor_data} operations processed\n"
                f"- Event data: {sensor_data} events processed"
                )

    def filter_streams(
        self,
        batches: List[Any],
        criteria: str
    ) -> None:
        print("Stream filtering active: High-priority data only")

        sensor_alerts = 0
        large_transactions = 0

        for stream in self.streams:
            data = batches.get(stream.stream_id, [])
            filtered = stream.filter_data(data, criteria)

            if isinstance(stream, SensorStream):
                sensor_alerts += len(filtered)
            elif isinstance(stream, TransactionStream):
                large_transactions += len(filtered)

        print(
            f"Filtered results: {sensor_alerts} critical sensor alerts, "
            f"{large_transactions} large transaction"
        )


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()

    batches = {
        "SENSOR_001": [22.5, 22.5, 22.5],
        "TRANS_001": [100, -50, -25],
        "EVENT_001": ["login", "error", "logout"]
    }

    processor = StreamProcessor()
    processor.process_streams(batches)
    print(processor.batch_result(1))

    print()
    processor.filter_streams(batches, "hight")

    print()
    print("All streams processed successfully. Nexus throughput optimal.")
