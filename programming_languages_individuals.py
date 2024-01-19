from owlready2 import *
from memory_management import *
from others import *
from running_environment import *

from programming_language import *

c = FastLanguage(hasFeature = [
    blocks,
    procedures,
    loops,
    structures,
    processes
], hasMemoryManagement = [
    manualMemoryManagement
], runsOn = [
    NativeEnvironment
], typeSystemType = [
    staticTypeSystem
], typeStrictness = [
    weakTypeStrictness
], hasErrorHandlingType = [
    nullPointers
]
)

c_pp = FastLanguage(hasFeature = [
    blocks,
    procedures,
    loops,
    classes,
    functionsAsFirstOrderCitizens,
    higherOrderFunctions,
    inheritance,
    simpleEnums,
    threads,
    coRoutines
], hasMemoryManagement = [
    manualMemoryManagement
], runsOn = [
    NativeEnvironment
], typeSystemType = [
    staticTypeSystem
], typeStrictness = [
    strongTypeStrictness
], hasErrorHandlingType = [
    nullPointers,
    exceptions
])

c_sharp = ProgrammingLanguage(hasFeature = [
    blocks,
    loops,
    classes,
    functionsAsFirstOrderCitizens,
    higherOrderFunctions,
    inheritance,
    simpleEnums,
    threads,
    asyncFunctions,
    coRoutines
], hasMemoryManagement = [
    TracingGC
], runsOn = [
    ByteCodeInterpreter
], typeSystemType = [
    staticTypeSystem
], typeStrictness = [
    strongTypeStrictness
], hasErrorHandlingType = [
    nullPointers,
    exceptions
])

java = ProgrammingLanguage(hasFeature = [
    blocks,
    loops,
    classes,
    functionsAsFirstOrderCitizens,
    higherOrderFunctions,
    inheritance,
    simpleEnums,
    threads
], hasMemoryManagement = [
    TracingGC
], runsOn = [
    jvm
], typeSystemType = [
    staticTypeSystem
], typeStrictness = [
    strongTypeStrictness
], hasErrorHandlingType = [
    nullPointers,
    exceptions
])

kotlin = ProgrammingLanguage(hasFeature = [
    blocks,
    loops,
    classes,
    functionsAsFirstOrderCitizens,
    higherOrderFunctions,
    inheritance,
    simpleEnums,
    threads,
    caseClasses
], hasMemoryManagement = [
    TracingGC
], runsOn = [
    jvm
], typeSystemType = [
    staticTypeSystem
], typeStrictness = [
    strongTypeStrictness
], hasErrorHandlingType = [
    exceptions,
    errorsAsSumTypes
])

python = ProgrammingLanguage(hasFeature = [
    blocks,
    loops,
    classes,
    functionsAsFirstOrderCitizens,
    higherOrderFunctions,
    inheritance,
    threads,
    asyncFunctions,
    tuples
], hasMemoryManagement = [
    referenceCounting
], runsOn = [
    LineByLineInterpreter
], typeSystemType = [
    dynamicTypeSystem
], typeStrictness = [
    strongTypeStrictness
], hasErrorHandlingType = [
    exceptions
])


bash = ProgrammingLanguage(hasFeature = [
    blocks,
    loops
], hasMemoryManagement = [
    manualMemoryManagement
], runsOn = [
    LineByLineInterpreter
], typeStrictness = [
    weakTypeStrictness
], hasErrorHandlingType = [
    errorsAsValues
])


powershell = ProgrammingLanguage(hasFeature = [
    blocks,
    loops,
    classes,
    inheritance
], hasMemoryManagement = [
    TracingGC
], runsOn = [
    LineByLineInterpreter
], typeSystemType = [
    dynamicTypeSystem
], typeStrictness = [
    weakTypeStrictness
], hasErrorHandlingType = [
    exceptions
])


rust = ProgrammingLanguage(hasFeature = [
    blocks,
    loops,
    structures,
    functionsAsFirstOrderCitizens,
    higherOrderFunctions,
    richEnums,
    threads,
    asyncFunctions,
    tuples,
    defaultImmutability
], hasMemoryManagement = [
    borrowChecker
], runsOn = [
    NativeEnvironment
], typeSystemType = [
    staticTypeSystem
], typeStrictness = [
    strongTypeStrictness
], hasErrorHandlingType = [
    errorsAsSumTypes
])

go = ProgrammingLanguage(hasFeature = [
    blocks,
    loops,
    structures,
    functionsAsFirstOrderCitizens,
    higherOrderFunctions,
    coRoutines
], hasMemoryManagement = [
    TracingGC
], runsOn = [
    NativeEnvironment
], typeSystemType = [
    staticTypeSystem
], typeStrictness = [
    strongTypeStrictness
], hasErrorHandlingType = [
    errorsAsValues
])

# ruby = ProgrammingLanguage()
# php = ProgrammingLanguage()

haskell = ProgrammingLanguage(hasFeature = [
    tuples,
    richEnums,
    functionsAsFirstOrderCitizens,
    higherOrderFunctions,
    lazyEvaluation,
    strictImmutability,
    monadConcurrency
], hasMemoryManagement = [
    TracingGC
], runsOn = [
    Interpreter
], typeSystemType = [
    staticTypeSystem
], typeStrictness = [
    strongTypeStrictness
], hasErrorHandlingType = [
    errorsAsSumTypes
])

scheme = ProgrammingLanguage(hasFeature = [
    functionsAsFirstOrderCitizens,
    higherOrderFunctions,
    strictImmutability
], hasMemoryManagement = [
    referenceCounting
], runsOn = [
    Interpreter
], typeSystemType = [
    dynamicTypeSystem
], typeStrictness = [
    strongTypeStrictness
], hasErrorHandlingType = [
    errorsAsValues
])

closure = ProgrammingLanguage(hasFeature = [
    functionsAsFirstOrderCitizens,
    higherOrderFunctions,
    strictImmutability
], hasMemoryManagement = [
    referenceCounting
], runsOn = [
    Interpreter
], typeSystemType = [
    dynamicTypeSystem
], typeStrictness = [
    strongTypeStrictness
], hasErrorHandlingType = [
    errorsAsValues
])

scala = ProgrammingLanguage(hasFeature = [
    blocks,
    loops,
    classes,
    functionsAsFirstOrderCitizens,
    higherOrderFunctions,
    richEnums,
    caseClasses,
    monadConcurrency,
    asyncFunctions,
    tuples,
    defaultImmutability
], hasMemoryManagement = [
    TracingGC
], runsOn = [
    jvm
], typeSystemType = [
    staticTypeSystem
], typeStrictness = [
    strongTypeStrictness
], hasErrorHandlingType = [
    errorsAsSumTypes
])

javascript = ProgrammingLanguage(hasFeature = [
    blocks,
    loops,
    classes,
    functionsAsFirstOrderCitizens,
    higherOrderFunctions,
    asyncFunctions,
], hasMemoryManagement = [
    TracingGC
], runsOn = [
    Interpreter
], typeSystemType = [
    dynamicTypeSystem
], typeStrictness = [
    weakTypeStrictness
], hasErrorHandlingType = [
    exceptions
])

elm = ProgrammingLanguage(hasFeature = [
    tuples,
    richEnums,
    functionsAsFirstOrderCitizens,
    higherOrderFunctions,
    lazyEvaluation,
    strictImmutability,
    monadConcurrency
], hasMemoryManagement = [
    TracingGC
], runsOn = [
    Interpreter
], typeSystemType = [
    staticTypeSystem
], typeStrictness = [
    strongTypeStrictness
], hasErrorHandlingType = [
    errorsAsSumTypes
])

prolog = ProgrammingLanguage(hasFeature = [
    rules,
    facts,
    strictImmutability
], hasMemoryManagement = [
    referenceCounting
], runsOn = [
    Interpreter
])

sql = ProgrammingLanguage(hasFeature = [
    queries,
    strictImmutability
], runsOn = [
    Interpreter
])

matlab = ProgrammingLanguage(hasFeature = [
    loops

], runsOn = [
    Interpreter
])
wolframMathematica = ProgrammingLanguage()
r = ProgrammingLanguage()