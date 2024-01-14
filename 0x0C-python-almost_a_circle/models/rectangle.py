#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        self._validate_and_set('width', value)

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        self._validate_and_set('height', value)

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self._x

    @x.setter
    def x(self, value):
        self._validate_and_set('x', value)

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self._y

    @y.setter
    def y(self, value):
        self._validate_and_set('y', value)

    def _validate_and_set(self, attr, value):
        """Validate and set attribute values."""
        if type(value) != int:
            raise TypeError(f"{attr} must be an integer")
        if value < 0 and attr in {'x', 'y'}:
            raise ValueError(f"{attr} must be >= 0")
        if value <= 0 and attr in {'width', 'height'}:
            raise ValueError(f"{attr} must be > 0")
        setattr(self, f"_{attr}", value)

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for _ in range(self.y)]
        for _ in range(self.height):
            [print(" ", end="") for _ in range(self.x)]
            [print("#", end="") for _ in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args:
            self._update_with_args(args)
        elif kwargs:
            self._update_with_kwargs(kwargs)

    def _update_with_args(self, args):
        """Update attributes with positional arguments."""
        attrs = ['id', 'width', 'height', 'x', 'y']
        for i in range(len(args)):
            if i < len(attrs):
                setattr(self, attrs[i], args[i])
            else:
                break

    def _update_with_kwargs(self, kwargs):
        """Update attributes with keyword arguments."""
        valid_keys = ['id', 'width', 'height', 'x', 'y']
        for key, value in kwargs.items():
            if key in valid_keys:
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
