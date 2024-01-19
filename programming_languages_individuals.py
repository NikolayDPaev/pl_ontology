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
], usedFor = [
    gamingDevelopment,
    desktopApplications,
    osDevelopment,
    embeddedDevelopment,
    compilerDevelopment,
    databaseManagement
])

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
    weakTypeStrictness
], hasErrorHandlingType = [
    nullPointers,
    exceptions
], usedFor = [
    gamingDevelopment,
    desktopApplications,
    enterpriseApplications,
    osDevelopment,
    embeddedDevelopment,
    compilerDevelopment,
    databaseManagement
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
], usedFor = [
    gamingDevelopment,
    desktopApplications,
    enterpriseApplications,
    webApplications
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
], usedFor = [
    webApplications,
    cloudApplications,
    desktopApplications,
    enterpriseApplications,
    mobileApplications
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
], usedFor = [
    webApplications,
    desktopApplications,
    enterpriseApplications,
    mobileApplications
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
], usedFor = [
    webApplications,
    aiDevelopment,
    scientificComputing,
    desktopApplications,
    enterpriseApplications,
    osDevelopment
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
], usedFor = [
    osDevelopment
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
], usedFor = [
    osDevelopment
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
], usedFor = [
    embeddedDevelopment,
    aiDevelopment,
    gamingDevelopment,
    webApplications,
    osDevelopment,
    compilerDevelopment,
    databaseManagement
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
], usedFor = [
    cloudApplications,
    enterpriseApplications,
    webApplications
])

ruby = ProgrammingLanguage(hasFeature = [
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
    ByteCodeInterpreter
], typeSystemType = [
    dynamicTypeSystem
], typeStrictness = [
    strongTypeStrictness
], hasErrorHandlingType = [
    nullPointers,
    exceptions
], usedFor = [
    webApplications
])

php = ProgrammingLanguage(hasFeature = [
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
    dynamicTypeSystem
], typeStrictness = [
    weakTypeStrictness
], hasErrorHandlingType = [
    nullPointers,
    exceptions
], usedFor = [
    webApplications
])

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
], usedFor = [
    scientificComputing,
    highlyConcurrentApplications,
    compilerDevelopment,
    financialSoftware
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
    research,
    aiDevelopment
])

closure = ProgrammingLanguage(hasFeature = [
    functionsAsFirstOrderCitizens,
    higherOrderFunctions,
    strictImmutability
], hasMemoryManagement = [
    referenceCounting
], runsOn = [
    jvm
], typeSystemType = [
    dynamicTypeSystem
], typeStrictness = [
    strongTypeStrictness
], hasErrorHandlingType = [
    errorsAsValues
], usedFor = [
    highlyConcurrentApplications
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
], usedFor = [
    cloudApplications,
    highlyConcurrentApplications
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
], usedFor = [
    webApplications
])

typescript = ProgrammingLanguage(hasFeature = [
    blocks,
    loops,
    classes,
    functionsAsFirstOrderCitizens,
    higherOrderFunctions,
    asyncFunctions,
    tuples,
    unionTypes
], hasMemoryManagement = [
    TracingGC
], runsOn = [
    Interpreter
], typeSystemType = [
    staticTypeSystem
], typeStrictness = [
    strongTypeStrictness
], hasErrorHandlingType = [
    exceptions
], usedFor = [
    webApplications
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
], usedFor = [
    webApplications
])

prolog = ProgrammingLanguage(hasFeature = [
    rules,
    facts,
    strictImmutability
], hasMemoryManagement = [
    referenceCounting
], runsOn = [
    Interpreter
], hasTypeSystemType = [
    dynamicTypeSystem
], usedFor = [
    research,
    aiDevelopment,
    compilerDevelopment
])

sql = ProgrammingLanguage(hasFeature = [
    queries,
    strictImmutability
], runsOn = [
    Interpreter
], usedFor = [
    databases
])

matlab = ProgrammingLanguage(hasFeature = [
    loops,
    procedures,
    pureFunctions,
    classes,
    inheritance,
    threads
], runsOn = [
    Interpreter
], hasTypeStrictness = [
    strongTypeStrictness
], hasTypeSystemType = [
    dynamicTypeSystem
], usedFor = [
    research,
    scientificComputing
])

wolframLanguage = ProgrammingLanguage(hasFeature = [
    loops,
    procedures,
    pureFunctions,
    threads
], runsOn = [
    Interpreter
], hasTypeStrictness = [
    strongTypeStrictness
], hasTypeSystemType = [
    dynamicTypeSystem
], usedFor = [
    research,
    scientificComputing
])

r = ProgrammingLanguage(hasFeature = [
    blocks,
    loops,
    procedures,
    classes,
    inheritance
], runsOn = [
    Interpreter
], hasTypeStrictness = [
    strongTypeStrictness
], hasTypeSystemType = [
    dynamicTypeSystem
], usedFor = [
    research,
    scientificComputing
])