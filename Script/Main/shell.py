import _Lexer as l
import _Parser as p
import Interpreter as I
import Error as E

while True:
      
      b = input('Script >> Main >> shell.py >')
      try:
      #if True:
            i = l.Lexer(b)
            #print(i.Pop)
            a = p.Parser(i)
            #print(a.Pop)
            o = I.Interpreter(a)
            print(o)
            
      except:
      #if False:
            E.Error('Python ','...','')
            
      
 
