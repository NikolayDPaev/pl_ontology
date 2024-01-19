from owlready2 import *

class Feature(Thing):
    pass

class Abstraction(Feature):
    pass

instructions = Feature()

# statements

class Statements(Abstraction):
    pass

rules = Statements()
facts = Statements()
queries = Statements()
functionDefinition = Statements()

# different functions

functionsAsFirstOrderCitizens = Abstraction()
higherOrderFunctions = Abstraction() # maybe remove
pureFunctions = Abstraction()

# structures in the code

class CodeStructures(Abstraction):
    pass

blocks = CodeStructures()
procedures = CodeStructures()
loops = CodeStructures()

# immutability

class Immutability(Feature):
    pass

defaultImmutability = Immutability()
strictImmutability = Immutability()

inheritance = Feature()

# concurrency
class Concurrency(Feature):
    pass

threads = Concurrency()
coRoutines = Concurrency()
processes = Concurrency()
asyncFunctions = Concurrency()
monadConcurrency = Concurrency()

# types

class CustomTypes(Feature):
    pass

class ProductTypes(CustomTypes):
    pass

class Structures(ProductTypes):
    pass

class SumTypes(CustomTypes):
    pass

structures = Structures()
tuples = ProductTypes()
classes = Structures()

simpleEnums = Feature()

richEnums = SumTypes()
caseClasses = SumTypes()
unionTypes = SumTypes()