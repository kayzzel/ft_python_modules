#!/usr/bin/env python3

from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(max_length=200, default=None)

    def __str__(self) -> str:
        base = (
            f"ID: {self.station_id}\n"
            f"Name: {self.name}\n"
            f"Crew: {self.crew_size} people\n"
            f"Power: {self.power_level}%\n"
            f"Oxygen: {self.oxygen_level}%\n"
            f"Status: \
{'Operational' if self.is_operational else 'Non-Operational'}\n"
        )
        if self.notes:
            base += f"Note: {self.notes}\n"
        return base


def main() -> None:
    valid_data: dict = {
            "station_id": "ID_001",
            "name": "this is a name",
            "crew_size": 6,
            "power_level": 50.50,
            "oxygen_level": 18.20,
            "last_maintenance": "2026-02-23 14:30:00",
            "notes": "a test note"
            }

    invalid_data: dict = {
            "station_id": "ID_002",
            "name": "this is a name",
            "crew_size": 21,
            "power_level": 50.50,
            "oxygen_level": 18.20,
            "last_maintenance": "2026-02-23 14:30:00",
            }

    print(
            "Space Station Data Validation\n"
            "========================================\n"
            "Valid station created:"
            )

    try:
        station_1: SpaceStation = SpaceStation(**valid_data)
    except ValidationError as err:
        for error in err.errors():
            print(error["msg"])
    else:
        print(station_1)

    print(
            "========================================\n"
            "Expected validation error:"
            )

    try:
        station_2: SpaceStation = SpaceStation(**invalid_data)
    except ValidationError as err:
        for error in err.errors():
            print(error["msg"])
    else:
        print(station_2)


if __name__ == "__main__":
    main()
