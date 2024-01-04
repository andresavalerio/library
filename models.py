"""This module contains the base classes in the library application."""

from abc import ABC
from pymongo.collection import Collection


class RepositoryModel(ABC):
    """
    Base class for models in the library application.

    This class provides basic CRUD operations for interacting with
    the database.
    """

    collection: Collection = None

    def create(self, data: dict):
        """Create a new document in the collection."""
        return self.collection.insert_one(data)

    def read(self, id: str, data: dict = None, projection: dict = None):
        """Retrieve a document from the collection based on the given id."""
        return self.collection.find_one({"_id": id}, data, projection)

    def update(self, id: str, data: dict, projection: dict = None):
        """Update a document in the collection with the given ID."""
        self.collection.update_one({"_id": id}, {"$set": data}, projection)
        return self.read(id, data, projection)

    def delete(self, id: str):
        """Delete a document from the collection based on the given ID."""
        return self.collection.delete_one({"_id": id})


class ControllerModel(ABC):
    """Base class for controlers in the library application."""

    repository: RepositoryModel = None
