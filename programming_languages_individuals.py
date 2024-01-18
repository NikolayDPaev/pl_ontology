from owlready2 import *
from pl_ontology.properties import Inspired

from programming_language import *

c = FastLanguage()
c.is_a.append(LowLevelLanguage)
c.is_a.append(StructuredLanguage)
c.is_a.append(CompiledLanguage)
c.is_a.append(StaticallyTypedLanguage)
c.is_a.append(WeaklyTypedLanguage)

c_pp = FastLanguage()
c_pp.is_a.append(LowLevelLanguage)
c_pp.is_a.append(StructuredLanguage)
c_pp.is_a.append(OOPLanguage)
c_pp.is_a.append(CompiledLanguage)
c_pp.is_a.append(StaticallyTypedLanguage)
c_pp.is_a.append(StronglyTypedLanguage)

c_sharp = OOPLanguage()
c_sharp.is_a.append(StructuredLanguage)
c_sharp.is_a.append(GarbageCollectedLanguage)
c_sharp.is_a.append(StaticallyTypedLanguage)
c_sharp.is_a.append(StronglyTypedLanguage)


java = ProgrammingLanguage()
kotlin = ProgrammingLanguage()
python = ProgrammingLanguage()
bash = ProgrammingLanguage()
powershell = ProgrammingLanguage()
rust = ProgrammingLanguage()
go = ProgrammingLanguage()
ruby = ProgrammingLanguage()
php = ProgrammingLanguage()
haskell = ProgrammingLanguage()
scheme = ProgrammingLanguage()
closure = ProgrammingLanguage()
scala = ProgrammingLanguage()
javascript = ProgrammingLanguage()
elm = ProgrammingLanguage()
prolog = ProgrammingLanguage()
matlab = ProgrammingLanguage()
wolframMathematica = ProgrammingLanguage()
r = ProgrammingLanguage()