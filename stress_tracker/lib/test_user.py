import unittest
from user import User


class TestGame(unittest.TestCase):
    def test_init_default_object(self):
        # Instantiate an object.
        object = User(
            3,
            "murwan",
            "Eisa",
            "gender",
            "eisa@gmail.com",
            "software development",
            "bachelor",
            "mur123",
            23,
            "first year",
        )
        message = "given object is not instance of player class."
        self.assertIsInstance(object, User, message)


if __name__ == "__main__":
    unittest.main()
