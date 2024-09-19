import unittest
try:
    from models.base import Base
except ModuleNotFoundError:
    try:
        from base import Base
    except ModuleNotFoundError:
        try:
            from ...models.base import Base
        except Exception:
            try:
                Base = __import__('../models/base').Base
            except ModuleNotFoundError:
                try:
                    Base = __import__('models/base').Base
                except Exception as e:
                    print("Could not import. Last exception info:")
                    print(type(e).__name__+ ':')
                    print(e)
                    print("\nRaising errors.")
                    raise e


class MyTestCase(unittest.TestCase):
    def test_something(self):
        b = Base(10)
        self.assertEqual(b.id, 10)  # add assertion here
        b.id = 3
        self.assertEqual(b.id, 3)


if __name__ == '__main__':
    unittest.main()
