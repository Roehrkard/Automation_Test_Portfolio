import pytest
from Transducer import TransducerTest


@pytest.fixture()
def td():
    td = TransducerTest()
    return td


def test_CanSetReciever(td):
    assert td.setReciever('DC') == 'DC' or 'AC' or 'no connection'


def test_CanTurnOnPump(td):
    assert td.turnOnPump('on') == 'on'


def test_CanIncPsi(td):
    assert td.incPsi(1) == 'pass'


def test_CanVExpected(td):
    assert td.VExpected(1, 1) == 'pass'


def test_CanTurnOffPump(td):
    assert td.turnOffPump('off') == 'off'
