#!/usr/bin/env python

from semantic_ner_search_demo import __version__
from semantic_ner_search_demo.libs.my_lib import MyLib
from semantic_ner_search_demo.main import something


def test_version():
    assert __version__ == "0.1.0"


def test_something_with_string(str_input):
    assert something(str_input) is True


def test_something_with_input(int_input):
    assert something(int_input) is False


def test_MyLib():
    my_lib = MyLib()
    assert my_lib.do_something() == "My Lib is doing something!"
