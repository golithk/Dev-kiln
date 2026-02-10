from src.greeting import greet


def test_greet():
    """Test that greet returns the expected greeting."""
    assert greet("World") == "Hello, World!"


def test_greet_with_different_name():
    """Test greet with a different name."""
    assert greet("Alice") == "Hello, Alice!"
