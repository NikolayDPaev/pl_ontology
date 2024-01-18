from owlready2 import *

class Feature(Thing):
    pass

instructions = Feature()
statements = Feature()
rules = Feature()
facts = Feature()
functionsAsFirstOrderCitizens = Feature()
higherOrderFunctions = Feature()
pureFunctions = Feature()
procedures = Feature()
loops = Feature()

class Immutability(Feature):
    pass

defaultImmutability = Immutability()
strictImmutability = Immutability()

inheritance = Feature()

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

enums = SumTypes()
caseClasses = SumTypes()