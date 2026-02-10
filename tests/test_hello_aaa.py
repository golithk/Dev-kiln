from src.hello_aaa import greet


def test_greet():
    """Test that greet returns the expected greeting."""
    assert greet() == "Hello, AAA!"
