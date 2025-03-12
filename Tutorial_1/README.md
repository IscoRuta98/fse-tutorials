# Git & GitHub, and Exercism

The bojective of this tutorial is to expose you to Git basics, and the Exercism platform

**Git**:

- Git is a version control software.
- Git is used as a command line tool and ran locally.
- Git allows us to track various versions/branches of a codebase.
- In addition it allows us to synchronous different versions of the same codebase (i.e. interact with local and remote branches).

**GitHub**:
- Github is a web application that allows git repositories to be hosted remotely.
- Provides extra functionality on top of git
- Mainly used by organisations to manage software projects.


## Git Basics

**Pre-requisite**:
- Make sure you have Git installed on your computer, and have an account on GitHub

1. **Initialize a local Git repository**  
   Navigate to your project directory using the command line, then initialize a new Git repository with the command:
   ```bash
   git init
   ```

2. **Add your files to the repository**
    Use the command:
    ```bash
    git add .
    ```
    to add all the files in your project directory. If you want to add specific files, you can specify them like this:
    ```bash
    git add <filename>
    ```

3. **Commit your changes**
    After adding your files, you need to commit your changes, which means recording them in the Git repository. Use:
    ```bash
    git commit -m "Your commit message"
    ```

4. **Create a remote repository on GitHub**
    Go to GitHub, log in to your account and click on the “+” button in the top-right corner. Select “New repository,” name your repository, add a description (optional), and click “Create repository.”

5. **Connect the local repository to the remote repository**
    Replace `your-remote-repository-URL` with the URL of your newly created GitHub repository:
    ```bash
    git remote add origin your-remote-repository-URL
    ```

6. **Push your changes to the remote repository**
    Finally, push your local changes to the remote repository:
    ```bash
    git push -u origin main
    ```
    `origin` is the default name for the remote repository on GitHub and `main` is the default branch name. After this command, your code will be available in your GitHub repository.

**References**:
- [Git Book](https://git-scm.com/book/en/v2)
- [Git videos](https://education.github.com/git-cheat-sheet-education.pdf)
- [Git & GitHub Tutorial for beginners](https://www.youtube.com/watch?v=tRZGeaHPoaw)



## Exercism

[Exercism](https://exercism.org/) is a free, open-source platform that offers interactive coding practice in a wide variety of programming languages, including Python. It provides structured exercises, each accompanied by test suites and community-driven feedback. This means you can usw the platform to improve your coding skills by working on real-world challenges, while also benefiting from guidance and insights shared by other developers.

On the [Python](https://exercism.org/tracks/python/) track, you’ll find exercises designed for beginners learning the basics, as well as more advanced tasks that help you hone your problem-solving skills. Whether you’re just starting out or looking to refine your expertise, Exercism’s collaborative environment ensures you get the support and practice you need. 

If you decide to explore beyond Python, the platform also hosts tracks for languages such as Java, C#, Ruby, and many more.
