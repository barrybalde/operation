"""
@overview Pour faire du test de méthodes 
"""

from operation.src.data_manipulator import DataManipulator





TEST_USER_DICT = {

    '0001': {
        'prenom': "Hawa",
        'nom': "Bah",
        "email": "barry@gmail.com",
    },

    '0002': {
        'prenom': "Sagacity",
        'nom': "Quantic",
        'email': "quantic@proton.me",
    }
}

OBJ_DATA_MANIPULATOR = DataManipulator(TEST_USER_DICT)



def test_get_info_user():
    """
    @overview Test pour la méthode `get_info_user()`
    """

    #
    if hasattr(OBJ_DATA_MANIPULATOR, "get_info_user"):
        assert OBJ_DATA_MANIPULATOR.get_info_user("0001", "email") == "barry@gmail.com", "Erreur, valeur incorrecte"

    
    if hasattr(OBJ_DATA_MANIPULATOR, "get_info_user"):
        assert OBJ_DATA_MANIPULATOR.get_info_user("0005", "email") == None, "Erreur, valeur incorrecte"