"""
@overview Le fichier `main` où la ou les classes peuvent être
instanciées.
"""

from operation.Operation import Operation





if __name__ == "__main__":
    
    obj = Operation()

    print(obj.factorial(4))