from src.hello_bbb import greet


def test_greet():
    """Test that greet returns the expected greeting."""
    assert greet() == "Hello, BBB!"
