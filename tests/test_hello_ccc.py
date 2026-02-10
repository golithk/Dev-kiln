from src.hello_ccc import greet


def test_greet():
    """Test that greet returns the expected greeting."""
    assert greet() == "Hello, CCC!"
