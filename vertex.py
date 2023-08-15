class vertex:
    _max: int = 100
    _min: int = -100

    def __init__(self, x_val: int, y_val:int) -> None:
        self.x = x_val
        self.y = y_val

    def __str__(self):
        return f"({self.x}, {self.y})"
    @classmethod
    def max(cls) -> int:
        return cls._max

    @classmethod
    def min(cls) -> int:
        return cls._min

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, x_val: int) -> None:
        if self._min <= x_val <= self._max:
            self._x = x_val
    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, y_val: int) -> None:
        if self._min <= y_val <= self._max:
            self._y = y_val
