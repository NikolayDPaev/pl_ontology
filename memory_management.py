from owlready2 import *

from pl_ontology.features import Abstraction

class MemoryManagement(Thing):
    pass

class AutomaticMemoryManagement(MemoryManagement, Abstraction):
    pass

class TracingGC(AutomaticMemoryManagement):
    pass

class SemiAutomaticMemoryManagement(MemoryManagement):
    pass

manualMemoryManagement = MemoryManagement()
referenceCounting = AutomaticMemoryManagement()
g1 = TracingGC()
borrowChecker = SemiAutomaticMemoryManagement()
