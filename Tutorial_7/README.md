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

# Activity: Deploying a FastAPI Application with CI/CD

### Objective:
In this assignment, you will:
1. Deploy a simple FastAPI application on Render.
2. Set up GitHub workflows for formatting (using `black`) and linting (using `flake8`).
3. Configure branch protection rules to ensure code quality before merging pull requests.

### Steps:

1. **Create a FastAPI Application**:
    - Create a new FastAPI project with a simple endpoint (e.g., `GET /` that returns "Hello, World!").
    - You are more than welcome to use the FastAPI application you built in the previous tutorial (In fact it is encouraged :D)
    - Push your code to a new GitHub repository.


2. **Deploy on Render**:
    - Create a Render account if you don’t have one.
    - Follow the [Render FastAPI deployment guide](https://render.com/docs/deploy-fastapi) to deploy your application.
    - Ensure your application is live and accessible via the Render-provided URL.

3. **Set Up GitHub Workflows**:
    - Add a `.github/workflows/` directory in your repository.
    - Create a workflow file (e.g., `ci.yml`) to:
      - Check code formatting using `black`.
      - Lint the code using `flake8`.
    - Example workflow snippet:
      ```yaml
      name: CI

      on:
         push:
            branches:
              - main
         pull_request:

      jobs:
         lint-and-format:
            runs-on: ubuntu-latest
            steps:
              - name: Checkout code
                 uses: actions/checkout@v3

              - name: Set up Python
                 uses: actions/setup-python@v4
                 with:
                    python-version: '3.9'

              - name: Install dependencies
                 run: |
                    python -m pip install --upgrade pip
                    pip install black flake8

              - name: Run Black
                 run: black --check .

              - name: Run Flake8
                 run: flake8 .
      ```

4. **Add Branch Protection Rules**:
    - Go to your repository settings on GitHub.
    - Under "Branches," add a protection rule for the `main` branch.
    - Enable the following:
      - Require status checks to pass before merging.
      - Select your CI workflow as a required status check.
      - Require pull request reviews before merging.

5. **Test Your Setup**:
    - Create a new branch and make a code change that violates formatting or linting rules.
    - Open a pull request to merge into `main`.
    - Verify that the workflow runs and blocks the merge if checks fail.
    - Fix the issues, push the changes, and confirm the pull request can be merged once all checks pass.

### Deliverables:
- A link to your GitHub repository.
- The Render URL of your deployed FastAPI application.
- Screenshots showing:
  - The branch protection rule configuration.
  - A failed workflow due to formatting or linting issues.
  - A successful workflow after fixing the issues.

Good luck! :D