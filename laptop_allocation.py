from dataclasses import dataclass
from enum import Enum
from typing import List, Dict
from itertools import permutations

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    # Sorted in order of preference, most preferred is first.
    preferred_operating_system: List[OperatingSystem]


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
    ''' 
    Allocate laptops to the people by preference.
    Args:
        permutation (List[Laptop]): A list of laptops assigned to people.
        people (List[Person]): A list of people to whom laptops are assigned.

    Returns:
        int: minimised the total sadness of all people.'''
    def calculate_sadness(permutation: List[Laptop], people: List[Person]) -> int:
        sadness = 0
        for person, laptop in zip(people, permutation):
            if laptop.operating_system in person.preferred_operating_system:
                sadness += person.preferred_operating_system.index(laptop.operating_system)
            else:
                sadness += 100
        return sadness

    min_sadness = float("inf")
    if len(people) > len(laptops):
        for permutation in  permutations(laptops):
            min_sadness = min(calculate_sadness(permutation, people), min_sadness)
    elif len(people) < len(laptops):
        for permutation in permutations(laptops, len(people)):
            min_sadness = min(calculate_sadness(permutation, people), min_sadness)
    else: 
        pass
    return min_sadness



people = [
    Person(name="Alice", age=30, preferred_operating_system=[OperatingSystem.MACOS, OperatingSystem.UBUNTU]),
    Person(name="Bob", age=22, preferred_operating_system=[OperatingSystem.ARCH, OperatingSystem.UBUNTU])
]

laptops = [
    Laptop(id=1, manufacturer="Apple", model="MacBook Pro", screen_size_in_inches=13.3, operating_system=OperatingSystem.MACOS),
    Laptop(id=2, manufacturer="Dell", model="XPS 13", screen_size_in_inches=13.4, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Lenovo", model="ThinkPad", screen_size_in_inches=14.0, operating_system=OperatingSystem.ARCH)
]
print(allocate_laptops(people, laptops))