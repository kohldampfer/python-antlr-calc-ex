from antlr4 import *
from grammar.ExpressionsListener import ExpressionsListener
from grammar.ExpressionsLexer import ExpressionsLexer
from grammar.ExpressionsParser import ExpressionsParser
import sys

class CalcExpressionsListener(ExpressionsListener):

   hadARun = False

   def enterStart(self, ctx):
      pass
      
   def exitStart(self, ctx):
      pass
      
   def calculate(self, ctx):
      # iterator which iterates over
      i = 0
      val1 = 0
      val2 = 0
      op = ''
      result = 0
   
      if ctx.getChildCount() < 3:
         return
         
      if ctx.getChildCount() > 3:
         raise Exception("CalcExpressionsListener.calculate: Assumed only 3 childs there were, but there were {0}".format(ctx.getChildCount))
         
      for c in ctx.getChildren():
         if i == 0:
            if c.getChildCount() > 2:
               val1 = self.calculate(c)
            else:
               val1 = int(c.getText())
         elif i == 1:
            op = c.getText()
         elif i == 2:
            if c.getChildCount() > 2:
               val2 = self.calculate(c)
            else:
               val2 = int(c.getText())
            # after retrieving all necessary data, calc and return
            # assuming that 
            return self.calc(val1, val2, op)
         else:
            raise Exception("CalcExcpressionListener.calculate: Not definition for iteration '{0}'".format(i))
            
         i = i + 1
      
      raise Exception("CalcExpressionListener.calculate: You should had already a result.")
   
      
   def enterExpr(self, ctx):
      result = 0
      if self.hadARun == False:
         result = self.calculate(ctx)
         self.hadARun = True
         print("Result is: '{0}'".format(result))
      
   
   def exitExpr(self, ctx):
      pass
      
   def calc(self, val1, val2, op):
      if op == '+':
         return val1 + val2
      elif op == '-':
         return val1 - val2
      elif op == '*':
         return val1 * val2
      elif op == '/':
         return val1 / val2
      else:
         raise Exception("CalcExpressionsListener.calc: Operator '{0}' is not implemented.".format(op))

def main():
   giveMeInput = input("Enter an expression\n")
   
   i_stream = InputStream(giveMeInput)
   
   lexer = ExpressionsLexer(i_stream)
   t_stream = CommonTokenStream(lexer)
   parser = ExpressionsParser(t_stream)
   tree = parser.start()
   
   calculator = CalcExpressionsListener()
   walker = ParseTreeWalker()
   walker.walk(calculator, tree)
   
   
if __name__ == '__main__':
   main()