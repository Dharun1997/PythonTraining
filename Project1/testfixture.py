import pytest

@pytest.yield_fixture()
def setup():
    print("Execute this always first")
    yield
    print("Execute this always last")

def testcase1(setup):
    print("This is first test case")

def testcase2(setup):
    print("This is second test case")

