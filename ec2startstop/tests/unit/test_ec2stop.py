import pytest

from ec2startstop.src import ec2stop


def test_ec2_stop():
    res = ec2stop.ec2_stop()
    assert res == "stop_ec2"
