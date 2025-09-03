"""
Test module for simple hello example.

Contains basic unit test for string_hello variable.
"""


the_string = "Hello"



def test_hello():
    """
    @overview Juste a `Hello` test 
    """

    assert isinstance(the_string, str) is True, 'Oups, value does not a string'

