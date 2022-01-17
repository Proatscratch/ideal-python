import sys
Stop = 0
#####################DIGITS#####################
DIGITS = '1234567890-'
################################################
#####################CHARS######################
#       TOP PRIORTITY(Can be anywhere)  #LAST PRIORITY(Can be second Char or later)  
Chars = ('abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ', '1234567890')
################################################
#####################SCOPE######################
Scope = {"FUNCTIONS":{"out":"F_OUT","error":"F_EXCEPTION","input":"F_IN","getModule":"F_COMPMODULE","length":"F_GETLENGTH","string":"F_STRING","int":"F_INT","list":"F_LIST","float":"F_FLOAT","pop":"F_DESTROY","type":"F_TYPE",},"KEYWORDS":{"if":"K_IF","in":"K_IN","while":"K_WHILE","for":"K_FOR", "or":"K_OR","and":"K_AND","var":"K_VAR","function":"K_FUNC","return":"K_RETURN","break":"K_BREAK","do":"K_DO"},'VARIBLES':{'py':"<programming variable 'py'>",'assembly':"<programming variable 'assembly'>",'C':"<programming variable 'C'>"}}
####################MODULES#####################
import Error

################################################
#####################LEXER######################

class Lexer:
      def __init__(self,Passed):
            self.code = ' '+Passed+' '
            self.idx = 0
            self.Lexed = []
            self.definer = ''
            self.defe = 0
            self.defe2 = 0
            self.r = 0
            self.Stop = 0
            self.run()
            

      def run(self):
            
            while self.idx < len(self.code):
                  
                  itr = self.code[self.idx]
                  #print(itr)
                  if itr == '+':
                       self.Lexed.append(('PLUS',))
                       self.idx+=1
                  elif itr == '-':
                        self.Lexed.append(('MINUS',))
                        self.idx+=1
                  elif itr == '*':
                        self.Lexed.append(('MUL',))
                        self.idx+=1
                  elif itr == '/':
                        self.Lexed.append(('DIV',))
                        self.idx+=1
                  elif itr == '^':
                        self.Lexed.append(('POW',))
                        self.idx+=1
                  elif itr == '%':
                        self.Lexed.append(('MOD',)) #MODULOUS
                        self.idx+=1
                  elif itr in DIGITS or itr in ['"',"'"]:
                        pop = self.handleMultiLetter(itr)
                        self.Lexed.append(pop)
                        #try:
                        if True:
                              if self.defe2 == 1:
                                    Scope["VARIBLES"][self.definer] = (pop)
                                    self.defe2 = 0
                        #except:pass
                        
                  elif itr in '    ':
                        self.idx+=1
                  elif itr == '#':
                        break
                  elif itr == '?':
                        try:
                              if self.defe2 == 1:
                                    Scope["VARIBLES"][self.definer] = ('BOOL','TRUE')
                                    self.defe2 = 0
                        except:pass
                        self.Lexed.append(('BOOL','TRUE'))
                        self.idx+=1
                  elif itr == '!':
                        self.idx+=1
                        itr = self.code[self.idx]
                        if itr == '?':
                              try:
                                    if self.defe2 == 1:
                                          Scope["VARIBLES"][self.definer] = ('BOOL','FALSE')
                              except:pass
                              self.Lexed.append(('BOOL','FALSE'))
                        elif itr == '=':
                              self.idx+=1
                              itr = self.code[self.idx]
                              if itr =='=':
                                    self.Lexed.append(('INEQUAL'))
                                    
                              else:
                                    error = Error.Error("Illegal Character", "Unknown Character",'!=',Error = False)
                        else:
                              self.idx-=1
                              self.Lexed.append(('NOT',))
                        self.idx+=1
                  elif itr == '>':
                        self.Lexed.append(("GN",))# GREATER THAN
                        self.idx+=1
                  elif itr == '<':
                        self.Lexed.append(("LN",))#LESS THAN
                        self.idx+=1
                  elif itr == ':':
                        self.Lexed.append(("SEP",))#SEPERATER
                        self.idx+=1
                  elif itr == ';':
                        self.Lexed.append(("END",))
                        self.idx+=1
                  elif itr == '(':
                        self.Lexed.append(("LPARAN",))#LEFT PARANTHESES
                        self.idx+=1
                  elif itr == ')':
                        self.Lexed.append(("RPARAN",))#RIGHT PARANTHESES
                        self.idx+=1
                  elif itr == '_':
                        self.Lexed.append(("INT","0"))
                        try:
                              if self.defe2 == 1:
                                    Scope["VARIBLES"][self.definer] = ('INT','0')
                                    self.defe2 = 0
                        except:pass
                        self.idx +=1
                  elif itr == '{':
                        self.Lexed.append(("LBRACE",))
                        self.idx +=1
                  elif itr == '}':
                        self.Lexed.append(("RBRACE",))
                        self.idx +=1
                  
                  elif itr in Chars[0]:
                        
                        p = self.handleMultiLetter(itr)
                        if p == None:
                              break
                        self.Lexed.append(p)
                        #self.idx+=1
                  elif itr == '=':
                        itr = self.code[self.idx+1]
                        if itr == '=':
                              itr = self.code[self.idx+2]
                              if itr == '=':
                                    #itr = self.code[self.idx+2]
                                    #if itr == '=':
                                    self.Lexed.append(("EQUAL",))
                              
                                    
                                    self.idx += 2
                              
                              
                                    
                              else:
                                    
                                    error = Error.Error("Illegal Character", "Unknown Character",'==',Error = False)
                                    break
                        else:       
                              
                              if self.defe == 1:
                                    
                                    self.Lexed.append("ASSIGN",)
                                    self.defe2 = 1
                              
                              
                                          

                              
                              
                             
                              self.defe = 0
                        self.idx += 1
                        
                  elif self.Stop == 1:
                        break
                        
                  
                  else:
                        
                        #self.Pop = ()
                        error = Error.Error("Illegal Character", "Unknown Character",itr,Error = False)
                              

                        break
            self.Pop = tuple(self.Lexed)
      def handleMultiLetter(self,char,):
            currentList = self.Lexed
            Res = ''
            DTCNT = 0
            if self.code[self.idx-1] == '-':
                  Res+='-'
                  del self.Lexed[-1]
            if char in DIGITS:
                  while (self.code[self.idx] in DIGITS+'.'):

                        Res+=self.code[self.idx]
                        if self.code[self.idx] in '.':
                              DTCNT+=1
                        if DTCNT > 1:
                              return
                        self.idx+=1
                                    
                  if DTCNT == 1:
                        return ("FLOAT",Res)
            
                  return ("INT",Res)
            elif char in ['"',"'"]:
                  self.idx+=1
                  while not(self.code[self.idx] in['"',"'"]) and self.code[self.idx] != "\\":
                        Res+=self.code[self.idx]
                        self.idx+=1
                  self.idx+=1
                  return ("STR","'"+Res+"'")
            elif char in Chars[0]:
                  #print(self.code[self.idx+1] in Chars[1])
                  while (self.code[self.idx] in Chars[0] or self.code[self.idx] in Chars[1]):
                        
                        try:
                              Res+=self.code[self.idx]
                        except:
                              break
                        self.idx+=1

                  if Res == '':
                        return
                  try:
                        return ("FUNC",Scope["FUNCTIONS"][Res])
                  except KeyError:
                        try:
                              if Scope["KEYWORDS"][Res] == Scope["KEYWORDS"]["var"]:
                                    self.r = 1
                              return ("KEY",Scope["KEYWORDS"][Res])
                        except KeyError:
                              
                              try:
                                    
                                    if self.r == 0:
                                          return Scope["VARIBLES"][Res]
                                    else:
                                          JUNKS

                                                
                                                
                                    
                                    
                                    
                              except:
                                    try:
                                          
                                          if self.r == 1:
                                                #Scope["VARIBLES"][Res] = ''
                                                
                                                self.definer = Res
                                                self.defe = 1
                                                self.defe2 = 0
                                                self.definer = Res
                                                return ('Var','Var','Var')
                                          
                                          #return
                                          
                                          
                                    except SyntaxError:pass
                                    
                                    #if self.defe == 0:
            self.Stop = 1
            Error.Error("Undefined ", "Undefined Name", Res)
            self.Pop = ()      
                                    
                              
                              
                  
                  
################################################
###################EXEC#########################      
#IS IN ANOTER MODULE :)
################################################
