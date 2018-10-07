#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `myproject` package."""

import pytest
import mathlib



@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_calc_total():
	total = mathlib.calc_total(4,5)
	assert(total,9)
