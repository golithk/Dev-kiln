from src.hello import say_hello


def test_say_hello():
    """Test that say_hello returns the expected greeting."""
    assert say_hello() == "Hello, World!"
