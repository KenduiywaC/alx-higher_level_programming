#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args:
            self._update_with_args(args)
        elif kwargs:
            self._update_with_kwargs(kwargs)

    def _update_with_args(self, args):
        """Update attributes using args."""
        for i, arg in enumerate(args):
            if i == 0 and arg is not None:
                self.id = arg
            elif i == 1:
                self.size = arg
            elif i == 2:
                self.x = arg
            elif i == 3:
                self.y = arg

    def _update_with_kwargs(self, kwargs):
        """Update attributes using kwargs."""
        for attr, value in kwargs.items():
            if attr == 'id' and value is not None:
                self.id = value
            elif attr == 'size':
                self.size = value
            elif attr == 'x':
                self.x = value
            elif attr == 'y':
                self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

