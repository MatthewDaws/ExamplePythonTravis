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

[Python modules](https://docs.python.org/3/tutorial/modules.html) are just valid python files.  When you "import" a module, the file is executed by the python iterpreter.  Read the docs for more.

A [Python package](https://docs.python.org/3/tutorial/modules.html#packages) is just a directory structure containing modules.  You add a `__init__.py` file to indicate that a directory is a package.  By default, this does nothing, and so it is common to include further `import` commands.

   - For example, `import points` runs two commands:
      - `import points.nn` which means that `points.nn` is imported into your namespace
      - `from points.point import Point` which means that `Point` now becomes a type in your namespace
      - see `example.py` for usage.  An interesting exercise is to change `__init__.py` to be empty, and see how then `example.py` needs to be modified.
   
To learn more, browse around github and see how they structure imports.  Or look at packages in your local python install.


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


## Pip setup

We should list the packages we require, both to help users, and to allow Travis to correctly install the dependencies.

   - As an example, fork this repository, and change `requirements.txt` to an empty file
   - The build should then fail, as `scipy` will no longer be found.
   - Travis installs `numpy` automatically, along with `pytest`, but little else.

TODO: Read up on how pip works.

## Still to do

   - docs
   - `requirements.txt` ??  Tried adding numpy, but that's already installed.
   - Talk about https://codecov.io/
   - Talk about pypi.python.org 