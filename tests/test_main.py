import pytest
from main import get_pkmn

def test_get_pkmn():
    data = get_pkmn("pikachu")
    assert data['name'] == 'pikachu'
    assert "height" in data
    assert "weight" in data