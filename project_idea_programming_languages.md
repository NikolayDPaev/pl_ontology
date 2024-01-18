# Programming languages

## Concepts
### Language
 - LowLevel
 - HighLevel
 - Imperative = [AND Language [FILLS :HasFeature instructions]]
   - Assembly = [AND Imperative LowLevel [ALL :RunsOn NativeEnvironment]]
   - Structural = [AND Imperative HighLevel [FILLS :HasFeature loops]]
     - Procedural = [AND Structural [FILLS :HasFeature procedures]]
     - Fast = [AND Procedural LowLevel]
 - Declarative = [AND HighLevel [FILLS :HasFeature statements]]
   - Functional = [AND FunctionalInspired [ALL :HasFeature DefaultImmutability]]
     - PureFunctional = [AND Functional [FILLS :HasFeature pureFunctions] [FILLS :HasFeature strictImmutability]]
       - LazyEvaluated = [AND PureFunctional [FILLS :HasEvaluationType lazy]]
   - Logical = [AND Declarative [FILLS :HasFeature strictImmutability] [FILLS :HasFeature rules] [FILLS :HasFeature facts]]

 - HasAlgebraicTypes = [AND Language [ALL :HasFeature ProductTypes] [FILLS :HasFeature SumTypes]]
 - OOPInspired = [AND Language [ALL :HasFeature Structures]]
 - OOP = [AND Language [FILLS :HasFeature classes] [FILLS :HasFeature inheritance]]

 - FunctionalInspired = [AND Language [FILLS :HasFeature higherOrderFunctions]]

 - MultiParadigmLanguage = [AND OOPInspired FunctionalInspired]

 - StaticallyTyped = [AND Language [FILLS :TypeSystemType staticTypeSystem]]
 - DynamicallyTyped = [AND Interpreted [FILLS :TypeSystemType dynamicTypeSystem]]

 - StronglyTyped = [AND Language [FILLS :TypeStrictness strongTypeStrictness]]
 - WeaklyTyped = [AND Language [FILLS :TypeStrictness weakTypeStrictness]]
 - SafeTypeSystemLanguage = [AND StaticTyped StronglyTyped]

 - ModernFunctional = [AND PureFunctional SafeTypeSystemLanguage]

 - LanguageWithRuntime = [AND HighLevelLanguage]

 - Compiled
   - CompiledToByteCode = [AND Compiled [ALL :RunsOn ByteCodeInterpreter]]
   - CompiledToMachineCode = [AND Compiled [ALL :RunsOn NativeEnvironment]]

 - FastLanguage = [AND LowLevelLanguage, CompiledToMachineCodeLanguage, NOT(LanguageWithRuntime)]

 - Interpreted = [AND LanguageWithRuntime [FILLS :RunsOn Interpreter]]

 - Scripting = [AND Interpreted [FILLS :RunsOn LineByLineInterpreter]]

 - JVMLanguage = [AND Language [FILLS :RunsOn jvm]]

 - GarbageCollected = [AND LanguageWithRuntime [ALL :hasMemoryManagement AutomaticMemoryManagement]]

 - ReferenceCounted = [AND Language [FILLS :hasMemoryManagement referenceCounting]]

 - Multifunctional = [AND Language [EXISTS 2 :UsedFor]]

 - CurlyBracketLanguages = [AND Language [FILLS :HasSimilarSyntaxTo c]]

 - InfluencedLanguage = [AND Language [EXISTS 2 :InspiredBy]]

 - InfluentialLanguage = [AND Language [EXISTS 2 :Inspired]]

 - FatherLanguage = [AND Language [EXISTS 3 :Inspired]]

### Feature
 - instructions
 - statements
 - facts
 - rules
 - functionsAsFirstOrderCitizens
 - higherOrderFunctions
 - pureFunctions
 - procedures
 - loops
 - DefaultImmutability
   - strictImmutability
 - inheritance
 - ProductTypes
   - tuples
   - Structures
     - classes
 - sumTypes

### Evaluation
 - strict
 - lazy

### TypeSystem
 - staticTypeSystem
 - dynamicTypeSystem

### TypeStrictness
 - strongTypeStrictness
 - weakTypeStrictness

### MemoryManagement
 - AutomaticMemoryManagement
   - referenceCounting
   - TracingGC
     - g1
 - SemiAutomaticMemoryManagement
   - borrowChecker
 - ManualMemoryManagement

### RunningEnvironment
 - Interpreter
   - LineByLineInterpreter
     - bash
   - ByteCodeInterpreter
     - jvm
 - NativeEnvironment
   - x86
   - x64
   - arm
   - mips

### Use cases
 - web
 - mobile
 - enterprise
 - servers
 - scientific
 - ai
 - os
 - gaming

### User
 - Developer
   - Web developer
   - Enterprise software developer
   - Mobile developer
   - Game developer
 - SysAdmin
 - Researcher
 - Data analyst

## Roles
 - :Inspired
 - :InspiredBy
 - :UsedFor
 - :UsedBy
 - :InterOpWith
 - :FromTheSameCreators
 - :HasSimilarSyntaxTo
 - :HasMemoryManagement
 - :HasDataTypes
 - :RunsOn
 - :TypeSystemType
 - :HasEvaluationType

## Individuals
 - c
 - c++
 - c#
 <!-- - f# -->
 - java
 - kotlin
 - python
 - bash
 - powershell
 - rust
 - go
 - ruby
 - php
 - haskell
 - scheme
 - closure
 - scala
 - javascript
 - elm
 - prolog
 - matLab
 - wolframMathematica
 - r