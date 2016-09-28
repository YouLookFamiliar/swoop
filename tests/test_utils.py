# -*- coding: utf-8 -*-

import os
import errno
import subprocess

import pytest
import swoopi


@pytest.mark.parametrize('supported, detected', [
    (True, True), (True, False), (False, False)
])
def test_picamera_status(monkeypatch, supported, detected):
    vcgencmd_output = 'supported={} detected={}'.format(
        int(supported), int(detected))

    monkeypatch.setattr('test_utils.subprocess.check_output',
                        lambda _: vcgencmd_output)

    res_support, res_detect = swoopi.utils.picamera_status()
    assert res_support == supported
    assert res_detect == detected


def test_picamera_environment_exceptions(monkeypatch):
    def nonzero_exception(_):
        raise subprocess.CalledProcessError(-1, 'vcgencmd', '')

    monkeypatch.setattr('test_utils.subprocess.check_output',
                        nonzero_exception)

    nonzero_support, nonzero_detect = swoopi.utils.picamera_status()
    assert nonzero_support is False and nonzero_detect is False

    def notfound_exception(_):
        raise OSError(errno.ENOENT, os.strerror(errno.ENOENT))

    monkeypatch.setattr('test_utils.subprocess.check_output',
                        notfound_exception)

    notfound_support, notfound_detect = swoopi.utils.picamera_status()
    assert nonzero_support is False and nonzero_detect is False
