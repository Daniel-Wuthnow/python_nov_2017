def varargs(arg1, *restOfArg):
   print "Got "+arg1+" "+ ", ".join(restOfArg)
   print arg1
   print restOfArg

varargs("one", "two", "three")
# OUTPUT: restOfArg is of <type 'tuple'>
