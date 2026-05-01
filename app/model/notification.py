import os
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import Protocol, runtime_checkable

from app.services.util import generate_unique_id

class NotificationError(Exception):
    pass

class ChannelUnavailableError(NotificationError):
    pass

class DeliveryError(NotificationError):
    pass

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

class FileChannel(NotificationChannel):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def is_available(self) -> bool:
        directory = os.path.dirname(self.file_path) or "."

        return os.path.exists(directory) and os.access(directory, os.W_OK)

    def get_channel_name(self) -> str:
        return f"file:{self.file_path}"

    def send(self, message: str) -> None:

        if not self.is_available():
            raise ChannelUnavailableError()

        try:
            with open(self.file_path, "a") as f:
                f.write(message + "\n")
        except Exception:
            raise DeliveryError()