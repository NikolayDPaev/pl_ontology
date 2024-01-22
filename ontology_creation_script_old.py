from owlready2 import *

onto = get_ontology("http://example.org/programming_languages.owl")

with onto:
    ### Features
    class Feature(Thing): pass
    class Abstraction(Feature): pass

    lazyEvaluation = Feature("lazy_evaluation")
    inheritance = Abstraction("inheritance")

    # statements
    class Statements(Abstraction): pass
    rules = Statements("rules")
    facts = Statements("facts")
    queries = Statements("queries")
    functionDefinition = Statements("function_definitions")

    # different functions
    functionsAsFirstClassCitizens = Abstraction("functions_as_first_order_citizens")
    higherOrderFunctions = Abstraction("higher_order_functions") # maybe remove
    pureFunctions = Abstraction("pure_functions")

    # structures in the code
    class CodeStructures(Abstraction): pass
    blocks = CodeStructures("blocks")
    procedures = CodeStructures("procedures")
    loops = CodeStructures("loops")

    # immutability
    class Immutability(Feature): pass
    defaultImmutability = Immutability("default_immutability")
    strictImmutability = Immutability("strict_immutability")

    # concurrency
    class Concurrency(Feature): pass
    threads = Concurrency("threads")
    coRoutines = Concurrency("coroutines")
    processes = Concurrency("processes")
    asyncFunctions = Concurrency("async_functions")
    monadConcurrency = Concurrency("monad_concurrency")

    # types
    class CustomTypes(Feature): pass
    class ProductTypes(CustomTypes): pass
    class Structures(ProductTypes): pass
    structures = Structures("structs")
    tuples = ProductTypes("tuples")
    classes = Structures("classes")
    simpleEnums = CustomTypes("simple_enums")

    class SumTypes(CustomTypes): pass
    richEnums = SumTypes("rich_enums")
    caseClasses = SumTypes("case_classes")
    unionTypes = SumTypes("union_types")

    # execution type
    class ExecutionType(Thing): pass
    lineByLineExecution = ExecutionType("line_by_line_execution")
    evaluationOfExpression = ExecutionType("evaluation_of_expression")
    reasoner = ExecutionType("reasoner")

    # memory management
    class MemoryManagement(Thing): pass
    class AutomaticMemoryManagement(MemoryManagement, Abstraction): pass
    class TracingGC(AutomaticMemoryManagement): pass
    class SemiAutomaticMemoryManagement(MemoryManagement): pass
    manualMemoryManagement = MemoryManagement("manual_memory_management")
    referenceCounting = AutomaticMemoryManagement("reference_counting")
    g1 = TracingGC("garbage_first_GC")
    borrowChecker = SemiAutomaticMemoryManagement("borrow_checker")

    # type system
    class TypeChecking(Thing): pass
    staticTypeChecking = TypeChecking("static_type_checking")
    dynamicTypeChecking = TypeChecking("dynamic_type_checking")
    # TypeChecking.is_a.append(OneOf([staticTypeChecking, dynamicTypeChecking]))

    class TypeSafety(Thing): pass
    strongTypeSafety = TypeSafety("strong_type_safety")
    weakTypeSafety = TypeSafety("weak_type_safety")
    # TypeSafety.is_a.append(OneOf([weakTypeSafety, strongTypeSafety]))

    # error handling
    class ErrorHandling(Thing): pass
    nullPointers = ErrorHandling("null_pointers")
    exceptions = ErrorHandling("exceptions")
    class ErrorInReturnType(ErrorHandling): pass
    errorsAsSumTypes = ErrorInReturnType("errors_as_sum_types")
    errorsAsValues = ErrorInReturnType("errors_as_values")

    # use cases
    class UseCase(Thing): pass
    webApplications = UseCase("web_applications")
    mobileApplications = UseCase("mobile_applications")
    desktopApplications = UseCase("desktop_applications")
    enterpriseApplications = UseCase("enterprise_level_applications")
    cloudApplications = UseCase("cloud_applications")
    scientificComputing = UseCase("scientific_computing")
    aiDevelopment = UseCase("AI_and_ML_field")
    osDevelopment = UseCase("OS_development")
    gameDevelopment = UseCase("game_development")
    databaseManagement = UseCase("database_management_systems_development")
    compilerDevelopment = UseCase("compilers_and_interpreters_development")
    embeddedDevelopment = UseCase("embedded_development")
    financialSoftware = UseCase("financial_and_banking_software")
    research = UseCase("research")
    databases = UseCase("databases")
    highlyConcurrentApplications = UseCase("highly_concurrent_applications")

    # users
    # class User(Thing): pass
    # class Developer(User): pass
    # webDev = Developer()
    # enterpriseSoftwareDev = Developer()
    # mobileDev = Developer()
    # gameDev = Developer()
    # sysAdmin = User()
    # researcher = User()
    # dataAnalyst = User()

    # running environment
    class RunningEnvironment(Thing): pass
    class Interpreter(RunningEnvironment): pass
    class LineByLineInterpreter(Interpreter): pass
    class ByteCodeInterpreter(Interpreter): pass
    class NativeEnvironment(RunningEnvironment): pass
    bash_interpreter = LineByLineInterpreter("bash_interpreter")
    python_interpreter = LineByLineInterpreter("python_interpreter")
    jvm = ByteCodeInterpreter("jvm")
    x86 = NativeEnvironment("x86")
    x64 = NativeEnvironment("x64")
    arm = NativeEnvironment("arm")
    mips = NativeEnvironment("mips")

    ### Programming language
    class ProgrammingLanguage(Thing): pass

    ### Properties

    class used_for(ProgrammingLanguage >> UseCase): pass

    class has_similar_syntax_to(ProgrammingLanguage >> ProgrammingLanguage):
        reflexive = True
        symmetric = True

    class inspired_by(ProgrammingLanguage >> ProgrammingLanguage):
        transitive = True

    class inspired(ProgrammingLanguage >> ProgrammingLanguage):
        inverse_property = inspired_by
        transitive = True

    class from_the_same_creators_as(ProgrammingLanguage >> ProgrammingLanguage):
        reflexive = True
        symmetric = True
        transitive = True

    class inter_op_with(ProgrammingLanguage >> ProgrammingLanguage): pass

    class runs_on(ProgrammingLanguage >> RunningEnvironment):
        functional = True

    class has_feature(ProgrammingLanguage >> Feature): pass

    class has_execution_type(ProgrammingLanguage >> ExecutionType):
        functional = True

    # class defaultEvaluationType(ProgrammingLanguage):

    class has_error_handling_type(ProgrammingLanguage >> ErrorHandling):
        functional = True

    class has_type_checking(ProgrammingLanguage >> TypeChecking):
        functional = True

    class has_type_safety(ProgrammingLanguage >> TypeSafety):
        functional = True

    class has_memory_management(ProgrammingLanguage >> MemoryManagement):
        functional = True

    ### Classes
    class HighLevelLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_feature.min(1, Abstraction)
        ]

    class LowLevelLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_feature.max(1, Abstraction)
        ]

    class ConcurrentLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_feature.only(Concurrency)
        ]

    class ImperativeLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_execution_type.value(lineByLineExecution)
        ]

    class StructuredLanguage(ImperativeLanguage):
        equivalent_to = [
            has_feature.only(CodeStructures)
        ]

    class AssemblyLanguage(ImperativeLanguage, LowLevelLanguage):
        equivalent_to = [
            ImperativeLanguage &
            LowLevelLanguage &
            runs_on.only(NativeEnvironment)
        ]

    class ProceduralLanguage(StructuredLanguage):
        equivalent_to = [
            has_feature.value(procedures)
        ]

    class DeclarativeLanguage(HighLevelLanguage):
        equivalent_to = [
            has_feature.only(Statements)
        ]

    class FunctionalInspiredLanguage(HighLevelLanguage):
        equivalent_to = [
            has_feature.value(functionsAsFirstClassCitizens) &
            has_feature.value(higherOrderFunctions)
        ]

    # inference that FunctionalLanguage is Declarative
    class FunctionalLanguage(FunctionalInspiredLanguage):
        equivalent_to = [
            FunctionalInspiredLanguage &
            has_execution_type.value(evaluationOfExpression) &
            has_feature.only(Immutability)
        ]

    class PureFunctionalLanguage(FunctionalLanguage):
        equivalent_to = [
            FunctionalLanguage &
            has_feature.value(pureFunctions) &
            has_feature.value(strictImmutability)
        ]

    class LazyEvaluatedLanguage(PureFunctionalLanguage):
        equivalent_to = [
            PureFunctionalLanguage &
            has_feature.value(lazyEvaluation)
        ]

    # inference that LogicLanguage is Declarative
    class LogicLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_feature.value(facts) &
            has_feature.value(rules)
        ]

    # inference that QueryLanguage is Declarative
    class QueryLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_feature.value(queries)
        ]

    class OOPInspiredLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_feature.only(Structures)
        ]

    class OOPLanguage(OOPInspiredLanguage):
        equivalent_to = [
            has_feature.value(classes) &
            has_feature.value(inheritance)
        ]

    class MultiParadigmLanguage(ProgrammingLanguage):
        equivalent_to = [
            OOPInspiredLanguage &
            FunctionalInspiredLanguage
        ]

    class StaticallyTypedLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_type_checking.value(staticTypeChecking)
        ]

    class DynamicallyTypedLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_type_checking.value(dynamicTypeChecking)
        ]

    class StronglyTypedLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_type_safety.value(strongTypeSafety)
        ]

    class WeaklyTypedLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_type_safety.value(weakTypeSafety)
        ]

    class SafeTypeCheckingLanguage(StronglyTypedLanguage, StaticallyTypedLanguage):
        equivalent_to = [
            StaticallyTypedLanguage &
            StronglyTypedLanguage
        ]

    class ErrorSafeLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_error_handling_type.value(errorsAsSumTypes)
        ]

    class SafeLanguage(ProgrammingLanguage):
        equivalent_to = [
            ErrorSafeLanguage &
            SafeTypeCheckingLanguage
        ]

    class HasAlgebraicTypes(ProgrammingLanguage):
        equivalent_to = [
            has_feature.only(ProductTypes) &
            has_feature.only(SumTypes)
        ]

    class ModernFunctionalLanguage(ProgrammingLanguage):
        equivalent_to = [
            PureFunctionalLanguage &
            SafeTypeCheckingLanguage &
            HasAlgebraicTypes
        ]

    class CompiledLanguage(ProgrammingLanguage):
        pass

    class LanguageWithRuntime(HighLevelLanguage):
        pass

    class CompiledToByteCodeLanguage(CompiledLanguage):
        equivalent_to = [
            runs_on.only(ByteCodeInterpreter)
        ]

    class CompiledToMachineCodeLanguage(CompiledLanguage):
        equivalent_to = [
            runs_on.only(NativeEnvironment)
        ]

    class FastLanguage(ProgrammingLanguage):
        equivalent_to = [
            CompiledToMachineCodeLanguage &
            Not(LanguageWithRuntime)
        ]

    class InterpretedLanguage(LanguageWithRuntime):
        equivalent_to = [
            runs_on.only(Interpreter)
        ]

    # inference that Scripting < Interpreted
    class ScriptingLanguage(ProgrammingLanguage):
        equivalent_to = [
            runs_on.only(LineByLineInterpreter)
        ]

    class ShellLanguage(ProgrammingLanguage):
        equivalent_to = [
            ScriptingLanguage &
            used_for.value(osDevelopment)
        ]

    # inference that JVMLanguage < Interpreted
    class JVMLanguage(ProgrammingLanguage):
        equivalent_to = [
            runs_on.value(jvm)
        ]

    class GarbageCollectedLanguage(LanguageWithRuntime):
        equivalent_to = [
            has_memory_management.only(AutomaticMemoryManagement)
        ]

    # inference that ReferenceCounted < GarbageCollected
    class ReferenceCountedLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_memory_management.value(referenceCounting)
        ]

    class MultifunctionalLanguage(ProgrammingLanguage):
        equivalent_to = [
            used_for.min(2, UseCase)
        ]

    class PopularLanguage(ProgrammingLanguage):
        equivalent_to = [
            used_for.min(3, UseCase)
        ]

    class InfluencedLanguage(ProgrammingLanguage):
        equivalent_to = [
            inspired_by.min(2, ProgrammingLanguage)
        ]

    class InfluentialLanguage(ProgrammingLanguage):
        equivalent_to = [
            inspired.min(2, ProgrammingLanguage)
        ]

    class FatherLanguage(Thing):
        equivalent_to = [
            inspired.min(3, ProgrammingLanguage)
        ]

    # Individuals
    c = ProgrammingLanguage("c", has_feature = [
        blocks,
        procedures,
        loops,
        structures,
        processes
    ], has_execution_type = [lineByLineExecution]
    , has_memory_management = [manualMemoryManagement]
    , runs_on = [NativeEnvironment]
    , has_type_checking = [staticTypeChecking]
    , has_type_safety = [weakTypeSafety]
    , has_error_handling_type = [nullPointers]
    , used_for = [
        gameDevelopment,
        desktopApplications,
        osDevelopment,
        embeddedDevelopment,
        compilerDevelopment,
        databaseManagement
    ])

    class CurlyBracketLanguages(ProgrammingLanguage):
        equivalent_to = [
            has_similar_syntax_to.only(c)
        ]

    c_pp = ProgrammingLanguage("c++", has_feature = [
        blocks,
        procedures,
        loops,
        classes,
        functionsAsFirstClassCitizens,
        higherOrderFunctions,
        inheritance,
        simpleEnums,
        threads,
        coRoutines
    ], has_execution_type = [lineByLineExecution]
    , has_memory_management = [manualMemoryManagement]
    , runs_on = [NativeEnvironment]
    , has_type_checking = [staticTypeChecking]
    , has_type_safety = [weakTypeSafety]
    , has_error_handling_type = [
        nullPointers,
        exceptions
    ], used_for = [
        gameDevelopment,
        desktopApplications,
        enterpriseApplications,
        osDevelopment,
        embeddedDevelopment,
        compilerDevelopment,
        databaseManagement
    ], inter_op_with = [c]
    , inspired_by = [c]
    )

    c_sharp = ProgrammingLanguage("c#", has_feature = [
        blocks,
        loops,
        classes,
        functionsAsFirstClassCitizens,
        higherOrderFunctions,
        inheritance,
        simpleEnums,
        threads,
        asyncFunctions,
        coRoutines
    ], has_execution_type = [lineByLineExecution]
    , has_memory_management = [TracingGC]
    , runs_on = [ByteCodeInterpreter]
    , has_type_checking = [staticTypeChecking]
    , has_type_safety = [strongTypeSafety]
    , has_error_handling_type = [
        nullPointers,
        exceptions
    ], used_for = [
        gameDevelopment,
        desktopApplications,
        enterpriseApplications,
        webApplications
    ], inspired_by = [c_pp]
    )

    java = ProgrammingLanguage("java", has_feature = [
        blocks,
        loops,
        classes,
        functionsAsFirstClassCitizens,
        higherOrderFunctions,
        inheritance,
        simpleEnums,
        threads
    ], has_execution_type = [lineByLineExecution]
    , has_memory_management = [TracingGC]
    , runs_on = [jvm]
    , has_type_checking = [staticTypeChecking]
    , has_type_safety = [strongTypeSafety]
    , has_error_handling_type = [
        nullPointers,
        exceptions
    ], used_for = [
        webApplications,
        cloudApplications,
        desktopApplications,
        enterpriseApplications,
        mobileApplications
    ], inspired_by = [c_pp]
    )

    kotlin = ProgrammingLanguage("kotlin", has_feature = [
        blocks,
        loops,
        classes,
        functionsAsFirstClassCitizens,
        higherOrderFunctions,
        inheritance,
        simpleEnums,
        threads,
        caseClasses
    ], has_execution_type = [lineByLineExecution]
    , has_memory_management = [TracingGC]
    , runs_on = [jvm]
    , has_type_checking = [staticTypeChecking]
    , has_type_safety = [strongTypeSafety]
    , has_error_handling_type = [
        exceptions,
        errorsAsSumTypes
    ], used_for = [
        webApplications,
        desktopApplications,
        enterpriseApplications,
        mobileApplications
    ], inspired_by = [c_pp]
    )

    python = ProgrammingLanguage("python", has_feature = [
        blocks,
        loops,
        classes,
        functionsAsFirstClassCitizens,
        higherOrderFunctions,
        inheritance,
        threads,
        asyncFunctions,
        tuples
    ], has_execution_type = [lineByLineExecution]
    , has_memory_management = [referenceCounting]
    , runs_on = [LineByLineInterpreter]
    , has_type_checking = [dynamicTypeChecking]
    , has_type_safety = [strongTypeSafety]
    , has_error_handling_type = [exceptions]
    , used_for = [
        webApplications,
        aiDevelopment,
        scientificComputing,
        desktopApplications,
        enterpriseApplications,
        osDevelopment
    ])

    bash = ProgrammingLanguage("bash", has_feature = [
        blocks,
        loops
    ], has_execution_type = [lineByLineExecution]
    , has_memory_management = [manualMemoryManagement]
    , runs_on = [LineByLineInterpreter]
    , has_type_safety = [weakTypeSafety]
    , has_error_handling_type = [errorsAsValues]
    , used_for = [osDevelopment]
    )

    powershell = ProgrammingLanguage("powershell",has_feature = [
        blocks,
        loops,
        classes,
        inheritance
    ], has_execution_type = [lineByLineExecution]
    , has_memory_management = [TracingGC]
    , runs_on = [LineByLineInterpreter]
    , has_type_checking = [dynamicTypeChecking]
    , has_type_safety = [weakTypeSafety]
    , has_error_handling_type = [exceptions]
    , used_for = [osDevelopment]
    , inspired_by = [bash]
    )

    haskell = ProgrammingLanguage("haskell",has_feature = [
        tuples,
        richEnums,
        functionsAsFirstClassCitizens,
        higherOrderFunctions,
        lazyEvaluation,
        strictImmutability,
        monadConcurrency
    ], has_execution_type = [evaluationOfExpression]
    , has_memory_management = [TracingGC]
    , runs_on = [Interpreter]
    , has_type_checking = [staticTypeChecking]
    , has_type_safety = [strongTypeSafety]
    , has_error_handling_type = [errorsAsSumTypes]
    , used_for = [
        scientificComputing,
        highlyConcurrentApplications,
        compilerDevelopment,
        financialSoftware
    ])

    rust = ProgrammingLanguage("rust",has_feature = [
        blocks,
        loops,
        structures,
        functionsAsFirstClassCitizens,
        higherOrderFunctions,
        richEnums,
        threads,
        asyncFunctions,
        tuples,
        defaultImmutability
    ], has_execution_type = [lineByLineExecution]
    , has_memory_management = [borrowChecker]
    , runs_on = [NativeEnvironment]
    , has_type_checking = [staticTypeChecking]
    , has_type_safety = [strongTypeSafety]
    , has_error_handling_type = [errorsAsSumTypes]
    , used_for = [
        embeddedDevelopment,
        aiDevelopment,
        gameDevelopment,
        webApplications,
        osDevelopment,
        compilerDevelopment,
        databaseManagement
    ], inspired_by = [
        c_pp,
        haskell
    ])

    go = ProgrammingLanguage("go",has_feature = [
        blocks,
        loops,
        structures,
        functionsAsFirstClassCitizens,
        higherOrderFunctions,
        coRoutines
    ], has_execution_type = [lineByLineExecution]
    , has_memory_management = [TracingGC]
    , runs_on = [NativeEnvironment]
    , has_type_checking = [staticTypeChecking]
    , has_type_safety = [strongTypeSafety]
    , has_error_handling_type = [errorsAsValues]
    , used_for = [
        cloudApplications,
        enterpriseApplications,
        webApplications
    ], inspired_by = [
        c,
        java
    ]
    )

    ruby = ProgrammingLanguage("ruby",has_feature = [
        blocks,
        loops,
        classes,
        functionsAsFirstClassCitizens,
        higherOrderFunctions,
        inheritance,
        simpleEnums,
        threads
    ], has_execution_type = [lineByLineExecution]
    , has_memory_management = [TracingGC]
    , runs_on = [ByteCodeInterpreter]
    , has_type_checking = [dynamicTypeChecking]
    , has_type_safety = [strongTypeSafety]
    , has_error_handling_type = [
        nullPointers,
        exceptions
    ], used_for = [webApplications]
    )

    php = ProgrammingLanguage("php",has_feature = [
        blocks,
        loops,
        classes,
        functionsAsFirstClassCitizens,
        higherOrderFunctions,
        inheritance,
        simpleEnums,
        threads
    ], has_execution_type = [lineByLineExecution]
    , has_memory_management = [TracingGC]
    , runs_on = [Interpreter]
    , has_type_checking = [dynamicTypeChecking]
    , has_type_safety = [weakTypeSafety]
    , has_error_handling_type = [
        nullPointers,
        exceptions
    ], used_for = [webApplications]
    )

    scheme = ProgrammingLanguage("scheme",has_feature = [
        functionsAsFirstClassCitizens,
        higherOrderFunctions,
        strictImmutability
    ], has_execution_type = [evaluationOfExpression]
    , has_memory_management = [referenceCounting]
    , runs_on = [Interpreter]
    , has_type_checking = [dynamicTypeChecking]
    , has_type_safety = [strongTypeSafety]
    , has_error_handling_type = [
        research,
        aiDevelopment
    ])

    closure = ProgrammingLanguage("closure",has_feature = [
        functionsAsFirstClassCitizens,
        higherOrderFunctions,
        strictImmutability
    ], has_execution_type = [evaluationOfExpression]
    , has_memory_management = [g1]
    , runs_on = [jvm]
    , has_type_checking = [dynamicTypeChecking]
    , has_type_safety = [strongTypeSafety]
    , has_error_handling_type = [errorsAsValues]
    , used_for = [highlyConcurrentApplications]
    , inspired_by = [scheme]
    )

    scala = ProgrammingLanguage("scala",has_feature = [
        blocks,
        loops,
        classes,
        functionsAsFirstClassCitizens,
        higherOrderFunctions,
        richEnums,
        caseClasses,
        monadConcurrency,
        asyncFunctions,
        tuples,
        defaultImmutability
    ], has_execution_type = [
        evaluationOfExpression,
        lineByLineExecution
    ], has_memory_management = [TracingGC]
    , runs_on = [jvm]
    , has_type_checking = [staticTypeChecking]
    , has_type_safety = [strongTypeSafety]
    , has_error_handling_type = [errorsAsSumTypes]
    , used_for = [
        cloudApplications,
        highlyConcurrentApplications
    ], inspired_by = [
        java,
        haskell
    ])

    javascript = ProgrammingLanguage("javascript",has_feature = [
        blocks,
        loops,
        classes,
        functionsAsFirstClassCitizens,
        higherOrderFunctions,
        asyncFunctions,
    ], has_execution_type = [lineByLineExecution]
    , has_memory_management = [TracingGC]
    , runs_on = [Interpreter]
    , has_type_checking = [dynamicTypeChecking]
    , has_type_safety = [weakTypeSafety]
    , has_error_handling_type = [exceptions]
    , used_for = [webApplications]
    , inspired_by = [java]
    )

    typescript = ProgrammingLanguage("typescript",has_feature = [
        blocks,
        loops,
        classes,
        functionsAsFirstClassCitizens,
        higherOrderFunctions,
        asyncFunctions,
        tuples,
        unionTypes
    ], has_execution_type = [lineByLineExecution]
    , has_memory_management = [TracingGC]
    , runs_on = [Interpreter]
    , has_type_checking = [staticTypeChecking]
    , has_type_safety = [strongTypeSafety]
    , has_error_handling_type = [exceptions]
    , used_for = [webApplications]
    , inspired_by = [javascript]
    )

    elm = ProgrammingLanguage("elm",has_feature = [
        tuples,
        richEnums,
        functionsAsFirstClassCitizens,
        higherOrderFunctions,
        lazyEvaluation,
        strictImmutability
    ], has_execution_type = [evaluationOfExpression]
    , has_memory_management = [TracingGC]
    , runs_on = [Interpreter]
    , has_type_checking = [staticTypeChecking]
    , has_type_safety = [strongTypeSafety]
    ,has_similar_syntax_to = [haskell]
    , has_error_handling_type = [errorsAsSumTypes]
    , used_for = [webApplications]
    , inspired_by = [
        haskell,
        javascript
    ])

    prolog = ProgrammingLanguage("prolog",has_feature = [
        rules,
        facts,
        strictImmutability
    ], has_execution_type = [reasoner]
    , has_memory_management = [referenceCounting]
    , runs_on = [Interpreter]
    , has_type_checking = [dynamicTypeChecking]
    , used_for = [
        research,
        aiDevelopment,
        compilerDevelopment
    ])

    sql = ProgrammingLanguage("sql",has_feature = [
        queries,
        strictImmutability
    ], has_execution_type = [reasoner]
    , runs_on = [Interpreter]
    , used_for = [databases]
    )

    matlab = ProgrammingLanguage("matlab",has_feature = [
        loops,
        procedures,
        pureFunctions,
        classes,
        inheritance,
        threads
    ], has_execution_type = [lineByLineExecution]
    , runs_on = [Interpreter]
    , has_type_safety = [strongTypeSafety]
    , has_type_checking = [dynamicTypeChecking]
    , used_for = [
        research,
        scientificComputing
    ])

    wolframLanguage = ProgrammingLanguage("wolfram",has_feature = [
        loops,
        procedures,
        pureFunctions,
        threads
    ], has_execution_type = [lineByLineExecution]
    , runs_on = [Interpreter]
    , has_type_safety = [strongTypeSafety]
    , has_type_checking = [dynamicTypeChecking]
    , used_for = [
        research,
        scientificComputing
    ])

    r = ProgrammingLanguage("r",has_feature = [
        blocks,
        loops,
        procedures,
        classes,
        inheritance
    ], has_execution_type = [lineByLineExecution]
    , runs_on = [Interpreter]
    , has_type_safety = [strongTypeSafety]
    , has_type_checking = [dynamicTypeChecking]
    , used_for = [
        research,
        scientificComputing
    ])

AllDifferent([lazyEvaluation, inheritance, rules, facts, queries, functionDefinition, functionsAsFirstClassCitizens, higherOrderFunctions, pureFunctions, blocks, procedures, loops, defaultImmutability, strictImmutability, threads, coRoutines, processes, asyncFunctions, monadConcurrency, structures, tuples, classes, simpleEnums, richEnums, caseClasses, unionTypes, lineByLineExecution, evaluationOfExpression, reasoner, manualMemoryManagement, referenceCounting, g1, borrowChecker, staticTypeChecking, dynamicTypeChecking, strongTypeSafety, weakTypeSafety, nullPointers, exceptions, errorsAsSumTypes, errorsAsValues, webApplications, mobileApplications, desktopApplications, enterpriseApplications, cloudApplications, scientificComputing, aiDevelopment, osDevelopment, gameDevelopment, databaseManagement, compilerDevelopment, embeddedDevelopment, financialSoftware, research, databases, highlyConcurrentApplications, bash_interpreter, python_interpreter, jvm, x86, x64, arm, mips, c, c_pp, c_sharp, java, kotlin, python, bash, powershell, rust, go, ruby, php, haskell, scheme, closure, scala, javascript, elm, prolog, matlab, wolframLanguage, r, sql])

# close_world(ProgrammingLanguage)
onto.save(file = "programming_languages.owl", format = "rdfxml")
