import unittest

testList = [Test1, Test2]
testLoad = unittest.TestLoader()


TestList = []

for testCase in testList:
    testSuite = testLoad.loadTestsFromTestCase(testCase)
    TestList.append(testSuite)

newSuite = unittest.TestSuite(TestList)
runner = unittest.TextTestRunner()
runner.run(newSuite)

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    result = runner.run(test_suite)
    print("---- START OF TEST RESULTS")
    print(result)

    print("result::errors")
    print(result.errors)

    print("result::failures")
    print(result.failures)

    print("result::skipped")
    print(result.skipped)

    print("result::successful")
    print(result.wasSuccessful())

    print("result::test-run")
    print(result.testsRun())
    print("---- END OF TEST RESULTS")