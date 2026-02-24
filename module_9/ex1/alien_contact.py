#!/usr/bin/env python3

from pydantic import BaseModel, Field, model_validator, ValidationError
from typing_extensions import Self
from datetime import datetime
from enum import Enum


class Contact(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: Contact
    signal_strength: float = Field(ge=0, le=10)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(max_length=500, default=None)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def alien_contact_validator(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC' (Alien Contact)")

        if self.contact_type == Contact.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if self.contact_type == Contact.TELEPATHIC and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesse")

        if self.signal_strength > 7 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )

        return self

    def __str__(self) -> str:
        return (
            f"ID: {self.contact_id}\n"
            f"Type: {self.contact_type.value}\n"
            f"Location: {self.location}\n"
            f"Signal: {self.signal_strength}/10\n"
            f"Duration: {self.duration_minutes} minutes\n"
            f"Witnesses: {self.witness_count}\n"
            f"Message: '{self.message_received}'"
        )


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")

    valid_data = {
        "contact_id": "AC_2024_001",
        "timestamp": "2026-02-23T14:30:00",
        "location": "Area 51, Nevada",
        "contact_type": "radio",
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": "Greetings from Zeta Reticuli",
        "is_verified": True
    }

    invalid_data = {
        "contact_id": "AC_2024_002",
        "timestamp": "2026-02-23T14:30:00",
        "location": "Nevada Desert",
        "contact_type": "telepathic",
        "signal_strength": 5.0,
        "duration_minutes": 20,
        "witness_count": 1,
        "is_verified": False
    }

    contact_1 = AlienContact(**valid_data)
    print("Valid contact report:")
    print(contact_1)

    print()
    print("======================================")
    print("Expected validation error:")

    try:
        contact_2: AlienContact = AlienContact(**invalid_data)
    except ValidationError as err:
        for error in err.errors():
            print(error["msg"])
    else:
        print(contact_2)


if __name__ == "__main__":
    main()
