#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Protocol, Any, Union, List, Dict
import time


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class InputStage():
    def process(self, data: Any) -> Any:
        if (isinstance(data, dict)):
            try:
                for key, value in data.items():
                    if (key not in ["sensor", "value", "unit"]):
                        raise Exception("Error S1: Invalide data structure,  \
valid structur is {sensor : ... , value : ... , unit : ...}")
                    if ((isinstance(value, int) or isinstance(value, float))
                       is False and isinstance(value, str) is False):
                        raise ValueError(f"Error S1: Invalide data found in \
data, {value} is not a string or an integer")
                data["value"] = float(data["value"])
            except (Exception, ValueError) as err:
                print(err)
                return None
            else:
                return data

        elif (isinstance(data, str)):
            try:
                data_split = data.split(",")
                if (len(data_split) < 3):
                    raise Exception("Error S1: Invalide data structure, \
valid structur is 'user,action,timestamp'")
            except Exception as err:
                print(err)
                return None
            else:
                return data

        elif (isinstance(data, list)):
            try:
                for temp in data:
                    float(temp)
            except Exception as err:
                print(err)
                return None
            else:
                return data
        print("Error S1: Invalide data type")


class TransformStage():
    def process(self, data: Any) -> Dict:
        if (isinstance(data, dict)):
            try:
                return ["Sensor_data", data]
            except Exception:
                print("Error S2: invalid data forma")
                return None

        if (isinstance(data, str)):
            try:
                return ["Log_data", {key: value for key, value
                                     in zip(["user", "action", "timestamp"],
                                            data.split(","))}]
            except Exception:
                print("Error S2: invalid data forma")
                return None

        if (isinstance(data, list)):
            try:
                return ["measure_data",
                        {"temp_" + str(i): data[i] for i in range(0, len(data))
                         }]
            except Exception as err:
                print(err)
                return None
        return data


class OutputStage():
    def process(self, data: Any) -> str:
        if data is None:
            return "An Error occured, output can't be generated"

        if data[0] == "Sensor_data":
            data = data[1]
            if data["sensor"] == "temp":
                return f"Processed temperatur reading: \
{data['value']} {data['unit']} (Normal Range)"
            if data["sensor"] == "hum":
                return f"Processed humidity reading: \
{data['value']} {data['unit']} (Normal Range)"

        if data[0] == "Log_data":
            data = data[1]
            return f"User: {data['user']}, activity: \
{data['action']} at {data['timestamp']}, 1 actions processed"

        if data[0] == "measure_data":
            data = data[1]
            return f"Stream summary: \
{len(data)} readings, avg: {round(sum(data.values()) / len(data), 2)}°C"


class OutputFormatStage():
    def process(self, data: Any) -> str:
        if (data is None):
            return data
        return data.upper()


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id: str = pipeline_id
        self.stages: List[InputStage | TransformStage | OutputStage] = []

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass

    def add_stage(self,
                  stages: List[InputStage | TransformStage | OutputStage]
                  ) -> None:
        for stage in stages:
            if (stage.__class__.__name__ in [stage.__class__.__name__
                                             for stage in self.stages]):
                print(f"{stage.__class__.__name__} already added, skipping")
            else:
                self.stages.append(stage)


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            for d in data:
                if (isinstance(d, dict)):
                    data = d
                    print(f"Input: {data}")
                    if (len(self.stages) == 0):
                        raise Exception("Error JSONAdapter: no stages given")
                    for stage in self.stages:
                        data = stage.process(data)
                    return data

            raise Exception("Error JSONAdapter: no valide data type found")
        except (Exception, AttributeError) as err:
            print(err)
            return None


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            for d in data:
                if (isinstance(d, str)):
                    data = d
                    print(f"Input: {data}")
                    if (len(self.stages) <= 0):
                        raise Exception("Error CSVAdapter: no stages given")
                    for stage in self.stages:
                        data = stage.process(data)
                    return data

            raise Exception("Error CSVAdapter: no valide data type found")
        except (Exception, AttributeError) as err:
            print(err)
            return None


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            for d in data:
                if (isinstance(d, list)):
                    data = d
                    print(f"Input: {data}")
                    if (len(self.stages) <= 0):
                        raise Exception("Error StreamAdapter: no stages given")
                    for stage in self.stages:
                        data = stage.process(data)
                    return data

            raise Exception("Error StreamAdapter: no valide data type found")
        except (Exception, AttributeError) as err:
            print(err)
            return None




class NexusManager():
    def __init__(self):
        self.piplines = []

    def add_pipeline(self, pipelines: Any) -> None:
        for pipeline in pipelines:
            if (pipeline in self.piplines):
                print(f"{type(pipeline).__name__} already added, skipping")
            else:
                self.piplines.append(pipeline)

    def process_data(self, data: Any):
        input = InputStage()
        transform = TransformStage()
        output = OutputStage()

        for pipeline in self.piplines:
            print(f"\nProcessing {pipeline.pipeline_id[:-3]} \
data through pipeline...")
            pipeline.add_stage([input, transform, output])
            result_str = pipeline.process(data)
            print("Transform: Enriched with metadata and validation")
            print(f"Output: {result_str}")
        for pipeline in self.piplines:
            pipeline.stages = []


def main() -> None:
    data = [
        {"sensor": "temp", "value": 23.5, "unit": "°C"},
        [12, 78, 4.0, 15.0, -4, 2],
        "gabach,login,21h42"
    ]

    data_error = [
        {"error": "error", "value": "test", "unit": 12},
        [None, 24, 4, 5.0, None, 2],
        "..."
    ]

    JSON = JSONAdapter("JSON_01")
    CSV = CSVAdapter("CSV_01")
    STREAM = StreamAdapter("Stream_01")

    nexus = NexusManager()

    print("=== CODE NEXUS - ENTREPRISE PIPELINE SYSTEM ===")

    print("\nInitializing Nexus Manager...")
    print("Pipeline capacity: 1000 stream/second\n")

    print("Creating Data Processing Pipeline...")

    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")

    print()
    print("=== Multi-Format Data Processing ===")

    nexus.add_pipeline([JSON, CSV, STREAM])
    nexus.process_data(data)

    print()
    print("=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")

    start = time.time()
    chain_result = OutputStage().process(TransformStage().
                                         process(InputStage().
                                                 process([4, 10, 8, 7,
                                                          2, 5, 4])))
    end = time.time()
    t = round(end - start, 7)

    print()
    print(f"Chain result: {chain_result}")
    print(f"Performance: {round((0.0000069 / t) * 100, 2)}% efficiency, \
{'{:.7f}'.format(t)}s total processing time\n")

    print(" Error Recovery Test ".center(21 + 6, "="))
    print("simulating pipeline failur...")
    nexus.process_data(data_error)

    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
