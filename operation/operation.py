"""
@overview Un fichier contenant une classe permettant d'effectuer
des opérations mathématiques.
"""





class Operation:
    """
    @overview Cette classe permet de faire des operations mathématiques comme 
    le `pgcd`, la `factorielle`.
    """


    def factorial(self, number:int) -> int | None:
        """
        @overview Méthode permettant de calculer la factorielle d'un nombre entier positif.

        :param number {int} : La valeur pour laquelle on calcule la factorielle : n >= 0.

        :return {int | None} : La factorielle du nombre en entrée sera retournée si c'est
        un entier positif, sinon `None` sera retourné.

        Use cage:
            success :  
                -> action : factorial(3) // (3 * 2 * 1)
                -> return : 6
            
            error:
                -> action : factorial(-3)
                -> return : None
        """

        # Declaration de variables
        result = 1


        # Test du paramètre en entrée
        if (number < 0) or ( not isinstance(number, int) ):
            return None

        for i in range(2, number + 1):
            result = result * i

        return result
