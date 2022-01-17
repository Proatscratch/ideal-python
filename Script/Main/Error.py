import sys
class Error:
      def __init__(self,name, reason,where, Error = True):
            print(str(name)+(int(Error)*'Error')+': '+str(reason)+" '"+str(where)+"'", file = sys.stderr)
