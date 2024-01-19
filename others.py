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

webApplications = UseCase()
mobileApplications = UseCase()
desktopApplications = UseCase()
enterpriseApplications = UseCase()
cloudApplications = UseCase()
scientificComputing = UseCase()
aiDevelopment = UseCase()
osDevelopment = UseCase()
gamingDevelopment = UseCase()
databaseManagement = UseCase()
compilerDevelopment = UseCase()
embeddedDevelopment = UseCase()
financialSoftware = UseCase()
research = UseCase()
databases = UseCase()
highlyConcurrentApplications = UseCase()

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