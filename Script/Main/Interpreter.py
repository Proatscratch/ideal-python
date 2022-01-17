import _Parser
import Error
Scope = {"FUNCTIONS":{"F_OUT":"print","F_EXCEPTION":'Error.Error',"F_IN":'input',"F_COMPMODULE":"","F_GETLENGTH":"len","F_STRING":"str","F_INT":"int","F_LIST":"list","F_FLOAT":"float","F_DESTROY":"del","F_TYPE":"type",},"KEYWORDS":{"K_IF":"if","K_IN":"in","K_WHILE":"while","K_FOR":"for", "K_OR":"or","K_AND":"and","K_VAR":"var","K_FUNC":"function","K_RETURN":"return","K_BREAK":"break","K_DO":"do"}}

import math
infinity = math.inf
            
class Interpreter:
      def __init__(self,Passed):
            self.code = Passed.Pop
            self.idx = 0
            #print(self.code)
            self.Interpret = []
            self.run()
      def run(self):
            while self.idx<len(self.code):
                  
                  try:
                  
                        itr = self.code[self.idx]

                        self.Interpret.append(self.OPER(itr))
                  except:
                  
                        Error.Error("Runtime","Error while interpreting",self.code[self.idx])
                  self.idx+=1
                  #print(self.Interpret)

            for a in self.Interpret:
                  print(eval(a))


      def OPER(self,itr):
            o1 = itr[1][0]
            o2 = itr[1][1]
            if itr[0] == '/' and int(o2) == 0:
                  
                  return 'infinity'
            if isinstance(o1,tuple):
                  o1 = self.OPER(itr[1][0])
            if isinstance(o2,tuple):
                  o2 = self.OPER(itr[1][1])
            
            return str(str(o1)+itr[0]+str(o2))
      
      def __repr__(self):
            return str('<Interpreter Value='+str(self.Interpret)+', Passed='+str(self.code)+'>')
      
      
            
      #def FUNC(self,itr):
            
                        
