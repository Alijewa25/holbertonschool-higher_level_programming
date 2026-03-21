#!/usr/bin/python3

"""Define a class Square."""
class Square:
    """Square Class

    Bu class kvadrat obyektini təsvir edir.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize (constructor)

        Args:
            size (int): kvadratın tərəfi
            position (tuple): (x, y) koordinatı
        """
        self.size = size          # setter çağırılır
        self.position = position  # setter çağırılır

    # ---------------- SIZE ----------------
    @property
    def size(self):
        """Size getter (oxumaq üçün)"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size setter (dəyər təyin etmək üçün)

        Şərtlər:
        - integer olmalıdır
        - 0-dan kiçik ola bilməz
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    # ---------------- POSITION ----------------
    @property
    def position(self):
        """Position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """Position setter

        Şərtlər:
        - tuple olmalıdır
        - uzunluğu 2 olmalıdır
        - bütün elementlər integer olmalıdır
        - bütün elementlər >= 0 olmalıdır
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError(
                "position must be a tuple of 2 non-negative integers"
            )

        self.__position = value

    # ---------------- AREA ----------------
    def area(self):
        """Kvadratın sahəsini qaytarır"""
        return self.__size * self.__size

    # ---------------- PRINT ----------------
    def my_print(self):
        """Kvadratı # ilə çap edir"""

        # Əgər size 0-dırsa boş sətir çıxır
        if self.__size == 0:
            print("")
            return

        # Y istiqamətində boş sətirlər (yəni aşağı sürüşmə)
        for _ in range(self.__position[1]):
            print("")

        # Kvadratın çapı
        for _ in range(self.__size):

            # X istiqamətində boşluqlar (sağa sürüşmə)
            for _ in range(self.__position[0]):
                print(" ", end="")

            # # işarələri
            for _ in range(self.__size):
                print("#", end="")

            # Növbəti sətrə keç
            print("")
