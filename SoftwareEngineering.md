# Software Engineering #


## Questions ##


### Maintaining Code Quality  ###

### Working As A Team ###

### Getting Code Right First ### 

### Is My Code Good ###

### Software Engineering Methodologies ###


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

7. A typical TDD cycle will look like this:
  1. (Re)write a test.
  2. Make sure the test fails to compile, else go to 1.
  3. Write production code.
  4. Run all tests until they succeed, else go to 3.
  5. Refactor code, go to 1.

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

### Getting Code Right First ###

### Is My Code Good ###

### Software Engineering Methodologies ### 
