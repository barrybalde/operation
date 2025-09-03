


string_hello = "Hello"



def test_hello():
    """
    @overview Juste a `Hello` test 
    """

    assert isinstance(string_hello, str) is True, 'Oups, value does not a string'
