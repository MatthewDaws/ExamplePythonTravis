[![Build Status](https://travis-ci.org/MatthewDaws/ExamplePythonTravis.svg?branch=master)](https://travis-ci.org/MatthewDaws/ExamplePythonTravis)

# Example Python and Travis #

Learning how to properly structure a Python repository on GitHub, with unit tests, and Travis integration.

   - Ideas stolen from The Hitchhiker's Guide to Python.
   - [Structure of the repository](http://docs.python-guide.org/en/latest/writing/structure/#structure-of-the-repository)
   - [Python testing tools](http://docs.python-guide.org/en/latest/writing/tests/#tools)
   - [pytest](http://pythontesting.net/framework/pytest/pytest-introduction/)
   - [Continuous Integration](http://docs.python-guide.org/en/latest/scenarios/ci/)

## Repository structure

Keep it simple.  Have a `readme.md`.


## Tests

Here I use [pytest](http://doc.pytest.org/en/latest/).  The docs are good.  I haven't explored, much at all, the features pytest gives you.  Nor have I looked at mocking etc.

I have put tests in the `tests` directory:

   - Read and re-read [Conventions for Python test discovery](http://doc.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery)
   - Decide that we should put an empty `__init__.py` file in `tests`.  This will make pytest recurse back to the main directory before running tests.  You want to be here to import the package.
   - An alternative is to put tests in the same directory as the module they test.  Coming from a Java/Maven world, this seems cluttered to me.

You can run the tests by executing `pytest` or `py.test` in the root directory of the project.


## Travis CI integration

The [Travis](https://travis-ci.org/) documentation is very clear.

   - Read [Getting started](https://docs.travis-ci.com/user/getting-started/).  Skip over the language list and follow the instructions to link GitHub to Travis.
   - Now read the [Python section](https://docs.travis-ci.com/user/languages/python/).

If it all works, you should see your project on the travis page: [here's mine](https://travis-ci.org/MatthewDaws/ExamplePythonTravis).  To finish, we should of course:

   - [Embed a status image](https://docs.travis-ci.com/user/status-images/).

What's going on under the hood is that Travis will build your project on a set virtual machine image "in the cloud" (aka on one of their servers).  For python, there is no compile stage, and so the "build" stage is actually to run all of the tests.


## Still to do

   - docs
   - `requirements.txt` ??
   - Talk about https://codecov.io/
   - Talk about pypi.python.org 