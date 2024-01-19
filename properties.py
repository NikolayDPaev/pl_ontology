from owlready2 import *
from sympy import symmetric_poly
from features import Feature
from memory_management import MemoryManagement
from others import ErrorHandling, EvaluationStrategy, TypeStrictness, TypeSystem, UseCase, User

from programming_language import ProgrammingLanguage
from running_environment import RunningEnvironment


class UsedBy(ObjectProperty):
    domain = [ProgrammingLanguage]
    range = [User]

class UsedFor(ObjectProperty):
    domain = [ProgrammingLanguage]
    range = [UseCase]

class BetweenLanguagesProperty(ObjectProperty):
    domain = [ProgrammingLanguage]
    range = [ProgrammingLanguage]

class HasSimilarSyntaxTo(BetweenLanguagesProperty):
    reflexive = True
    symmetric = True

class InspiredBy(BetweenLanguagesProperty):
    pass

class Inspired(BetweenLanguagesProperty):
    inverse_property = InspiredBy

class FromTheSameCreators(BetweenLanguagesProperty):
    reflexive = True
    symmetric = True
    transitive = True

class InterOpWith(BetweenLanguagesProperty):
    pass

class runsOn(ObjectProperty):
    domain = [ProgrammingLanguage]
    range = [RunningEnvironment]

class hasFeature(ObjectProperty):
    domain = [ProgrammingLanguage]
    range = [Feature]

# class defaultEvaluationType(ProgrammingLanguage):

class hasErrorHandlingType(ObjectProperty):
    functional = True
    domain = [ProgrammingLanguage]
    range = [ErrorHandling]

class hasEvaluationType(ObjectProperty):
    functional = True
    domain = [ProgrammingLanguage]
    range = [EvaluationStrategy]

class hasTypeSystemType(ObjectProperty):
    functional = True
    domain = [ProgrammingLanguage]
    range = [TypeSystem]

class hasTypeStrictness(ObjectProperty):
    functional = True
    domain = [ProgrammingLanguage]
    range = [TypeStrictness]

class hasMemoryManagement(ObjectProperty):
    functional = True
    domain = [ProgrammingLanguage]
    range = [MemoryManagement]
