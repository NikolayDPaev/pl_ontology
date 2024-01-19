from owlready2 import *

# evaluation

class EvaluationStrategy(Thing):
    pass

strictEvaluation = EvaluationStrategy()
lazyEvaluation = EvaluationStrategy()

# types

class TypeSystem(Thing):
    pass

staticTypeSystem = TypeSystem()
dynamicTypeSystem = TypeSystem()

class TypeStrictness(Thing):
    pass

strongTypeStrictness = TypeStrictness()
weakTypeStrictness = TypeStrictness()

# error handling

class ErrorHandling(Thing):
    pass

nullPointers = ErrorHandling()
exceptions = ErrorHandling()

class ErrorInReturnType(ErrorHandling):
    pass

errorsAsSumTypes = ErrorInReturnType()
errorsAsValues = ErrorInReturnType()

# use cases

class UseCase(Thing):
    pass

web = UseCase()
mobile = UseCase()
enterprise = UseCase()
servers = UseCase()
scientific = UseCase()
ai = UseCase()
os = UseCase()
gaming = UseCase()

# users

class User(Thing):
    pass

class Developer(User):
    pass

webDev = Developer()
enterpriseSoftwareDev = Developer()
mobileDev = Developer()
gameDev = Developer()

sysAdmin = User()
researcher = User()
dataAnalyst = User()