# tdd-python
A deep-dive of Test Driven Development with Python and the Django Framework

# Requirements
- [Install](https://askubuntu.com/questions/870530/how-to-install-geckodriver-in-ubuntu) `geckodriver`
# Todo:
- functional testing with `selenium` and `unit testing`
- Some buzz words:
- `Functional Test == Acceptance Test == Eng-to-End Test`

# Functional Tests Vs Unittests
- The basic distinction, though, is that
`functional tests` test the application from the outside, from the point of view of the `user`. That's why we use `selenium` to simulate as a user using a browser

- `Unit tests` test the application from the inside, from the point of view of theprogrammer.

# TDD Approach
- Our application wants to pass tests from the `user side` and `programmer side` as well.

- TDD cycle involves starting with a test that fails (functional test), then writing code to get it to pass(unittest)

1. We start by writing a functional test, describing the new functionality from the user’s point of view.

2. Once we have a functional test that fails, we start to think about how to write code that can get it to pass (or at least to get past its current failure). The `programmer's` point of view using `unittest`.

- Functional tests should help you build an application with the right functionality, and guarantee you never accidentally break it. Unit tests should help you to write code that’s clean and bug free














[Reference](Book:Test Driven Development with Python)