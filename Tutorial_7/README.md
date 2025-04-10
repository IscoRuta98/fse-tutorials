# Continous Integration & Continous Deployment (CI/CD) in Python

## Resources:
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Deploying FastAPI Application on Render](https://render.com/docs/deploy-fastapi)
- [Improving Code Quality with Flake8 and Black: A Guide for Python Developers](https://medium.com/@huzaifazahoor654/improving-code-quality-with-flake8-and-black-a-guide-for-python-developers-c374168d5884#:~:text=Flake8%20is%20a%20linter%20tool,quality%20of%20your%20Python%20code.)
- [Formatting and Linting Python Code with isort, black, and flake8 & using pre-commit](https://manishankarjaiswal.medium.com/formatting-and-linting-python-code-with-isort-black-and-flake8-39bf876666ed)

## What is CI/CD?

CI/CD stands for **Continuous Integration** and **Continuous Deployment** (or **Continuous Delivery**). It is a set of practices and tools that help developers automate parts of the software development process, such as building, testing, and deploying code. This makes it easier to release updates quickly and reliably.

### Continuous Integration (CI)
This is the practice of automatically building and testing code changes whenever developers push updates to a shared repository. It ensures that new changes work well with the existing codebase.

### Continuous Delivery (CD)
This involves automatically preparing code changes for release to production. The deployment is ready but requires manual approval before going live.

### Continuous Deployment (CD)
This takes automation a step further by automatically deploying code changes to production without requiring manual approval.

Together, CI and CD form a **CI/CD pipeline**, which is a series of automated steps that streamline the development process and reduce manual effort. This pipeline is a key part of modern DevOps practices.

To reference an image located in the `images/` directory within the same directory as this markdown file, you can use the following syntax:


[Visual example of CI/CD](/Tutorial_7/images/ci-cd-example.png)



### Why CI/CD is important in software development?


The short answer: Speed. The State of DevOps report found organizations that have “mastered” CI/CD deploy 208 times more often and have a lead time that is 106 times faster than the rest. While faster development is the most well-known benefit of CI/CD, a continuous integration and continuous delivery pipeline enables much more.

- Development velocity: Ongoing feedback allows developers to commit smaller changes more often, versus waiting for one release.

- Stability and reliability: Automated, continuous testing ensures that codebases remain stable and release-ready at any time.

- Business growth: Freed up from manual tasks, organizations can focus resources on innovation, customer satisfaction, and paying down technical debt.

## GitHub Actions

[Link to docs](https://docs.github.com/en/actions/about-github-actions/)

GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. You can create workflows that build and test every pull request to your repository, or deploy merged pull requests to production.

## Example of CI/CD in a Pyhton application:

https://github.com/IscoRuta98/todo-server

The above repo is an example of deploying a FastAPI application on Render and using GitHub Actions for CI. 