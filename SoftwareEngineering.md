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

7. A typical TDD cycle (red, green, refactor) will look like this:
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
