import os
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import Protocol, runtime_checkable

from app.services.util import generate_unique_id

class NotificationChannel(ABC):

    @abstractmethod
    def send(self, message: str) -> None:
        pass

    @abstractmethod
    def get_channel_name(self) -> str:
        pass

    @abstractmethod
    def is_available(self) -> bool:
        pass


