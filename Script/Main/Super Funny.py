#########IMPORT##########
import _Lexer
import Error
#########################
##########NODES##########
class BOOLNode():
      def __init__(self,Thing,right):
            
            self.Thing = "TRUE" if Thing == True else "FALSE"
            if Thing == 'NOT':
                  self.Thing = "NOT"
            if self.Thing == 'NOT':
                  #Return.idx+=1
                  Next = NEXTNode('NOT',right,right)

      def __repr__(self):
            return self.Thing
class NEXTNode():
      def __init__(self,Thing,After,right):
            self.Nodes = ['NOT']
            self.Thing = Thing
            self.right = right
            
      def __repr__(self):
            if self.Thing in self.Nodes:
                  boolien = BOOLNode(self.Thing,self.right)
                  return f'!({boolien})'
            
#########################
#########PARSER##########




class Parser:
      def __init__(self,Passed):
            self.code = Passed.Pop
            self.idx = 0
            print(self.code)
            self.Parser = []
            self.run()

      def run(self):
            
            while self.idx < len(self.code):
                  print(len(self.NBS(0)))
                  if len(self.NBS(0)) == 2:
                        pass
                  elif len(self.NBS(0)) == 1:
                        expr = self.NBS(0)
                        left = self.NBS(-1)
                        right = self.NBS(1)
                        
                        if self.NBS(0)[0] == 'NOT':
                              self.NEXTNode('NOT',right,self.NBS(1))
                              print(Next)
                  print(self.NBS(0)[0])
                  self.idx+=1
            print(self.Parser)
      def FindNodeType(self,Expected):
            return eval(Expected+'Node')

      def NBS(self,Grab):
            try:
                  return self.code[self.idx+Grab]
            except:
                  Error.Error("Invalid Syntax","Expected 'INT', 'STRING' or 'BOOL' but got", '("INT","0")', False)
                  return
      def NEXTNode(self,Thing,After,right):
            self.Thing = Thing
            self.right = right
            
            self.BOOLNode(self.Thing,self.right)
            if Thing == 'NOT':
                  return f'!({boolien})'
      def BOOLNode(self,Thing,right):
            self.Thing = "TRUE" if Thing == True else "FALSE"
            if Thing == 'NOT':
                  self.Thing = "NOT"
            if self.Thing == 'NOT':
                  #Return.idx+=1
                  self.idx+=1
                  self.NEXTNode('NOT',right,right)
            return self.Thing
#########################                                        
                  
##########EXEC###########
Popert = _Lexer.Lexer("!!?")

Return = Parser(Popert)
#########################
