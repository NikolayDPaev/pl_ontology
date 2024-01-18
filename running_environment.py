from owlready2 import *

class RunningEnvironment(Thing):
    pass

class Interpreter(RunningEnvironment):
    pass

class LineByLineInterpreter(Interpreter):
    pass

class ByteCodeInterpreter(Interpreter):
    pass

class NativeEnvironment(RunningEnvironment):
    pass

bash = LineByLineInterpreter()
jvm = ByteCodeInterpreter()
x86 = NativeEnvironment()
x64 = NativeEnvironment()
arm = NativeEnvironment()
mips = NativeEnvironment()