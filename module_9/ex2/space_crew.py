#!/usr/bin/env python3

from pydantic import BaseModel, Field, model_validator, ValidationError
from typing_extensions import Self
from datetime import datetime
from enum import Enum


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_validate_rules(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        if not [
                member for member in self.crew
                if member.rank in [Rank.CAPTAIN, Rank.COMMANDER]
                ]:
            raise ValueError("Must have at least one Commander or Captain")
        if (self.duration_days > 365 and
            len(
                [member for member in self.crew if member.years_experience > 4]
                ) < len(self.crew) / 2):
            raise ValueError(
                    "Long missions (> 365 days) "
                    "need 50% experienced crew (5+ years)")
        if [member for member in self.crew if not member.is_active]:
            raise ValueError("All crew members must be active")

        return self

    def __str__(self) -> str:
        crew_info = "\n".join(
            f"- {member.name} ({member.rank.value}) - {member.specialization}"
            for member in self.crew
        )

        return (
            f"Mission: {self.mission_name}\n"
            f"ID: {self.mission_id}\n"
            f"Destination: {self.destination}\n"
            f"Duration: {self.duration_days} days\n"
            f"Budget: ${self.budget_millions}M\n"
            f"Crew size: {len(self.crew)}\n"
            f"Crew members:\n"
            f"{crew_info}"
        )


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")

    valid_data: dict = {
        "mission_id": "M2024_MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "launch_date": "2026-03-01T10:00:00",
        "duration_days": 900,
        "budget_millions": 2500.0,
        "crew": [
            {
                "member_id": "C01",
                "name": "Sarah Connor",
                "rank": "commander",
                "age": 45,
                "specialization": "Mission Command",
                "years_experience": 20,
                "is_active": True
            },
            {
                "member_id": "C02",
                "name": "John Smith",
                "rank": "lieutenant",
                "age": 35,
                "specialization": "Navigation",
                "years_experience": 8,
                "is_active": True
            },
            {
                "member_id": "C03",
                "name": "Alice Johnson",
                "rank": "officer",
                "age": 30,
                "specialization": "Engineering",
                "years_experience": 6,
                "is_active": True
            }
        ]
    }

    invalid_data: dict = {
        **valid_data,
        "crew": [
            {
                "member_id": "C02",
                "name": "John Smith",
                "rank": "lieutenant",
                "age": 35,
                "specialization": "Navigation",
                "years_experience": 8,
                "is_active": True
            }
        ]
    }

    try:
        mission_1: SpaceMission = SpaceMission(**valid_data)
    except ValidationError as e:
        print(e.errors()[0]["msg"])
    else:
        print("Valid mission created:")
        print(mission_1)

    print()
    print("=========================================")
    print("Expected validation error:")

    try:
        mission_2: SpaceMission = SpaceMission(**invalid_data)
    except ValidationError as err:
        print(err.errors()[0]["msg"])
    else:
        print(mission_2)


if __name__ == "__main__":
    main()
