import pytest
from funcion2 import suma

def test_fx():
    assert type(suma(1,2)) == int


test_fx()