import pytest
from opyapi.routing import Route
from opyapi.routing import Router


def test_route_parsing():
    route = Route("/example/{pattern}")
    assert route.match("/example/test")

    route = Route("/example/{pattern}", pattern=r"\d+")
    assert route.match("/example/12")
    assert not route.match("/example/fail")


def test_route_match():
    route = Route("/pets/{pet_id}")
    route = route.match("/pets/11a22")
    assert route["pet_id"] == "11a22"

    route = Route("/pets/{pet_id}", pet_id=r"\d+")
    assert not route.match("/pets/11a22")
    route = route.match("/pets/22")
    assert route._attributes == {"pet_id": "22"}


def test_router():
    router = Router()
    router.add_route("GET", Route("/pets/{pet_id}"))
    router.add_route("get", Route("/pets"))
    route = router.match("GET", "/pets/12")

    assert route["pet_id"] == "12"
    assert router.match('get', '/pets')
