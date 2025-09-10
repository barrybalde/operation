


class DataManipulator():
    """
    @overview Une classe permettant de manipuler des objets comme des dictionnaires.
    """


    def __init__(self, data_user:dict):
        """
        @overview constructeur

        :param data_user {dict} : Données utilisateurs.

        Exemple : user_dict = {
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
        """

        self.get_data_user = data_user



    def get_info_user(self, key_unique_username:str, key_value_username:str):
        """
        @overview une méthode qui permet de retourner une valeur donnée(à partir d'une clé).

        :param key_unique_username {str} : Le username de l'utilisateur.
        :param key_value_username {str} : La clé nous permettant de récupérer la valeur qu'on 
            souhaite (une donnée spécifique , ex : email).

        :return {str} : La valuer à partir du paramètre 'key_value_username'
        """

        for key_username, value_username in self.get_data_user.items():

            if  key_username == key_unique_username:
                return value_username[key_value_username]


