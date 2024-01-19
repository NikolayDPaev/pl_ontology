from owlready2 import *

onto = get_ontology("http://example.org/programming_languages.owl")

from memory_management import *
from running_environment import *
from properties import *
from others import *
from programming_languages_individuals import *
from features import *

class ProgrammingLanguage(Thing):
    pass

class HighLevelLanguage(ProgrammingLanguage):
    hasFeature.min(1, Abstraction)

class LowLevelLanguage(ProgrammingLanguage):
    hasFeature.max(1, Abstraction)

class ConcurrentLanguage(ProgrammingLanguage):
    hasFeature.only(Concurrency)

class ImperativeLanguage(ProgrammingLanguage):
    hasFeature.only(instructions)

class StructuredLanguage(ImperativeLanguage):
    hasFeature.only(CodeStructures)

class AssemblyLanguage(ImperativeLanguage, LowLevelLanguage):
    runsOn.only(NativeEnvironment)

class ProceduralLanguage(StructuredLanguage):
    hasFeature.only(procedures)

class DeclarativeLanguage(HighLevelLanguage):
    hasFeature.only(Statements)

class FunctionalInspiredLanguage(HighLevelLanguage):
    hasFeature.only(functionsAsFirstOrderCitizens)
    hasFeature.only(higherOrderFunctions)

# inference that FunctionalLanguage is Declarative
class FunctionalLanguage(FunctionalInspiredLanguage):
    hasFeature.only(Statements)
    hasFeature.only(defaultImmutability)

class PureFunctionalLanguage(FunctionalLanguage):
    hasFeature.only(pureFunctions)
    hasFeature.only(strictImmutability)

class LazyEvaluatedLanguage(PureFunctionalLanguage):
    hasFeature.only(lazyEvaluation)

# inference that LogicLanguage is Declarative
class LogicLanguage(ProgrammingLanguage):
    hasFeature.only(facts)
    hasFeature.only(rules)

# inference that QueryLanguage is Declarative
class QueryLanguage(ProgrammingLanguage):
    hasFeature.only(Statements)

class HasAlgebraicTypes(ProgrammingLanguage):
    hasFeature.only(ProductTypes)
    hasFeature.only(SumTypes)

class OOPInspiredLanguage(ProgrammingLanguage):
    hasFeature.only(Structures)

class OOPLanguage(OOPInspiredLanguage):
    hasFeature.only(classes)
    hasFeature.only(inheritance)

class MultiParadigmLanguage(OOPInspiredLanguage, FunctionalInspiredLanguage):
    pass

class StaticallyTypedLanguage(ProgrammingLanguage):
    hasTypeSystemType.only(staticTypeSystem)

class DynamicallyTypedLanguage(ProgrammingLanguage):
    hasTypeSystemType.only(dynamicTypeSystem)

class StronglyTypedLanguage(ProgrammingLanguage):
    hasTypeStrictness.only(strongTypeStrictness)

class WeaklyTypedLanguage(ProgrammingLanguage):
    hasTypeStrictness.only(weakTypeStrictness)

class SafeTypeSystemLanguage(StaticallyTypedLanguage, StronglyTypedLanguage):
    pass

class ErrorSafeLanguage(ProgrammingLanguage):
    hasErrorHandlingType.only(ErrorInReturnType)

class SafeLanguage(ErrorSafeLanguage, SafeTypeSystemLanguage):
    pass

class ModernFunctionalLanguage(PureFunctionalLanguage, SafeTypeSystemLanguage):
    pass

class CompiledLanguage(ProgrammingLanguage):
    pass

class LanguageWithRuntime(HighLevelLanguage):
    pass

class CompiledToByteCodeLanguage(CompiledLanguage):
    runsOn.only(ByteCodeInterpreter)

class CompiledToMachineCodeLanguage(CompiledLanguage):
    runsOn.only(NativeEnvironment)

class FastLanguage(CompiledToMachineCodeLanguage):
    Not(LanguageWithRuntime)

class InterpretedLanguage(LanguageWithRuntime):
    runsOn.only(Interpreter)

# inference that Scripting < Interpreted
class ScriptingLanguage(ProgrammingLanguage):
    runsOn.only(LineByLineInterpreter)

class ShellLanguage(ScriptingLanguage):
    UsedFor.only(os)

# inference that JVMLanguage < Interpreted
class JVMLanguage(ProgrammingLanguage):
    runsOn.only(LineByLineInterpreter)

class GarbageCollectedLanguage(LanguageWithRuntime):
    hasMemoryManagement.only(AutomaticMemoryManagement)

# inference that ReferenceCounted < GarbageCollected
class ReferenceCountedLanguage(ProgrammingLanguage):
    hasMemoryManagement.only(referenceCounting)

class CurlyBracketLanguages(ProgrammingLanguage):
    HasSimilarSyntaxTo.only(c)

class MultifunctionalLanguage(ProgrammingLanguage):
    UsedFor.min(2, UseCase)

class PopularLanguage(ProgrammingLanguage):
    UsedBy.min(3, User)

class InfluencedLanguage(ProgrammingLanguage):
    InspiredBy.min(2, ProgrammingLanguage)

class InfluentialLanguage(ProgrammingLanguage):
    Inspired.min(2, ProgrammingLanguage)

class FatherLanguage(Thing):
    Inspired.min(3, ProgrammingLanguage)


onto.save()