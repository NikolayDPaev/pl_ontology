from owlready2 import *

onto = get_ontology("http://example.org/programming_languages.owl")

with onto:
    ### Features
    class Feature(Thing): pass
    class Abstraction(Feature): pass

    lazy_evaluation = Feature("lazy_evaluation")
    inheritance = Abstraction("inheritance")

    # statements
    class Statements(Abstraction): pass
    rules = Statements("rules")
    facts = Statements("facts")
    queries = Statements("queries")

    # different functions
    functions_as_first_class_citizens = Abstraction("functions_as_first_class_citizens")
    higher_order_functions = Abstraction("higher_order_functions")
    pure_functions = Abstraction("pure_functions")

    # structures in the code
    class CodeStructures(Abstraction): pass
    blocks = CodeStructures("blocks")
    procedures = CodeStructures("procedures")
    loops = CodeStructures("loops")

    # immutability
    class Immutability(Feature): pass
    default_immutability = Immutability("default_immutability")
    strict_immutability = Immutability("strict_immutability")

    # concurrency
    class Concurrency(Feature): pass
    threads = Concurrency("threads")
    co_routines = Concurrency("co_routines")
    processes = Concurrency("processes")
    async_functions = Concurrency("async_functions")
    monad_concurrency = Concurrency("monad_concurrency")

    # types
    class CustomTypes(Feature): pass
    class ProductTypes(CustomTypes): pass
    class Structures(ProductTypes): pass
    structures = Structures("structs")
    tuples = ProductTypes("tuples")
    classes = Structures("classes")
    simple_enums = CustomTypes("simple_enums")

    class SumTypes(CustomTypes): pass
    rich_enums = SumTypes("rich_enums")
    case_classes = SumTypes("case_classes")
    union_types = SumTypes("union_types")

    # execution type
    class ExecutionType(Thing): pass
    line_by_line_execution = ExecutionType("line_by_line_execution")
    evaluation_of_expression = ExecutionType("evaluation_of_expression")
    evaluation_of_query = ExecutionType("evaluation_of_query")

    # memory management
    class MemoryManagement(Thing): pass
    class AutomaticMemoryManagement(MemoryManagement, Abstraction): pass
    class TracingGC(AutomaticMemoryManagement): pass
    class SemiAutomaticMemoryManagement(MemoryManagement): pass
    manual_memory_management = MemoryManagement("manual_memory_management")
    reference_counting = AutomaticMemoryManagement("reference_counting")
    generational_GC = TracingGC("generational_GC")
    borrow_checker = SemiAutomaticMemoryManagement("borrow_checker")

    # type system
    class TypeChecking(Thing): pass
    static_type_checking = TypeChecking("static_type_checking")
    dynamic_type_checking = TypeChecking("dynamic_type_checking")

    class TypeSafety(Thing): pass
    strong_type_safety = TypeSafety("strong_type_safety")
    weak_type_safety = TypeSafety("weak_type_safety")

    # error handling
    class ErrorHandling(Thing): pass
    null_pointers = ErrorHandling("null_pointers")
    exceptions = ErrorHandling("exceptions")
    class ErrorInReturnType(ErrorHandling): pass
    errors_as_sum_types = ErrorInReturnType("errors_as_sum_types")
    errors_as_values = ErrorInReturnType("errors_as_values")

    # use cases
    class UseCase(Thing): pass
    web_applications = UseCase("web_applications")
    mobile_applications = UseCase("mobile_applications")
    desktop_applications = UseCase("desktop_applications")
    enterprise_applications = UseCase("enterprise_level_applications")
    cloud_applications = UseCase("cloud_applications")
    scientific_computing = UseCase("scientific_computing")
    ai_development = UseCase("AI_and_ML_field")
    os_development = UseCase("OS_development")
    os_communication = UseCase("OS_communication")
    game_development = UseCase("game_development")
    database_management = UseCase("database_management_systems_development")
    compiler_development = UseCase("compilers_and_interpreters_development")
    embedded_development = UseCase("embedded_development")
    financial_software = UseCase("financial_and_banking_software")
    research = UseCase("research")
    databases = UseCase("databases")
    highly_concurrent_applications = UseCase("highly_concurrent_applications")

    # running environment
    class RunningEnvironment(Thing): pass
    class Interpreter(RunningEnvironment): pass
    class LineByLineInterpreter(Interpreter): pass
    class ByteCodeInterpreter(Interpreter): pass
    bash_interpreter = LineByLineInterpreter("bash_interpreter")
    python_interpreter = LineByLineInterpreter("python_interpreter")
    native_environment = RunningEnvironment("native_environment")
    jvm = ByteCodeInterpreter("jvm")
    dot_net_vm = ByteCodeInterpreter(".net")
    ruby_vm = ByteCodeInterpreter("ruby_vm")
    php_interpreter = ByteCodeInterpreter("php_interpreter")
    v8_engine = Interpreter("v8")
    scheme_repl = LineByLineInterpreter("scheme_repl")
    prolog_interpreter = Interpreter("prolog_interpreter")
    sql_server = Interpreter("sql_server")
    matlab = Interpreter("matlab")
    wolfram = Interpreter("wolfram")
    r_studio = Interpreter("r_studio")

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
            has_feature.exactly(0, Abstraction)
        ]

    class ConcurrentLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_feature.some(Concurrency)
        ]

    class ImperativeLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_execution_type.value(line_by_line_execution)
        ]

    class StructuredLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_feature.some(CodeStructures)
        ]

    class AssemblyLanguage(ProgrammingLanguage):
        equivalent_to = [
            ImperativeLanguage &
            LowLevelLanguage &
            runs_on.value(native_environment)
        ]

    class ProceduralLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_feature.value(procedures)
        ]

    class DeclarativeLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_execution_type.value(evaluation_of_query) |
            has_execution_type.value(evaluation_of_expression)
        ]

    class FunctionalInspiredLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_feature.value(functions_as_first_class_citizens) &
            has_feature.value(higher_order_functions)
        ]

    # inference that FunctionalLanguage is Declarative
    class FunctionalLanguage(ProgrammingLanguage):
        equivalent_to = [
            FunctionalInspiredLanguage &
            has_execution_type.value(evaluation_of_expression) &
            has_feature.some(Immutability)
        ]

    class PureFunctionalLanguage(ProgrammingLanguage):
        equivalent_to = [
            FunctionalLanguage &
            has_feature.value(pure_functions) &
            has_feature.value(strict_immutability)
        ]

    class LazyEvaluatedLanguage(ProgrammingLanguage):
        equivalent_to = [
            PureFunctionalLanguage &
            has_feature.value(lazy_evaluation)
        ]

    class LogicLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_feature.value(facts) &
            has_feature.value(rules)
        ]

    class QueryLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_feature.value(queries)
        ]

    class OOPInspiredLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_feature.some(Structures)
        ]

    class OOPLanguage(ProgrammingLanguage):
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
            has_type_checking.value(static_type_checking)
        ]

    class DynamicallyTypedLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_type_checking.value(dynamic_type_checking)
        ]

    class StronglyTypedLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_type_safety.value(strong_type_safety)
        ]

    class WeaklyTypedLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_type_safety.value(weak_type_safety)
        ]

    class SafeTypeCheckingLanguage(ProgrammingLanguage):
        equivalent_to = [
            StaticallyTypedLanguage &
            StronglyTypedLanguage
        ]

    class ErrorSafeLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_error_handling_type.value(errors_as_sum_types)
        ]

    class SafeLanguage(ProgrammingLanguage):
        equivalent_to = [
            ErrorSafeLanguage &
            SafeTypeCheckingLanguage
        ]

    class HasAlgebraicTypes(ProgrammingLanguage):
        equivalent_to = [
            has_feature.some(ProductTypes) &
            has_feature.some(SumTypes)
        ]

    class ModernFunctionalLanguage(ProgrammingLanguage):
        equivalent_to = [
            PureFunctionalLanguage &
            SafeTypeCheckingLanguage &
            HasAlgebraicTypes
        ]

    class CompiledToByteCodeLanguage(ProgrammingLanguage):
        equivalent_to = [
            runs_on.some(ByteCodeInterpreter)
        ]

    class CompiledToMachineCodeLanguage(ProgrammingLanguage):
        equivalent_to = [
            runs_on.value(native_environment)
        ]

    class CompiledLanguage(ProgrammingLanguage):
        equivalent_to = [
            CompiledToByteCodeLanguage |
            CompiledToMachineCodeLanguage]

    class InterpretedLanguage(ProgrammingLanguage):
        equivalent_to = [
            runs_on.some(Interpreter)
        ]

    # inference that Scripting < Interpreted
    class ScriptingLanguage(ProgrammingLanguage):
        equivalent_to = [
            runs_on.some(LineByLineInterpreter)
        ]

    class ShellLanguage(ProgrammingLanguage):
        equivalent_to = [
            used_for.value(os_communication)
        ]

    # inference that JVMLanguage < Interpreted
    class JVMLanguage(ProgrammingLanguage):
        equivalent_to = [
            runs_on.value(jvm)
        ]

    class GarbageCollectedLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_memory_management.some(AutomaticMemoryManagement)
        ]

    class LanguageWithRuntime(ProgrammingLanguage):
        equivalent_to = [InterpretedLanguage | GarbageCollectedLanguage]

    class FastLanguage(ProgrammingLanguage):
        equivalent_to = [
            CompiledToMachineCodeLanguage &
            Not(LanguageWithRuntime)
        ]

    # inference that ReferenceCounted < GarbageCollected
    class ReferenceCountedLanguage(ProgrammingLanguage):
        equivalent_to = [
            has_memory_management.value(reference_counting)
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

    class FatherLanguage(ProgrammingLanguage):
        equivalent_to = [
            inspired.min(3, ProgrammingLanguage)
        ]

    # Individuals
    x86_assembly = ProgrammingLanguage("x86_assembly"
    , has_execution_type = [line_by_line_execution]
    , has_memory_management = [manual_memory_management]
    , runs_on = [native_environment]
    , has_type_safety = [weak_type_safety]
    , has_error_handling_type = [null_pointers]
    , used_for = [
        embedded_development
    ])

    c = ProgrammingLanguage("c", has_feature = [
        blocks,
        procedures,
        loops,
        structures,
        processes
    ], has_execution_type = [line_by_line_execution]
    , has_memory_management = [manual_memory_management]
    , runs_on = [native_environment]
    , has_type_checking = [static_type_checking]
    , has_type_safety = [weak_type_safety]
    , has_error_handling_type = [null_pointers]
    , used_for = [
        game_development,
        desktop_applications,
        os_development,
        embedded_development,
        compiler_development,
        database_management
    ])

    class CurlyBracketLanguages(ProgrammingLanguage):
        equivalent_to = [
            has_similar_syntax_to.value(c)
        ]

    c_pp = ProgrammingLanguage("c++", has_feature = [
        blocks,
        procedures,
        loops,
        classes,
        functions_as_first_class_citizens,
        higher_order_functions,
        inheritance,
        simple_enums,
        threads,
        co_routines
    ], has_execution_type = [line_by_line_execution]
    , has_memory_management = [manual_memory_management]
    , runs_on = [native_environment]
    , has_type_checking = [static_type_checking]
    , has_type_safety = [weak_type_safety]
    , has_error_handling_type = [
        null_pointers,
        exceptions
    ], used_for = [
        game_development,
        desktop_applications,
        enterprise_applications,
        os_development,
        embedded_development,
        compiler_development,
        database_management
    ], inter_op_with = [c]
    , inspired_by = [c]
    , has_similar_syntax_to = [c]
    )

    c_sharp = ProgrammingLanguage("c#", has_feature = [
        blocks,
        loops,
        classes,
        functions_as_first_class_citizens,
        higher_order_functions,
        inheritance,
        simple_enums,
        threads,
        async_functions,
        co_routines
    ], has_execution_type = [line_by_line_execution]
    , has_memory_management = [generational_GC]
    , runs_on = [dot_net_vm]
    , has_type_checking = [static_type_checking]
    , has_type_safety = [strong_type_safety]
    , has_error_handling_type = [
        null_pointers,
        exceptions
    ], used_for = [
        game_development,
        desktop_applications,
        enterprise_applications,
        web_applications
    ], inspired_by = [c_pp]
    , has_similar_syntax_to = [c]
    )

    java = ProgrammingLanguage("java", has_feature = [
        blocks,
        loops,
        classes,
        functions_as_first_class_citizens,
        higher_order_functions,
        inheritance,
        simple_enums,
        threads
    ], has_execution_type = [line_by_line_execution]
    , has_memory_management = [generational_GC]
    , runs_on = [jvm]
    , has_type_checking = [static_type_checking]
    , has_type_safety = [strong_type_safety]
    , has_error_handling_type = [
        null_pointers,
        exceptions
    ], used_for = [
        web_applications,
        cloud_applications,
        desktop_applications,
        enterprise_applications,
        mobile_applications
    ], inspired_by = [c_pp]
    , has_similar_syntax_to = [c]
    )

    kotlin = ProgrammingLanguage("kotlin", has_feature = [
        blocks,
        loops,
        classes,
        functions_as_first_class_citizens,
        higher_order_functions,
        inheritance,
        simple_enums,
        threads,
        case_classes
    ], has_execution_type = [line_by_line_execution]
    , has_memory_management = [generational_GC]
    , runs_on = [jvm]
    , has_type_checking = [static_type_checking]
    , has_type_safety = [strong_type_safety]
    , has_error_handling_type = [
        exceptions,
        errors_as_sum_types
    ], used_for = [
        web_applications,
        desktop_applications,
        enterprise_applications,
        mobile_applications
    ], inspired_by = [c_pp]
    , has_similar_syntax_to = [c]
    )

    python = ProgrammingLanguage("python", has_feature = [
        blocks,
        loops,
        classes,
        functions_as_first_class_citizens,
        higher_order_functions,
        inheritance,
        threads,
        async_functions,
        tuples
    ], has_execution_type = [line_by_line_execution]
    , has_memory_management = [reference_counting]
    , runs_on = [python_interpreter]
    , has_type_checking = [dynamic_type_checking]
    , has_type_safety = [strong_type_safety]
    , has_error_handling_type = [exceptions]
    , used_for = [
        web_applications,
        ai_development,
        scientific_computing,
        desktop_applications,
        enterprise_applications,
        os_development
    ])

    bash = ProgrammingLanguage("bash", has_feature = [
        blocks,
        loops
    ], has_execution_type = [line_by_line_execution]
    , has_memory_management = [manual_memory_management]
    , runs_on = [bash_interpreter]
    , has_type_safety = [weak_type_safety]
    , has_error_handling_type = [errors_as_values]
    , used_for = [os_communication]
    )

    powershell = ProgrammingLanguage("powershell",has_feature = [
        blocks,
        loops,
        classes,
        inheritance
    ], has_execution_type = [line_by_line_execution]
    , has_memory_management = [generational_GC]
    , runs_on = [dot_net_vm]
    , has_type_checking = [dynamic_type_checking]
    , has_type_safety = [weak_type_safety]
    , has_error_handling_type = [exceptions]
    , used_for = [os_communication]
    , inspired_by = [bash]
    )

    haskell = ProgrammingLanguage("haskell",has_feature = [
        tuples,
        rich_enums,
        functions_as_first_class_citizens,
        higher_order_functions,
        lazy_evaluation,
        pure_functions,
        strict_immutability,
        monad_concurrency
    ], has_execution_type = [evaluation_of_expression]
    , has_memory_management = [generational_GC]
    , runs_on = [native_environment]
    , has_type_checking = [static_type_checking]
    , has_type_safety = [strong_type_safety]
    , has_error_handling_type = [errors_as_sum_types]
    , used_for = [
        scientific_computing,
        highly_concurrent_applications,
        compiler_development,
        financial_software
    ])

    rust = ProgrammingLanguage("rust",has_feature = [
        blocks,
        loops,
        structures,
        functions_as_first_class_citizens,
        higher_order_functions,
        rich_enums,
        threads,
        async_functions,
        tuples,
        default_immutability
    ], has_execution_type = [line_by_line_execution]
    , has_memory_management = [borrow_checker]
    , runs_on = [native_environment]
    , has_type_checking = [static_type_checking]
    , has_type_safety = [strong_type_safety]
    , has_error_handling_type = [errors_as_sum_types]
    , used_for = [
        embedded_development,
        ai_development,
        game_development,
        web_applications,
        os_development,
        compiler_development,
        database_management
    ], inspired_by = [
        c_pp,
        haskell
    ], has_similar_syntax_to = [c]
    )

    go = ProgrammingLanguage("go",has_feature = [
        blocks,
        loops,
        structures,
        functions_as_first_class_citizens,
        higher_order_functions,
        co_routines
    ], has_execution_type = [line_by_line_execution]
    , has_memory_management = [generational_GC]
    , runs_on = [native_environment]
    , has_type_checking = [static_type_checking]
    , has_type_safety = [strong_type_safety]
    , has_error_handling_type = [errors_as_values]
    , used_for = [
        cloud_applications,
        enterprise_applications,
        web_applications
    ], inspired_by = [
        c,
        java
    ], has_similar_syntax_to = [c]
    )

    ruby = ProgrammingLanguage("ruby",has_feature = [
        blocks,
        loops,
        classes,
        functions_as_first_class_citizens,
        higher_order_functions,
        inheritance,
        simple_enums,
        threads
    ], has_execution_type = [line_by_line_execution]
    , has_memory_management = [generational_GC]
    , runs_on = [ruby_vm]
    , has_type_checking = [dynamic_type_checking]
    , has_type_safety = [strong_type_safety]
    , has_error_handling_type = [
        null_pointers,
        exceptions
    ], used_for = [web_applications]
    )

    php = ProgrammingLanguage("php",has_feature = [
        blocks,
        loops,
        classes,
        functions_as_first_class_citizens,
        higher_order_functions,
        inheritance,
        simple_enums,
        threads
    ], has_execution_type = [line_by_line_execution]
    , has_memory_management = [generational_GC]
    , runs_on = [php_interpreter]
    , has_type_checking = [dynamic_type_checking]
    , has_type_safety = [weak_type_safety]
    , has_error_handling_type = [
        null_pointers,
        exceptions
    ], used_for = [web_applications]
    , has_similar_syntax_to = [c]
    )

    scheme = ProgrammingLanguage("scheme",has_feature = [
        functions_as_first_class_citizens,
        higher_order_functions,
        strict_immutability
    ], has_execution_type = [evaluation_of_expression]
    , has_memory_management = [reference_counting]
    , runs_on = [scheme_repl]
    , has_type_checking = [dynamic_type_checking]
    , has_type_safety = [strong_type_safety]
    , has_error_handling_type = [
        research,
        ai_development
    ])

    closure = ProgrammingLanguage("closure",has_feature = [
        functions_as_first_class_citizens,
        higher_order_functions,
        strict_immutability
    ], has_execution_type = [evaluation_of_expression]
    , has_memory_management = [generational_GC]
    , runs_on = [jvm]
    , has_type_checking = [dynamic_type_checking]
    , has_type_safety = [strong_type_safety]
    , has_error_handling_type = [errors_as_values]
    , used_for = [highly_concurrent_applications]
    , inspired_by = [scheme]
    )

    scala = ProgrammingLanguage("scala",has_feature = [
        blocks,
        loops,
        classes,
        functions_as_first_class_citizens,
        higher_order_functions,
        rich_enums,
        case_classes,
        monad_concurrency,
        async_functions,
        tuples,
        default_immutability
    ], has_execution_type = [
        evaluation_of_expression,
        line_by_line_execution
    ], has_memory_management = [generational_GC]
    , runs_on = [jvm]
    , has_type_checking = [static_type_checking]
    , has_type_safety = [strong_type_safety]
    , has_error_handling_type = [errors_as_sum_types]
    , used_for = [
        cloud_applications,
        highly_concurrent_applications
    ], inspired_by = [
        java,
        haskell
    ])

    javascript = ProgrammingLanguage("javascript",has_feature = [
        blocks,
        loops,
        classes,
        functions_as_first_class_citizens,
        higher_order_functions,
        async_functions,
    ], has_execution_type = [line_by_line_execution]
    , has_memory_management = [generational_GC]
    , runs_on = [v8_engine]
    , has_type_checking = [dynamic_type_checking]
    , has_type_safety = [weak_type_safety]
    , has_error_handling_type = [exceptions]
    , used_for = [web_applications]
    , inspired_by = [java]
    , has_similar_syntax_to = [c]
    )

    typescript = ProgrammingLanguage("typescript",has_feature = [
        blocks,
        loops,
        classes,
        functions_as_first_class_citizens,
        higher_order_functions,
        async_functions,
        tuples,
        union_types
    ], has_execution_type = [line_by_line_execution]
    , has_memory_management = [generational_GC]
    , runs_on = [v8_engine]
    , has_type_checking = [static_type_checking]
    , has_type_safety = [strong_type_safety]
    , has_error_handling_type = [exceptions]
    , used_for = [web_applications]
    , inspired_by = [javascript]
    , has_similar_syntax_to = [c]
    )

    elm = ProgrammingLanguage("elm",has_feature = [
        tuples,
        rich_enums,
        pure_functions,
        functions_as_first_class_citizens,
        higher_order_functions,
        strict_immutability
    ], has_execution_type = [evaluation_of_expression]
    , has_memory_management = [generational_GC]
    , runs_on = [v8_engine]
    , has_type_checking = [static_type_checking]
    , has_type_safety = [strong_type_safety]
    ,has_similar_syntax_to = [haskell]
    , has_error_handling_type = [errors_as_sum_types]
    , used_for = [web_applications]
    , inspired_by = [
        haskell,
        javascript
    ])

    prolog = ProgrammingLanguage("prolog",has_feature = [
        rules,
        facts,
        strict_immutability
    ], has_execution_type = [evaluation_of_query]
    , has_memory_management = [reference_counting]
    , runs_on = [prolog_interpreter]
    , has_type_checking = [dynamic_type_checking]
    , used_for = [
        research,
        ai_development,
        compiler_development
    ])

    sql = ProgrammingLanguage("sql",has_feature = [
        queries,
        strict_immutability
    ], has_execution_type = [evaluation_of_query]
    , runs_on = [sql_server]
    , used_for = [databases]
    )

    matlab_language = ProgrammingLanguage("matlab_lang",has_feature = [
        loops,
        procedures,
        pure_functions,
        classes,
        inheritance,
        threads
    ], has_execution_type = [line_by_line_execution]
    , runs_on = [matlab]
    , has_type_safety = [strong_type_safety]
    , has_type_checking = [dynamic_type_checking]
    , used_for = [
        research,
        scientific_computing
    ])

    wolfram_language = ProgrammingLanguage("wolfram_lang",has_feature = [
        loops,
        procedures,
        pure_functions,
        threads
    ], has_execution_type = [line_by_line_execution]
    , runs_on = [wolfram]
    , has_type_safety = [strong_type_safety]
    , has_type_checking = [dynamic_type_checking]
    , used_for = [
        research,
        scientific_computing
    ])

    r = ProgrammingLanguage("r",has_feature = [
        blocks,
        loops,
        procedures,
        classes,
        inheritance
    ], has_execution_type = [line_by_line_execution]
    , runs_on = [r_studio]
    , has_type_safety = [strong_type_safety]
    , has_type_checking = [dynamic_type_checking]
    , used_for = [
        research,
        scientific_computing
    ])

AllDifferent([x86_assembly, os_communication, lazy_evaluation, inheritance, rules, facts, queries, functions_as_first_class_citizens, higher_order_functions, pure_functions, blocks, procedures, loops, default_immutability, strict_immutability, threads, co_routines, processes, async_functions, monad_concurrency, structures, tuples, classes, simple_enums, rich_enums, case_classes, union_types, line_by_line_execution, evaluation_of_expression, evaluation_of_query, manual_memory_management, reference_counting, generational_GC, borrow_checker, static_type_checking, dynamic_type_checking, strong_type_safety, weak_type_safety, null_pointers, exceptions, errors_as_sum_types, errors_as_values, web_applications, mobile_applications, desktop_applications, enterprise_applications, cloud_applications, scientific_computing, ai_development, os_development, game_development, database_management, compiler_development, embedded_development, financial_software, research, databases, highly_concurrent_applications, bash_interpreter, python_interpreter, jvm, dot_net_vm, ruby_vm, php_interpreter, v8_engine, scheme_repl, prolog_interpreter, matlab_language, wolfram_language, sql_server, r_studio, native_environment, c, c_pp, c_sharp, java, kotlin, python, bash, powershell, rust, go, ruby, php, haskell, scheme, closure, scala, javascript, elm, prolog, matlab, wolfram_language, r, sql])

# close_world(ProgrammingLanguage)
onto.save(file = "programming_languages.owl", format = "rdfxml")
