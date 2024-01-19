from owlready2 import *

onto = get_ontology("http://example.org/programming_languages.owl")

with onto:
    ### Features
    class Feature(Thing): pass
    instructions = Feature("instructions")
    inheritance = Feature("inheritance")
    class Abstraction(Feature): pass

    # statements
    class Statements(Abstraction): pass
    rules = Statements("rules")
    facts = Statements("facts")
    queries = Statements("queries")
    functionDefinition = Statements("function_definitions")

    # different functions
    functionsAsFirstOrderCitizens = Abstraction("functions_as_first_order_citizens")
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
    simpleEnums = Feature("simple_enums")

    class SumTypes(CustomTypes): pass
    richEnums = SumTypes("rich_enums")
    caseClasses = SumTypes("case_classes")
    unionTypes = SumTypes("union_types")

    # memory management
    class MemoryManagement(Thing): pass
    class AutomaticMemoryManagement(MemoryManagement, Abstraction): pass
    class TracingGC(AutomaticMemoryManagement): pass
    class SemiAutomaticMemoryManagement(MemoryManagement): pass
    manualMemoryManagement = MemoryManagement("manual_memory_management")
    referenceCounting = AutomaticMemoryManagement("reference_counting")
    g1 = TracingGC("garbage_first_GC")
    borrowChecker = SemiAutomaticMemoryManagement("borrow_checker")

    # evaluation
    class EvaluationStrategy(Thing): pass
    strictEvaluation = EvaluationStrategy("strict_evaluation")
    lazyEvaluation = EvaluationStrategy("lazy_evaluation")

    # type system
    class TypeChecking(Thing): pass
    staticTypeChecking = TypeChecking("static_type_checking")
    dynamicTypeChecking = TypeChecking("dynamic_type_checking")

    class TypeSafety(Thing): pass
    strongTypeSafety = TypeSafety("strong_type_safety")
    weakTypeSafety = TypeSafety("weak_type_safety")

    # error handling
    class ErrorHandling(Thing): pass
    nullPointers = ErrorHandling("null_pointers")
    exceptions = ErrorHandling("exceptions")
    class ErrorInReturnType(ErrorHandling): pass
    errorsAsSumTypes = ErrorInReturnType("errors_as_sum _types")
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
    jvm = ByteCodeInterpreter("jvm")
    x86 = NativeEnvironment("x86")
    x64 = NativeEnvironment("x64")
    arm = NativeEnvironment("arm")
    mips = NativeEnvironment("mips")

    ### Programming language
    class ProgrammingLanguage(Thing): pass

    ### Properties

    # class UsedBy(ObjectProperty):
    #     domain = [ProgrammingLanguage]
    #     range = [User]

    class used_for(ObjectProperty):
        domain = [ProgrammingLanguage]
        range = [UseCase]

    class has_similar_syntax_to(ProgrammingLanguage >> ProgrammingLanguage):
        reflexive = True
        symmetric = True

    class inspired_by(ProgrammingLanguage >> ProgrammingLanguage): pass

    class inspired(ProgrammingLanguage >> ProgrammingLanguage):
        inverse_property = inspired_by

    class from_the_same_creators(ProgrammingLanguage >> ProgrammingLanguage):
        reflexive = True
        symmetric = True
        transitive = True

    class inter_op_with(ProgrammingLanguage >> ProgrammingLanguage): pass

    class runs_on(ProgrammingLanguage >> RunningEnvironment): pass

    class has_feature(ProgrammingLanguage >> Feature): pass

    # class defaultEvaluationType(ProgrammingLanguage):

    class has_error_handling_type(ProgrammingLanguage >> ErrorHandling):
        functional = True

    class has_evaluation_type(ProgrammingLanguage >> EvaluationStrategy):
        functional = True

    class has_type_checking(ProgrammingLanguage >> TypeChecking):
        functional = True

    class has_type_safety(ProgrammingLanguage >> TypeSafety):
        functional = True

    class has_memory_management(ProgrammingLanguage >> MemoryManagement):
        functional = True

    ### Classes
    class HighLevelLanguage(ProgrammingLanguage):
        has_feature.min(1, Abstraction)

    class LowLevelLanguage(ProgrammingLanguage):
        has_feature.max(1, Abstraction)

    class ConcurrentLanguage(ProgrammingLanguage):
        has_feature.only(Concurrency)

    class ImperativeLanguage(ProgrammingLanguage):
        has_feature.only(instructions)

    class StructuredLanguage(ImperativeLanguage):
        has_feature.only(CodeStructures)

    class AssemblyLanguage(ImperativeLanguage, LowLevelLanguage):
        runs_on.only(NativeEnvironment)

    class ProceduralLanguage(StructuredLanguage):
        has_feature.only(procedures)

    class DeclarativeLanguage(HighLevelLanguage):
        has_feature.only(Statements)

    class FunctionalInspiredLanguage(HighLevelLanguage):
        has_feature.only(functionsAsFirstOrderCitizens)
        has_feature.only(higherOrderFunctions)

    # inference that FunctionalLanguage is Declarative
    class FunctionalLanguage(FunctionalInspiredLanguage):
        has_feature.only(Statements)
        has_feature.only(defaultImmutability)

    class PureFunctionalLanguage(FunctionalLanguage):
        has_feature.only(pureFunctions)
        has_feature.only(strictImmutability)

    class LazyEvaluatedLanguage(PureFunctionalLanguage):
        has_feature.only(lazyEvaluation)

    # inference that LogicLanguage is Declarative
    class LogicLanguage(ProgrammingLanguage):
        has_feature.only(facts)
        has_feature.only(rules)

    # inference that QueryLanguage is Declarative
    class QueryLanguage(ProgrammingLanguage):
        has_feature.only(Statements)

    class HasAlgebraicTypes(ProgrammingLanguage):
        has_feature.only(ProductTypes)
        has_feature.only(SumTypes)

    class OOPinspiredLanguage(ProgrammingLanguage):
        has_feature.only(Structures)

    class OOPLanguage(OOPinspiredLanguage):
        equivalent_to = [has_feature.only(classes) & has_feature.only(inheritance)]
        # has_feature.only(classes)
        # has_feature.only(inheritance)

    class MultiParadigmLanguage(OOPinspiredLanguage, FunctionalInspiredLanguage): pass

    class StaticallyTypedLanguage(ProgrammingLanguage):
        has_type_checking.only(staticTypeChecking)

    class DynamicallyTypedLanguage(ProgrammingLanguage):
        has_type_checking.only(dynamicTypeChecking)

    class StronglyTypedLanguage(ProgrammingLanguage):
        has_type_safety.only(strongTypeSafety)

    class WeaklyTypedLanguage(ProgrammingLanguage):
        has_type_safety.only(weakTypeSafety)

    class SafeTypeCheckingLanguage(StaticallyTypedLanguage, StronglyTypedLanguage): pass

    class ErrorSafeLanguage(ProgrammingLanguage):
        has_error_handling_type.only(ErrorInReturnType)

    class SafeLanguage(ErrorSafeLanguage, SafeTypeCheckingLanguage): pass

    class ModernFunctionalLanguage(PureFunctionalLanguage, SafeTypeCheckingLanguage): pass

    class CompiledLanguage(ProgrammingLanguage): pass

    class LanguageWithRuntime(HighLevelLanguage): pass

    class CompiledToByteCodeLanguage(CompiledLanguage):
        runs_on.only(ByteCodeInterpreter)

    class CompiledToMachineCodeLanguage(CompiledLanguage):
        runs_on.only(NativeEnvironment)

    class FastLanguage(CompiledToMachineCodeLanguage):
        Not(LanguageWithRuntime)

    class InterpretedLanguage(LanguageWithRuntime):
        runs_on.only(Interpreter)

    # inference that Scripting < Interpreted
    class ScriptingLanguage(ProgrammingLanguage):
        runs_on.only(LineByLineInterpreter)

    class ShellLanguage(ScriptingLanguage):
        used_for.only(os)

    # inference that JVMLanguage < Interpreted
    class JVMLanguage(ProgrammingLanguage):
        runs_on.only(LineByLineInterpreter)

    class GarbageCollectedLanguage(LanguageWithRuntime):
        has_memory_management.only(AutomaticMemoryManagement)

    # inference that ReferenceCounted < GarbageCollected
    class ReferenceCountedLanguage(ProgrammingLanguage):
        has_memory_management.only(referenceCounting)

    class MultifunctionalLanguage(ProgrammingLanguage):
        used_for.min(2, UseCase)

    class PopularLanguage(ProgrammingLanguage):
        used_for.min(3, UseCase)

    class InfluencedLanguage(ProgrammingLanguage):
        inspired_by.min(2, ProgrammingLanguage)

    class InfluentialLanguage(ProgrammingLanguage):
        inspired.min(2, ProgrammingLanguage)

    class FatherLanguage(Thing):
        inspired.min(3, ProgrammingLanguage)

    # Individuals
    c = FastLanguage("c", has_feature = [
        blocks,
        procedures,
        loops,
        structures,
        processes
    ], has_memory_management = [
        manualMemoryManagement
    ], runs_on = [
        NativeEnvironment
    ], TypeCheckingType = [
        staticTypeChecking
    ], TypeSafety = [
        weakTypeSafety
    ], has_error_handling_type = [
        nullPointers
    ], used_for = [
        gameDevelopment,
        desktopApplications,
        osDevelopment,
        embeddedDevelopment,
        compilerDevelopment,
        databaseManagement
    ])

    class CurlyBracketLanguages(ProgrammingLanguage):
        has_similar_syntax_to.only(c)

    c_pp = FastLanguage("c++", has_feature = [
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
    ], has_memory_management = [
        manualMemoryManagement
    ], runs_on = [
        NativeEnvironment
    ], TypeCheckingType = [
        staticTypeChecking
    ], TypeSafety = [
        weakTypeSafety
    ], has_error_handling_type = [
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
    ], inter_op_with = [
        c
    ], inspired_by = [
        c
    ])

    c_sharp = ProgrammingLanguage("c#", has_feature = [
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
    ], has_memory_management = [
        TracingGC
    ], runs_on = [
        ByteCodeInterpreter
    ], TypeCheckingType = [
        staticTypeChecking
    ], TypeSafety = [
        strongTypeSafety
    ], has_error_handling_type = [
        nullPointers,
        exceptions
    ], used_for = [
        gameDevelopment,
        desktopApplications,
        enterpriseApplications,
        webApplications
    ], inspired_by = [
        c_pp
    ])

    java = ProgrammingLanguage("java", has_feature = [
        blocks,
        loops,
        classes,
        functionsAsFirstOrderCitizens,
        higherOrderFunctions,
        inheritance,
        simpleEnums,
        threads
    ], has_memory_management = [
        TracingGC
    ], runs_on = [
        jvm
    ], TypeCheckingType = [
        staticTypeChecking
    ], TypeSafety = [
        strongTypeSafety
    ], has_error_handling_type = [
        nullPointers,
        exceptions
    ], used_for = [
        webApplications,
        cloudApplications,
        desktopApplications,
        enterpriseApplications,
        mobileApplications
    ], inspired_by = [
        c_pp
    ])

    kotlin = ProgrammingLanguage("kotlin", has_feature = [
        blocks,
        loops,
        classes,
        functionsAsFirstOrderCitizens,
        higherOrderFunctions,
        inheritance,
        simpleEnums,
        threads,
        caseClasses
    ], has_memory_management = [
        TracingGC
    ], runs_on = [
        jvm
    ], TypeCheckingType = [
        staticTypeChecking
    ], TypeSafety = [
        strongTypeSafety
    ], has_error_handling_type = [
        exceptions,
        errorsAsSumTypes
    ], used_for = [
        webApplications,
        desktopApplications,
        enterpriseApplications,
        mobileApplications
    ], inspired_by = [
        c_pp
    ])

    python = ProgrammingLanguage("python", has_feature = [
        blocks,
        loops,
        classes,
        functionsAsFirstOrderCitizens,
        higherOrderFunctions,
        inheritance,
        threads,
        asyncFunctions,
        tuples
    ], has_memory_management = [
        referenceCounting
    ], runs_on = [
        LineByLineInterpreter
    ], TypeCheckingType = [
        dynamicTypeChecking
    ], TypeSafety = [
        strongTypeSafety
    ], has_error_handling_type = [
        exceptions
    ], used_for = [
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
    ], has_memory_management = [
        manualMemoryManagement
    ], runs_on = [
        LineByLineInterpreter
    ], TypeSafety = [
        weakTypeSafety
    ], has_error_handling_type = [
        errorsAsValues
    ], used_for = [
        osDevelopment
    ])

    powershell = ProgrammingLanguage("powershell",has_feature = [
        blocks,
        loops,
        classes,
        inheritance
    ], has_memory_management = [
        TracingGC
    ], runs_on = [
        LineByLineInterpreter
    ], TypeCheckingType = [
        dynamicTypeChecking
    ], TypeSafety = [
        weakTypeSafety
    ], has_error_handling_type = [
        exceptions
    ], used_for = [
        osDevelopment
    ], inspired_by = [
        bash
    ])

    haskell = ProgrammingLanguage("haskell",has_feature = [
        tuples,
        richEnums,
        functionsAsFirstOrderCitizens,
        higherOrderFunctions,
        lazyEvaluation,
        strictImmutability,
        monadConcurrency
    ], has_memory_management = [
        TracingGC
    ], runs_on = [
        Interpreter
    ], TypeCheckingType = [
        staticTypeChecking
    ], TypeSafety = [
        strongTypeSafety
    ], has_error_handling_type = [
        errorsAsSumTypes
    ], used_for = [
        scientificComputing,
        highlyConcurrentApplications,
        compilerDevelopment,
        financialSoftware
    ])

    rust = ProgrammingLanguage("rust",has_feature = [
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
    ], has_memory_management = [
        borrowChecker
    ], runs_on = [
        NativeEnvironment
    ], TypeCheckingType = [
        staticTypeChecking
    ], TypeSafety = [
        strongTypeSafety
    ], has_error_handling_type = [
        errorsAsSumTypes
    ], used_for = [
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
        functionsAsFirstOrderCitizens,
        higherOrderFunctions,
        coRoutines
    ], has_memory_management = [
        TracingGC
    ], runs_on = [
        NativeEnvironment
    ], TypeCheckingType = [
        staticTypeChecking
    ], TypeSafety = [
        strongTypeSafety
    ], has_error_handling_type = [
        errorsAsValues
    ], used_for = [
        cloudApplications,
        enterpriseApplications,
        webApplications
    ], inspired_by = [
        c
    ])

    ruby = ProgrammingLanguage("ruby",has_feature = [
        blocks,
        loops,
        classes,
        functionsAsFirstOrderCitizens,
        higherOrderFunctions,
        inheritance,
        simpleEnums,
        threads
    ], has_memory_management = [
        TracingGC
    ], runs_on = [
        ByteCodeInterpreter
    ], TypeCheckingType = [
        dynamicTypeChecking
    ], TypeSafety = [
        strongTypeSafety
    ], has_error_handling_type = [
        nullPointers,
        exceptions
    ], used_for = [
        webApplications
    ])

    php = ProgrammingLanguage("php",has_feature = [
        blocks,
        loops,
        classes,
        functionsAsFirstOrderCitizens,
        higherOrderFunctions,
        inheritance,
        simpleEnums,
        threads
    ], has_memory_management = [
        TracingGC
    ], runs_on = [
        jvm
    ], TypeCheckingType = [
        dynamicTypeChecking
    ], TypeSafety = [
        weakTypeSafety
    ], has_error_handling_type = [
        nullPointers,
        exceptions
    ], used_for = [
        webApplications
    ])

    scheme = ProgrammingLanguage("scheme",has_feature = [
        functionsAsFirstOrderCitizens,
        higherOrderFunctions,
        strictImmutability
    ], has_memory_management = [
        referenceCounting
    ], runs_on = [
        Interpreter
    ], TypeCheckingType = [
        dynamicTypeChecking
    ], TypeSafety = [
        strongTypeSafety
    ], has_error_handling_type = [
        research,
        aiDevelopment
    ])

    closure = ProgrammingLanguage("closure",has_feature = [
        functionsAsFirstOrderCitizens,
        higherOrderFunctions,
        strictImmutability
    ], has_memory_management = [
        referenceCounting
    ], runs_on = [
        jvm
    ], TypeCheckingType = [
        dynamicTypeChecking
    ], TypeSafety = [
        strongTypeSafety
    ], has_error_handling_type = [
        errorsAsValues
    ], used_for = [
        highlyConcurrentApplications
    ], inspired_by = [
        scheme
    ])

    scala = ProgrammingLanguage("scala",has_feature = [
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
    ], has_memory_management = [
        TracingGC
    ], runs_on = [
        jvm
    ], TypeCheckingType = [
        staticTypeChecking
    ], TypeSafety = [
        strongTypeSafety
    ], has_error_handling_type = [
        errorsAsSumTypes
    ], used_for = [
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
        functionsAsFirstOrderCitizens,
        higherOrderFunctions,
        asyncFunctions,
    ], has_memory_management = [
        TracingGC
    ], runs_on = [
        Interpreter
    ], TypeCheckingType = [
        dynamicTypeChecking
    ], TypeSafety = [
        weakTypeSafety
    ], has_error_handling_type = [
        exceptions
    ], used_for = [
        webApplications
    ], inspired_by = [
        java
    ])

    typescript = ProgrammingLanguage("typescript",has_feature = [
        blocks,
        loops,
        classes,
        functionsAsFirstOrderCitizens,
        higherOrderFunctions,
        asyncFunctions,
        tuples,
        unionTypes
    ], has_memory_management = [
        TracingGC
    ], runs_on = [
        Interpreter
    ], TypeCheckingType = [
        staticTypeChecking
    ], TypeSafety = [
        strongTypeSafety
    ], has_error_handling_type = [
        exceptions
    ], used_for = [
        webApplications
    ], inspired_by = [
        javascript
    ])

    elm = ProgrammingLanguage("elm",has_feature = [
        tuples,
        richEnums,
        functionsAsFirstOrderCitizens,
        higherOrderFunctions,
        lazyEvaluation,
        strictImmutability,
        monadConcurrency
    ], has_memory_management = [
        TracingGC
    ], runs_on = [
        Interpreter
    ], TypeCheckingType = [
        staticTypeChecking
    ], TypeSafety = [
        strongTypeSafety
    ], has_error_handling_type = [
        errorsAsSumTypes
    ], used_for = [
        webApplications
    ], inspired_by = [
        haskell,
        javascript
    ])

    prolog = ProgrammingLanguage("prolog",has_feature = [
        rules,
        facts,
        strictImmutability
    ], has_memory_management = [
        referenceCounting
    ], runs_on = [
        Interpreter
    ], has_type_checking = [
        dynamicTypeChecking
    ], used_for = [
        research,
        aiDevelopment,
        compilerDevelopment
    ])

    sql = ProgrammingLanguage("sql",has_feature = [
        queries,
        strictImmutability
    ], runs_on = [
        Interpreter
    ], used_for = [
        databases
    ])

    matlab = ProgrammingLanguage("matlab",has_feature = [
        loops,
        procedures,
        pureFunctions,
        classes,
        inheritance,
        threads
    ], runs_on = [
        Interpreter
    ], has_type_safety = [
        strongTypeSafety
    ], has_type_checking = [
        dynamicTypeChecking
    ], used_for = [
        research,
        scientificComputing
    ])

    wolframLanguage = ProgrammingLanguage("wolfram",has_feature = [
        loops,
        procedures,
        pureFunctions,
        threads
    ], runs_on = [
        Interpreter
    ], has_type_safety = [
        strongTypeSafety
    ], has_type_checking = [
        dynamicTypeChecking
    ], used_for = [
        research,
        scientificComputing
    ])

    r = ProgrammingLanguage("r",has_feature = [
        blocks,
        loops,
        procedures,
        classes,
        inheritance
    ], runs_on = [
        Interpreter
    ], has_type_safety = [
        strongTypeSafety
    ], has_type_checking = [
        dynamicTypeChecking
    ], used_for = [
        research,
        scientificComputing
    ])

AllDifferent([instructions, inheritance, rules, facts, queries, functionDefinition, functionsAsFirstOrderCitizens, higherOrderFunctions, pureFunctions, blocks, procedures, loops, defaultImmutability, strictImmutability, threads, coRoutines, processes, asyncFunctions, monadConcurrency, structures, tuples, classes, simpleEnums, richEnums, caseClasses, unionTypes, manualMemoryManagement, referenceCounting, g1, borrowChecker, strictEvaluation, lazyEvaluation, staticTypeChecking, dynamicTypeChecking, strongTypeSafety, weakTypeSafety, nullPointers, exceptions, errorsAsSumTypes, errorsAsValues, webApplications, mobileApplications, desktopApplications, enterpriseApplications, cloudApplications, scientificComputing, aiDevelopment, osDevelopment, gameDevelopment, databaseManagement, compilerDevelopment, embeddedDevelopment, financialSoftware, research, databases, highlyConcurrentApplications, bash_interpreter, jvm, x86, x64, arm, mips, c, c_pp, c_sharp, java, kotlin, python, bash, powershell, rust, go, ruby, php, haskell, scheme, closure, scala, javascript, elm, prolog, matlab, wolframLanguage, r, sql])

# close_world(ProgrammingLanguage)
onto.save(file = "programming_languages.owl", format = "rdfxml")
