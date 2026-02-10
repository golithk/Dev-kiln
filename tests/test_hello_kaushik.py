from src.hello_kaushik import greet


def test_greet():
    """Test that greet returns the expected greeting."""
    assert greet() == "Hello, Kaushik!"
