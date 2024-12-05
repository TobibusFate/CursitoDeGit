# Generated from F:/Archivos/Code/Test/Matrix.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MatrixParser import MatrixParser
else:
    from MatrixParser import MatrixParser

# This class defines a complete listener for a parse tree produced by MatrixParser.
class MatrixListener(ParseTreeListener):

    # Enter a parse tree produced by MatrixParser#matrix.
    def enterMatrix(self, ctx:MatrixParser.MatrixContext):
        pass

    # Exit a parse tree produced by MatrixParser#matrix.
    def exitMatrix(self, ctx:MatrixParser.MatrixContext):
        pass


    # Enter a parse tree produced by MatrixParser#filas.
    def enterFilas(self, ctx:MatrixParser.FilasContext):
        pass

    # Exit a parse tree produced by MatrixParser#filas.
    def exitFilas(self, ctx:MatrixParser.FilasContext):
        pass


    # Enter a parse tree produced by MatrixParser#fila.
    def enterFila(self, ctx:MatrixParser.FilaContext):
        pass

    # Exit a parse tree produced by MatrixParser#fila.
    def exitFila(self, ctx:MatrixParser.FilaContext):
        pass



del MatrixParser