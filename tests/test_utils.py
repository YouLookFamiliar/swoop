# -*- coding: utf-8 -*-

import pytest
import subprocess

import swoopi


def test_picamera_connected(monkeypatch):
    monkeypatch.setattr('test_utils.subprocess.check_output',
                        lambda _: 'supported=1 detected=1')
    assert swoopi.utils.picamera_connected() == True


def test_picamera_not_connected(monkeypatch):
    monkeypatch.setattr('test_utils.subprocess.check_output',
                       lambda _: 'supported=1 detected=0')
    assert swoopi.utils.picamera_connected() == False


def test_picamera_wrong_platform(monkeypatch):
    def subprocess_exception(_):
        raise subprocess.CalledProcessError(-1, 'vcgencmd', '')

    monkeypatch.setattr('test_utils.subprocess.check_output',
                        subprocess_exception)

    assert swoopi.utils.picamera_connected() == False

