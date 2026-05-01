import os
from dataclasses import dataclass, field
from datetime import datetime
from typing import Protocol, runtime_checkable

from app.services.util import generate_unique_id

class ConsoleChannel(NotificationChannel):

    def send(self, message: str) -> None:
        if not self.is_available():
            raise ChannelUnavailableError()

        try:
            print(message)
        except Exception:
            raise DeliveryError()

    def get_channel_name(self) -> str:
        return "console"

    def is_available(self) -> bool:
        return True