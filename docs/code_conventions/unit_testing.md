## UT1 - Unit testing file structure

Mirror the folder structure of by:
- Placing all files containing unit tests in a folder named `test`
- There is a unit testing class corresponding to each class in the project. 
- Each file name starts with `test_`. e.g. `test_json_encoder.py`

## UT2 - AAA pattern

In addition to the [popular guidelines for the AAA pattern](https://docs.microsoft.com/en-us/dotnet/core/testing/unit-testing-best-practices#arranging-your-tests) we agree to:
- Separate the Arrange, Act, Assert sections of the unit test with a comment for each `# Arrange ` `# Act` `# Assert`
- When there is no “Arrange” section we do not write the `# Arrange `comment

If the unit test is small enough we can combine the Act and Assert into one section separated by `# Act & Assert` comment

## UT3 - Naming of the unit tests

Considering popular naming methods [here](https://dzone.com/articles/7-popular-unit-test-naming), we agree to following order 
- nameOfMethod_expectedBehaviour_senarioDescription 
  - e.g. MethodName_ShouldThrowException_WhenAgeLessThan18