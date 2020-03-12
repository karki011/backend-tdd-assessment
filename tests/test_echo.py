#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess
# Your test case class goes here


class TestEcho(unittest.TestCase):
    def setUp(self):
        self.parser = echo.create_parser()

    def test_help(self):
        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()
        self.assertEquals(stdout, usage)

    def test_upper_short(self):
        args = ["-u", "hello"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.upper)
        self.assertEquals(echo.main(args), "HELLO")

    def test_upper_long(self):
        args = ["--upper", 'hello world']
        actual = echo.main(args)
        expected = "HELLO WORLD"
        self.assertEqual(actual, expected)

    def test_lower_short(self):
        args = ["-l", "HELLO"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.lower)
        self.assertEquals(echo.main(args), 'hello')

    def test_lower_long(self):
        args = ["--lower", "HELLO"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.lower)
        self.assertEquals(echo.main(args), 'hello')

    def test_title_short(self):
        args = ["-t", "hello"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.title)
        self.assertEquals(echo.main(args), 'Hello')

    def test_title_long(self):
        args = ["--title", "hello"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.title)
        self.assertEquals(echo.main(args), 'Hello')

    def test_all_args(self):
        args = ["-tul", 'hElLo']
        namespace = self.parser.parse_args(args)
        self.assertTrue(all([namespace.lower,
                             namespace.upper,
                             namespace.title]))
        self.assertEquals(echo.main(args), 'Hello')

    def test_no_args(self):
        args = ['hello world']
        namespace = self.parser.parse_args(args)
        self.assertFalse(
            all([namespace.lower, namespace.upper, namespace.title]))
        self.assertEquals(echo.main(args), args[0])


if __name__ == '__main__':
    unittest.main()
