# Unit testing

I have decided to use the [PyTest](http://doc.pytest.org/en/latest/) framework:

- It seems to "pythonic" (i.e. it just works, without any messing about extending classes and so forth)
- It offers something similar to what Maven and JUnit gave me as a Java developer-- a single command line tool to run tests, and a very easy way to write tests.

Python itself comes with some excellent unit test support.  You could just use the [unittest](https://docs.python.org/3/library/unittest.html) package from the standard library.


# Repository layout

I have placed all the tests in a "tests" directory, separate from the main code, but mirroring the directory layout.  The [other test layout](http://doc.pytest.org/en/latest/goodpractices.html#choosing-a-test-layout-import-rules) option is to place test modules with the main code.  If you are following my layout, but doing more advanced testing, do read the [warning](http://doc.pytest.org/en/latest/goodpractices.html#tests-outside-application-code).

## PyTest import rules

What PyTest does is to automatically "discover" test modules, and then one by one imports them and runs them.  It performs some magic to decide where to pretend the module is actally located.  To quote from the docs:

> If pytest finds a “a/b/test_module.py” test file while recursing into the filesystem it determines the import name as follows:
>   - determine basedir: this is the first “upward” (towards the root) directory not containing an __init__.py. If e.g. both a and b contain an __init__.py file then the parent directory of a will become the basedir.
>   - perform sys.path.insert(0, basedir) to make the test module importable under the fully qualified import name.
>   - import a.b.test_module where the path is determined by converting path separators / into ”.” characters. This means you must follow the convention of having directory and file names map directly to the import names.

You almost certainly want the "basedir" to be the root of the project, and so you may need to insert empty `__init__.py` files into the test directory structure.

A further side effect of this is that if you open for example `tests\test_nn.py` into an IDE, you may find that the IDE does not import `points` correctly.  This is because:

- PyTest will use the above rules and will actually run `test_nn.py` as if it were located in the root directory of the repo.  The directory `points` is certainly accessible here.
- The IDE will believe that `test_nn.py` is actually part of the `tests` package, which has no access to `points`.

There is an inconsistency here, however, in that while `pytest` will run all tests fine, selecting a single test which is nested in `tests\` won't work; for example `pytest tests\scipy\test_pdist.py` fails.


# Editor integration

## Spyder

I haven't explored spyder a great deal.  Perhaps this addon would be good to try:

- https://pypi.python.org/pypi/spyder-unittest

One manual work-around is the following.  When you are writing a unit test, place the file in the root of the repo, say `working_test.py`

- Spyder will follow imports correctly, so you can get code completion etc.
- To run the test, just use `pytest working_test.py`

Then, when done, move the test file to the correct location in the `tests` directory.

## Visual Studio Code

I've had more luck with [VS Code](https://code.visualstudio.com/)

- Download [Don Jayamanne's Python extension](https://github.com/DonJayamanne/pythonVSCode).  Use the instructions here: [Python on Visual Studio Code](https://code.visualstudio.com/docs/languages/python)

Then a little setup is required.  Open the setting JSON file (Menu "File" -> "Preferences" -> "Settings") and add:

    "python.linting.enabled": false,
    "python.linting.lintOnSave": false,

    "python.unitTest.pyTestEnabled": true

The first two lines are optional-- they turn off automatic linting of your code, which I find too aggressive to see all the time.  The final line is the important one.

Once you've made this change, open the repo as a "folder", and you'll find:

- At the bottom of the screen (the "status bar") you can now click "Run Tests"

If you open a test, you will also find that (perhaps only once all tests have been run) that each test method now has a magic menu item above it-- "Run Test"  or "Debug Test"

Unfortunately, this is not completely magic, and it doesn't cope with nested tests (e.g. `test\scipy\test_pdist.py`) for the same reasons as given above.
