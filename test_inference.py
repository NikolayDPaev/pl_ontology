from owlready2 import *

onto = get_ontology("http://example.org/test_inference.owl")

with onto:
    class ProgrammingLanguage(Thing): pass

    class RunningEnvironment(Thing): pass
    class Interpreter(RunningEnvironment): pass
    jvm = Interpreter('java_virtual_machine')

    class runsOn(ProgrammingLanguage >> RunningEnvironment):
        functional = True

    class InterpretedLanguage(ProgrammingLanguage):
        equivalent_to = [runsOn.some(Interpreter)]

    class JVMLanguage(ProgrammingLanguage):
        equivalent_to = [runsOn.value(jvm)]

    java = ProgrammingLanguage('java', runsOn = [jvm])
    AllDifferent([jvm, java])
    # close_world(onto)
    sync_reasoner_pellet()

print(onto.get_instances_of(JVMLanguage))
# [test_inference.java]
print(onto.get_children_of(InterpretedLanguage))