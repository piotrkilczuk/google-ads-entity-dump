from __future__ import annotations


class ContextException(ValueError):
    message: str

    def __init__(self, message: str):
        self.message = message
