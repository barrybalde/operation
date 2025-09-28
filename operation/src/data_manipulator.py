


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



    def get_info_user(self, key_unique_username:str, key_value_username:str) -> str | None:
        """
        @overview une méthode qui permet de retourner une valeur donnée(à partir d'une clé).

        :param key_unique_username {str} : Le username de l'utilisateur.
        :param key_value_username {str} : La clé nous permettant de récupérer la valeur qu'on 
            souhaite (une donnée spécifique , ex : email).

        :return {str | None} : La valuer à partir du paramètre 'key_value_username', ou None
        si la clé du dictionnaire de base n'existe pas.
        """

        # Test si l'utilisateur existe
        if self.key_exists(self.get_data_user, key_unique_username) is False:
            return None
        

        for key_username, value_username in self.get_data_user.items():

            if  key_username == key_unique_username:
                
                # Vérification de l'existence de la clé (ex : email)
                if not self.key_exists(value_username, key_value_username):
                    return None

                return value_username[key_value_username]
        
        
        return None
    
    

    def get_user_data(self, key_unique_username: str) -> dict | None:
        """
        @overview Une méthode qui retourne toutes les données d'un utilisateur.

        :param key_unique_username {str} : Le username unique de l'utilisateur à récupérer.

        :return {dict | None} : Le dictionnaire contenant toutes les informations de l'utilisateur,
        ou None si l'utilisateur n'existe pas.
        """

        for key_username, value_username in self.get_data_user.items():
            if key_username == key_unique_username:
                return value_username
            
        return None
    


    def key_exists(self, dict_data:dict, key_dict: str) -> bool:
        """
        @overview Une méthode qui vérifie si une clé existe dans un dictionnaire.

        :param key_data {dict} : Le dictionnaire.
        :param key_dict {str} : La clé du dictionnaire à vérifier.

        :return {bool} : True si la clé existe, False sinon.
        """
        
        for current_key in dict_data.keys():
            if current_key == key_dict:
                return True
            
        return False



    def add_user(self, key_unique_username:str, user_info:dict) -> bool | None: 
        """
        @overview une méthode qui permet d'ajouter un nouveau utilisateur un dictionnaire.

        :param key_unique_username {str} : La clé du dictionnaire
        :param user_info{dict} : Un dictionnaire contenant les information de l'utilisateur.

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

        #
        if self.key_exists(self.get_data_user, key_unique_username):
            return False
        
        #
        if not isinstance(user_info, dict):
            return False
        

        self.get_data_user[key_unique_username] = user_info 


    
    def get_users(self):
        """
        @overview une méthode qui permet de retourner tous les utilisateurs.

        :return {dict} : Le dictionnaire.

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

        return self.get_data_user
    


    def delete_user(self, key_unique_username:str):
        """
        @overview une méthode qui permet de supprimer un utilisateur du dictionnaire.

        :param key_unique_username {str} : le username de L’utilisateur à supprimer.

        :return {bool} : false si l'utilisateur n'existe pas

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

        Pattern : method('0001')
        """

        if not self.key_exists(self.get_data_user, key_unique_username):
            return False
        
        # Suppression de l'utilisateur
        del self.get_data_user[key_unique_username]



    def update_user_data(self, key_unique_user: str, key_data_to_update: str, new_value_to_put: str) -> bool:
        """
        @overview Une méthode qui permet de mettre à jour les informations d'un utilisateur.
        
        :param key_unique_user {str} : Le username unique de l’utilisateur.
        :param key_data_to_update {str} : La clé représentant l'information à modifier.
        :param new_value_to_put {str} : La nouvelle information à mettre remplaçant l'ancienne (par le biais de `key_data_to_update`).

        :return {bool} : `True` si la si la modification a été bien effectuer ou `False` si l'utilisateur ou la clé n'existe pas.
        """

        if not self.key_exists(self.get_data_user, key_unique_user):
            return False
        

        for key_username, data_username in self.get_data_user.items():

            if key_username == key_unique_user:

                if key_data_to_update in data_username:
                    data_username[key_data_to_update] = new_value_to_put
                    return True
                
                else: return False
                
        
        return False
    