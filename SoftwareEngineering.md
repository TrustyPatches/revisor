# Software Engineering #


## Questions ##

### Maintaining Code Quality  ###

1. What are CASE tools used for?

2. Give some examples of the kinds of CASE tools that might be used.

3. What three key things do workbenches allow for?

4. What is an IDE?

5. Describe five essential Javadoc annotations.

6. Sum up what a test is in ten words or less.

7. Describe a typical TDD cycle.

8. Give a couple of examples of why TDD is beneficial to a project.

9. Define a test runner.

10. Define a test suite.

11. Define a test case.

12. Define a unit test.

13. Define a test fixture.

14. Define an integration test.

15. What are mock objects?

16. How can you create a test fixture with JUnit?

17. JUnit will automatically teardown a test fixture, but to ensure certain resources are closed correctly, what can you do?

18. How can we mark a method as a test in JUnit?

19. How can you make an assertion using the assertTrue method in JUnit?

20. What are the benefits of having programming standards?

### Working As A Team ###

1. What are the steps needed to carry out a synchronization merge?

2. What are the steps needed to carry out a reintegrate merge?

3. What is the high level process for creating a tag?

4. Give an example of the kind of diagram used in UML to represent a class.

5. What kind of relationships can be used between classes in a UML diagram? How can we draw them?

6. Describe the dependency relationship.

7. Describe the association relationship.

8. Describe the aggregation relationship.

9. Describe the composition relationship.

10. Describe the inheritance relationship.

11. How can we represent multiplicity in a UML diagram?

12. What is meant by coupling?

13. What is meant by cohesion?

14. What is vertical slicing?

15. What is horizontal slicing?

16. What is a use case diagram for?

17. What is an actor in a use case diagram?

18. What is a use case in a use case diagram?

19. What are the four kind of use case relationship that might appear in a use case diagram?

20. Describe the association relationship.

21. Describe the inclusion relationship.

22. Describe the extends relationship.

23. Describe the generatlisation relationship.

### Getting Code Right First ### 

1. What are some different frames that can appear in a sequence diagram?

2. What are some design pattern types?

3. Describe creational design patterns.

4. Give an example of a creational design pattern.

5. Describe structural design patterns.

6. Give an example of a structural design pattern.

7. Describe behavioural design patterns.

8. Give an example of a behavioural design pattern.

9. Describe architectural design patterns.

10. Give an example of an architectural design pattern.

11. Give some other examples of design patterns.

### Is My Code Good ###

1. What is testing used for?

2. Define what validation means in a project?

3. Define what verification means in a project?

4. What is scaffolding code?

5. Describe the testing taxonomy.

6. What is fault injection?

7. Define a direct measurement.

8. Define an indirect measurement.

9. How can you calculate cyclomatic complexity?


### Software Engineering Methodologies ###

1. What are the distinct phases characteristic of the waterfall methodology?

2. Draw a diagram depicting the project flow of a plan based development model.

3. Draw a diagram depicting the project flow of an agile development model.


## Answers ##

### Maintaining Code Quality  ### 

1. CASE tools (Computer Aided Software Engineering) support the software design process activities such as requirements engineering, design, program development and testing.

2. CASE tools include design editors, data dictionaries, compilers, debuggers, system building tools etc.

3. Workbenches allow for:
  * Presentation integration - A homogenous and consistent workspace.
  * Control integration - Easy migration of tools.
  * Data integration - Access to a common data set.

4. An IDE is a colleciton of CASE tools and workbenches. 

5. Essential Javadoc tags include:
  * @author - your name
  * @param - arguments to a method
  * @return - what the result is that gets returned
  * @throws - any exceptions that are thrown
  * @see - refer documentation for another class

6. A test is something we write once and run often.

7. A typical TDD cycle (red, green, refactor) will look like this:
  * (Re)write a test.
  * Make sure the test fails to compile, else go to 1.
  * Write production code.
  * Run all tests until they succeed, else go to 3.
  * Refactor code, go to 1.

8. Some benefits of TDD include:
  * Allows us to define the purpose and functionality of a method before implementing it.
  * Allows us to refactor or change the implementation of a class without fear of breaking it. 

9. A test runner is software that runs tests and reports results.

10. A test suite is a collection of test cases.

11. A test case tests the response of a single method to a particular set of inputs.

12. A unit test is a test of the smallest element of code you can sensibly test, usually a single class. 

13. A test fixture is the environment in which a test is run. 

14. An integration test is a test of how all classes work together. 

15. Proper unit testing involves mock objects, fake versions of classes with which the class under test interacts.

16. Create a test fixture with @Before public void init()

17. Clean up resources after a test with @After public void cleanUp()

18. Mark a test in JUnit with @Test

19. A typical assertion in JUnit looks something like: assertTrue("Test message here", getFive() == 5)

20. We have programming standards:
  * To allow automation
  * To avoid common errors
  * To make code more readable
  * To improve the language
      ... because 80% of project effort is maintenance


### Working As A Team ###

1. To perform a sync merge: 
  * Commit changes
  * Merge changes from trunk to branch
  * Commit merged changes to the branch

2. To perform a reintegrate merge:
  * Commit changes and checkout trunk
  * Merge changes from branch into trunk
  * Commit changes then delete trunk

3. We make a release candidate branch when we are looking to create a release. Once it passes necessary QA, we create a tag by copying from the release candidate branch. These tags are read only.

4. The diagram for a class in UML might look something like this example:
    |---------------|
    |    Student    | <-- Name
    |---------------|
    | name          | <-- Attributes
    | age           |
    |---------------|
    | takeNotes()   | <-- Operations
    | sleep()       |
    | eat()         |
    | sitExams()    |
    | goToLibrary() |
    |---------------|

5. The following relationships can exist between classes:

  weak  O               knows of >
        | Dependency  - - - - - - -
        |                 max >
        | Association -------------
        |                part of
        | Aggregation -----------<> (hollow arrow head)
        |                 is on
        | Composition -----------<> (filled in arrow head)
        |                 is a
        | Inheritance ------------>
strong  V

6. Dependency relationship:
  * Depends on other class
  * All other relationships imply dependency

7. Association relationship:
  * While one class can be used without the other, it is unlikely
  * Designed to work together, default relationship

8. Aggregation relationship:
  * One class will involve one or more instances of the other class
  * Can be built and destroyed separately

9. Composition relationship:
  * Very closely coupled
  * Destroying one will destroy contents

10. Inheritence relationship:
  * Most highly coupled
  * One is just a specialised version of the other

11. Can describe multiplicity like so:
  * Exact number, eg. (5)
  * Range of numbers, eg. (0..5)
  * Can use * for an arbitrary number, eg. (0..*)

12. The level of coupling describes the reliance of classes on each other. Highly coupled classes are bad and cannot be modified independently. They are hard to modify, hard to test and hard to reuse.

13. The level of cohesion measures the design of individual classes. If the methods that serve a class are closely related, they have high cohesion. Low cohesion classes are hard to maintain, hard to test, hard to reuse and hard to understand.

14. Vertical slicing: Finishing a whole path from input to output quickly so the entire program can be run as a whole, albeit with very limited (or faked) functionality. Allow the client to be involved early. Allows frequent, incremental functional builds and releases. 

15. Horizontal slicing: Assemblies or even single classes are perfected to gradually build up a program from the core components. Most effort is spent on perfecting individual modules. Sometimes necessary for key central service components. Delays feedback and can lead to overengineering.

16. A use case diagram is used to identify the primary elements and processes that from the system. The passing elements are termed as actors and the processes are called use cases. 

17. An actor represents some kind of person, organisation or external system that plays a role in one or more interactions with the system. An actor is drawn as a stick figure.

18. A use case describes a sequence of actions providing something of value to an actor. A use case is drawn as an ellipse.

19. Four kinds of use case relationship: inclusion, extends, generalisation, association.

20. Association relationship: Actors can be associated with a use case.

21. Inclusion relationship: A base use case contains an inclusion use case.

22. Extends relationship: An extends use case augments a base use case if an extension condition is satisfied.

23. Generalisation relationship: From specialist actors to generalised actors indicates the specialised actor is consistent with the generalised actor, possible with additional information.


### Getting Code Right First ###

1. Different frames can be used in sequence diagrams to portray different semantics:
    * opt: for conditionals; guard shows conditional statement
    * alt: shows mutually exclusive conditionals
    * loop: loop fragments while guard is true
    * par: parallel fragments execute in parallel
    * region: external region within which only one thread can run

2. Some design pattern types: Creational, structural, behavioural, architectural.

3. Creational design patterns: Try to create objects in a manner suitable to the situation. Uncontrolled object creation can lead to design problems, inefficiencies or added complexity.

4. Singleton: Restricts instantiation of a class to one object. 

5. Structural design patterns: Identify simple ways to implement relationships between entities.

6. Facade: Create a simplified interface to ease usage. Shields clients from complexity.

7. Behavioural design patterns: Identify common communication patterns between objects. They increase flexability in carrying out these communications.

8. Observer: Requests to observe an event raised by another object.

9. Architectural design patterns: Forms the basis of the application architecture.

10. MVC: Decouple model and view to reduce complexity.

11. Other examples of design patterns:

|-------------------------------------------------------|
| Creational | Structural | Behavioural | Architectural |
|-------------------------------------------------------|
| Singleton  | Facade     | Observer    | MVC           |
| Prototype  | Adapter    | Iterator    | MVVM          |
| Abstract   | Composite  | Mediator    | MVW           |
|   Factory  |            |             |               |
|-------------------------------------------------------|


### Is My Code Good ###

1. Testing is to cause failures in order to make faults visible so that they can be fixed and not delived in code that goes to customers.

2. Validate: Are we building the right software?

3. Verification: Are we building the software right?

4. Scaffolding code simulates the function of code that doesn't exist yet and isn't intended to be shipped. It uses:
    * Stubs: Modules that simulate components
    * Drivers: Used to test a module and provide inputs and control
    * Mock objects: Temporary substitutes for real objects. Must have same interface as real one.

5. Testing taxonomy:

|-------------|-------------------|--------------------|------------|------------|
| Type        | Specification     | Scope              | Opacity    | Done By?   |
|-------------|-------------------|--------------------|------------|------------|
| Unit        | Low level design, | No more than       | White box  | Programmer |
|             | Code structure    | one class          |            |            |
|             |                   |                    |            |            |
| Integration | Low level design, | Multiple classes   | White box, | Programmer |
|             | High level design |                    | Black box  |            |
|             |                   |                    |            |            |
| Functional  | High level design | Whole product      | Black box  | Tester     |
|             |                   |                    |            |            |
|             |                   |                    |            |            |
| System      | Requirements      | Whole product in   | Black box  | Tester     |
|             | Analysis          | representative env |            |            |
|             |                   |                    |            |            |
| Acceptance  | Requirements      | Whole product in   | Black box  | Customer   |
|             | Analyses          | customer env       |            |            |
|             |                   |                    |            |            |
| Beta        | Ad-hoc            | Whole product in   | Black box  | Customer   | 
|             |                   | customer env       |            |            |
|-------------|-------------------|--------------------|------------|------------|

6. Fault injection: Introduce faults to test code paths, in particular error handling paths that might be infrequently executed.

7. Direct measurement: Measuring an attribute without relying on any other.

8. Indirect measurement: Measuring an attribute by measuring many different attributes,

9. Calculating cyclomatic complexity:
    * Draw a control flow graph
    * CC = Edges - Vertices + 2
    * Derive a basis set of independent paths
    * Generate data to drive each path


### Software Engineering Methodologies ### 

1. In the waterfall model there are separate distinct phases:
  * Requirements analysis and definition
  * System and software design
  * Implementation and unit testing
  * Integration and system testing
  * Operation and maintenance

2. Plan based development:
  
        /--------------\                                                 /------------\
        |              |                                                 |            |
        V              |                                                 V            |
  /--------------------------\   /----------------------------\   /--------------------------\
  | Requirements engineering |-->| Requirements specification |-->| Design of implementation | 
  \--------------------------/   \----------------------------/   \--------------------------/
              ^                                                                 |
              |                                                                 |
              \-----------------------------------------------------------------/

3. Agile development:

  
  /----------------\         /------------------\
  | Requirements   | ------> | Design and       |
  |    engineering | <------ |   implementation |
  \----------------/         \------------------/
