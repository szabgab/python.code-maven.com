import os
import pathlib
import time
import pytest


@pytest.fixture(params=["name"])
def generate(name):
    print(f"Fixture before test using {name}")
    yield
    print(f"Fixture after test using {name}")

@pytest.mark.parametrize("name", ["apple"])
def test_with_param(name, generate):
    print(f"Test using {name}")

@pytest.mark.parametrize("name", ["banana"])
def test_without_param(generate):
    print(f"Test not using param")

@pytest.mark.parametrize("name", ["banana"])
def test_with_param_without_fixture(name):
    print(f"Test using param {name} and not using fixture")

def test_without_param_without_fixture():
    print(f"Test not using param and not using fixture")

