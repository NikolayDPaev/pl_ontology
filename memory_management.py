from owlready2 import *

class MemoryManagement(Thing):
    pass

class AutomaticMemoryManagement(MemoryManagement):
    pass

class TracingGC(AutomaticMemoryManagement):
    pass

class SemiAutomaticMemoryManagement(MemoryManagement):
    pass

manualMemoryManagement = MemoryManagement()
referenceCounting = AutomaticMemoryManagement()
g1 = TracingGC()
borrowChecker = SemiAutomaticMemoryManagement()
