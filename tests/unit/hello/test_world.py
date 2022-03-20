import pytest
from my_python_example.hello import world


def test_hello_world():
    actual = world.hello_world('Name')
    assert actual == 'Hello Name!'
