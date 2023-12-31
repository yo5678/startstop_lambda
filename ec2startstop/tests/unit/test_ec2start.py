import pytest

from ec2startstop.src import ec2start


def test_ec2_stop():
    res = ec2start.ec2_start()
    assert res == "start_ec2"
