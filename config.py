"""Module providing a configuration class for reading and accessing JSON configuration files."""
import json


class Config:
    """Class representing a configuration manager for JSON configuration files."""

    def __init__(self, filename):
        with open(filename, encoding="utf-8") as file:
            self.config = json.load(file)

    def get_config(self):
        """Retrieve the configuration data as a Python dictionary."""
        return self.config

    def update_config(self, filename):
        """Update the configuration data with new values."""
        with open(filename, encoding="utf-8") as file:
            self.config = json.load(file)
