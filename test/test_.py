from laptop_allocation import *
import pytest

people = [
    Person(name="Alice", age=30, preferred_operating_system=[OperatingSystem.MACOS, OperatingSystem.UBUNTU]),
    Person(name="Bob", age=22, preferred_operating_system=[OperatingSystem.ARCH, OperatingSystem.UBUNTU, OperatingSystem.MACOS]),
    Person(name="Bob", age=22, preferred_operating_system=[OperatingSystem.ARCH, OperatingSystem.MACOS]),
    Person(name="Bob", age=22, preferred_operating_system=[OperatingSystem.ARCH, OperatingSystem.UBUNTU]),
    Person(name="Bob", age=22, preferred_operating_system=[ OperatingSystem.UBUNTU]),
    Person(name="Bob", age=22, preferred_operating_system=[OperatingSystem.MACOS, OperatingSystem.UBUNTU]),
    Person(name="Bob", age=22, preferred_operating_system=[OperatingSystem.ARCH, OperatingSystem.MACOS]),
    Person(name="Bob", age=22, preferred_operating_system=[OperatingSystem.MACOS]),
]

laptops = [
    Laptop(id=1, manufacturer="Apple", model="MacBook Pro", screen_size_in_inches=13.3, operating_system=OperatingSystem.MACOS),
    Laptop(id=2, manufacturer="Dell", model="XPS 13", screen_size_in_inches=13.4, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Lenovo", model="ThinkPad", screen_size_in_inches=14.0, operating_system=OperatingSystem.ARCH),
    Laptop(id=4, manufacturer="Lenovo", model="ThinkPad", screen_size_in_inches=14.0, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=5, manufacturer="Lenovo", model="ThinkPad", screen_size_in_inches=14.0, operating_system=OperatingSystem.ARCH),
    Laptop(id=6, manufacturer="Lenovo", model="ThinkPad", screen_size_in_inches=14.0, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=7, manufacturer="Apple", model="MacBook Pro", screen_size_in_inches=13.3, operating_system=OperatingSystem.MACOS),
]


def test_more_laptops_than_people():
    sadness = allocate_laptops(people, laptops)

    assert isinstance(sadness, int)
    assert sadness >= 0
    assert sadness <= 100 * len(people)