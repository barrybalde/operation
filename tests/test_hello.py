"""
Test module for simple hello example.

Contains basic unit test for string_hello variable.
"""


THE_STRING = "Hello"



def test_hello():
    """
    @overview Just a `Hello` test 
    """

    assert isinstance(THE_STRING, str) is True, 'Oups, value does not a string'
