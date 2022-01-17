#########IMPORT##########
import _Lexer
import Error
#########################

            
Scope = {"FUNCTIONS":{"F_OUT":"print","F_EXCEPTION":'Error.Error',"F_IN":'input',"F_COMPMODULE":"","F_GETLENGTH":"len","F_STRING":"str","F_INT":"int","F_LIST":"list","F_FLOAT":"float","F_DESTROY":"del","F_TYPE":"type",},"KEYWORDS":{"K_IF":"if","K_IN":"in","K_WHILE":"while","K_FOR":"for", "K_OR":"or","K_AND":"and","K_VAR":"var","K_FUNC":"function","K_RETURN":"return","K_BREAK":"break","K_DO":"do"}}

#########PARSER##########


Throw = 0
class Parser:
      def __init__(self,Passed):
            self.code = Passed.Pop
            self.idx = 0
            self.param = 0
            self.Parser = []
            self.exp = []
            self.run()
            

      def run(self):
            
            while self.idx < len(self.code):
                  
                  #print(len(self.code[self.idx]))
                  #print(self.code[self.idx][0])
                  if len(tuple(self.code[self.idx])) == 2:
                        self.idx+=1
                  
                  elif len(tuple(self.code[self.idx])) == 1:
                        try:
                        #if True:
                              #print('self.'+str(self.code[self.idx][0])+'('+str(self.code[self.idx-1])+','+str(self.code[self.idx+1])+')')

                              a = eval('self.'+str(self.code[self.idx][0])+'('+str(self.code[self.idx-1])+','+str(self.code[self.idx+1])+')')
                              
                              try:       
                              #if True:
                                          
                                    self.idx+=2                                                
                                    b = eval('self.'+str(self.code[self.idx][0])+'('+str(self.code[self.idx-1])+','+str(self.code[self.idx+1])+')')
                                    self.idx-=2
                                    a = eval('self.'+self.code[self.idx][0]+'('+str(self.code[self.idx-1])+','+str(b)+')')
                                          
                                    self.idx+=2                    
                                                            
                              except:pass
                                   
                              if Throw:
                                    raise SyntaxError()
                              self.Parser.append(a)
                              self.idx+=1
                        
                                            
                        except:
                        #if False:
                              Error.Error("Invalid Syntax","Bad Operation / Not used correctly",self.code[self.idx][0],False)
                              break
                        
                        else:
                              self.idx+=1
                        
            self.Pop = (tuple(self.Parser))
      
      def PLUS(self,l,r):
            lo = l
            ro = r
            l = l[1]
            r = r[1]
            
            #print(l,r)
            if lo[0] == "'" and ro[0] == "'":
                  return ('+',["'"+l+"'","'"+r+"'"])
            return ('+',[l,r])
      def MINUS(self,l,r):
            l = l[1]
            r = r[1]
            return ('-',[l,r])
      def MUL(self,l,r):
            l = l[1]
            r = r[1]
            return ('*',[l,r])
      def DIV(self,l,r):
            l = l[1]
            r = r[1]
            return ('/',[l,r])
      def POW(self,l,r):
            l = l[1]
            r = r[1]
            return ('**',[l,r])
      def MOD(self,l,r):
            l = l[1]
            r = r[1]
            return ('%',[l,r])
      def GN(self,l,r):
            l = l[1]
            r = r[1]
            return ('>',[l,r])
      def LN(self,l,r):
            l = l[1]
            r = r[1]
            return ('<',[l,r])
      def NOT(self,l,r):
            l = l[1]
            r = r[1]
            return ('!',[r])
      def EQUAL(self,l,r):
            l = l[1]
            r = r[1]
            return ('=',[l,r])
      def FUNC(self,r):
            return (Scope["FUNCTIONS"][self.idx])
      def LPARAN(self,r):
            print(r)
            #self.exp[0] 
            return (Scope["EXPR"][self.idx])
      
      
      
                              



#########################                                        
                  
##########EXEC###########
#Is in another Module :O
#########################
