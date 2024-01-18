from owlready2 import *

class EvaluationStrategy(Thing):
    pass

strictEvaluation = EvaluationStrategy()
lazyEvaluation = EvaluationStrategy()

class TypeSystem(Thing):
    pass

staticTypeSystem = TypeSystem()
dynamicTypeSystem = TypeSystem()

class TypeStrictness(Thing):
    pass

strongTypeStrictness = TypeStrictness()
weakTypeStrictness = TypeStrictness()

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