from owlready2 import *
from sympy import symmetric_poly
from pl_ontology.features import Feature
from pl_ontology.memory_management import MemoryManagement
from pl_ontology.others import EvaluationStrategy, TypeStrictness, TypeSystem, UseCase, User

from pl_ontology.programming_language import ProgrammingLanguage
from pl_ontology.running_environment import RunningEnvironment


# Object properties

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
    inverse_property = Inspired

class Inspired(BetweenLanguagesProperty):
    inverse_property = InspiredBy

class FromTheSameCreators(BetweenLanguagesProperty):
    reflexive = True
    symmetric = True
    transitive = True

class InterOpWith(BetweenLanguagesProperty):
    pass

# Class properties

class runsOn(DataProperty):
    domain = [ProgrammingLanguage]
    range = [RunningEnvironment]

class hasFeature(DataProperty):
    domain = [ProgrammingLanguage]
    range = [Feature]

class hasEvaluationType(DataProperty):
    domain = [ProgrammingLanguage]
    range = [EvaluationStrategy]

class typeSystemType(DataProperty):
    domain = [ProgrammingLanguage]
    range = [TypeSystem]

class typeStrictness(DataProperty):
    domain = [ProgrammingLanguage]
    range = [TypeStrictness]

class hasMemoryManagement(DataProperty):
    domain = [ProgrammingLanguage]
    range = [MemoryManagement]
