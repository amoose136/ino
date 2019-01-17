# -*- coding: utf-8; -*-

from unittest import TestCase

from ino.environment import Version


class TestVersion(TestCase):
    def test_parsing(self):
        self.assertEqual(Version.parse('0022'), (0, 22, 0))
        self.assertEqual(Version.parse('0022ubuntu0.1'), (0, 22, 0))
        self.assertEqual(Version.parse('0022-macosx-20110822'), (0, 22, 0))
        self.assertEqual(Version.parse('1.0'), (1, 0, 0))
        self.assertEqual(Version.parse('1:1.0.5+dfsg2-1'), (1, 0, 5))

    def test_int_conversion(self):
        self.assertEqual(Version(0, 22, 0).as_int(), 22)
        self.assertEqual(Version(1, 0, 0).as_int(), 100)
        self.assertEqual(Version(1, 0, 5).as_int(), 105)
        self.assertEqual(Version(1, 5, 1).as_int(), 151)