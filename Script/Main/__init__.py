import _Lexer as l
import _Parser as p
import Interpreter as I
import Error as E

while True:
      
      b = input('assembly >> C >> py >> Script >')
      #try:
      if True:
            i = l.Lexer(b)
            a = p.Parser(i)
            o = I.Interpreter(a)
            
      #except:
      if False:
            E.Error('Python ','...','')
            
      
 
