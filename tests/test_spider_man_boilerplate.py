#!/usr/bin/env python

"""Tests for `spider_man_boilerplate` package."""


import unittest
from click.testing import CliRunner

from spider_man_boilerplate import spider_man_boilerplate
from spider_man_boilerplate import cli


class TestSpider_man_boilerplate(unittest.TestCase):
    """Tests for `spider_man_boilerplate` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'spider_man_boilerplate.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
