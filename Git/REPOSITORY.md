# Creating and Managing a Git Repository

Creating a repository is simple, and the process is largely the same whether you
are starting a brand new repository or finally choosing to incorporate git in an
existing project.

## Creating a Repository

On GitHub, visit your repositories and click the `New` button. Enter a name,
description, whether its public or private, etc. README, .gitignore, and license
files will be discussed in the [Managing a Repository](#managing-a-repository)
section and can be ignored for now. Click the `Create repository` button.

GitHub now offers you the commands required to initialize a brand new repository
or push an existing one. One thing to note about the steps for an existing repo
is that it assumes you have already run the `git init` command in the project
folder. If this is an existing project but not already initialized for git, make
sure to complete this step.

To be redundant, GitHub tells you:

#### Create New Repository on the Command Line

```bash
echo "# test123" >> README.md # this creates a README markdown file
git init # initialize git repo in the current folder
git add README.md # add README.md to list of files being "tracked" by git
git commit -m "first commit" # commit the changes (the new file README.md) to the local branch
git branch -M main # rename the branch (by default "master") to "main"
git remote add origin git@github.com:villanovaieee/test123.git # add remote "origin" to track this repository
git push -u origin main # push the committed changes "upstream" to the "main" branch of our repository stored in "origin"
```

#### Push an Existing Repository from the Command Line

```bash
git remote add origin git@github.com:villanovaieee/test123.git
git branch -M main
git push -u origin main
```

#### Initialize a Git Repository in an Existing Project and then Push

```bash
git init # can't forget to init
git remote add origin git@github.com:villanovaieee/test123.git
git branch -M main
git push -u origin main
```

## Managing a Repository

### Common Files

We will first talk about the files GitHub offers to create for you from the
start: README.md, .gitignore, and a license.

1. A `README.md` file stored at the root of your project will be displayed on the
   GitHub homepage of your project. This should include all information that you
   would like to immediately make transparent to users of your code base. Feel free
   to view any of the markdown files in this repository in "raw" format for a view
   of markdown's syntax.

2. `.gitignore` files instruct git on files and folders that should not be
   tracked. For example, if you have a `.env` file with sensitive information on
   database connections or something similar, that should go in the .gitignore file
   so as not to be blasted on your public repository's GitHub page. If you're
   managing a nodejs project, the `node_modules` folder in the project can store
   hundreds of megabytes worth of dependencies that will make your repository
   unnecessarily large and should also be added to .gitignore. - Just adding .env or node_modules will ignore any files or folders with
   these names. You can prefix with a `/` to begin specifying absolute paths to
   specific files or folders, if some have the same name but only some should
   be ignored.

3. `Licenses` are used to make developers aware of the open-source nature of a
   project and under what pretenses it can be used or modified. These are typically
   stored in a `LICENSE` or `COPYING` file and are referenced heavily in the README
   or the code base. Two popular open source licenses are
   the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html)
   (v3) and the [MIT License](https://opensource.org/licenses/MIT).

### Basic Use of Git

We will reference the basic structure of the example repository in the
[`Example_Repository`](./Example_Repository/) folder.

We are creating a project with [Node.js](https://nodejs.org/en/), which has
the following file structure:

```
NodeJS Project
│   index.js
│   package-lock.json
│   package.json
│
└───node_modules
    └───dependency1
    │       package.json
    │       dependency1.js
    └───dependency2
            package.json
            dependency2.js
```

If we have a lot of dependencies, the node_modules folder can get exceptionally
large. We don't want to track it because package.json files will keep a list of
installed dependencies and allow users of the code to install the dependencies
locally using `npm install`. Just look at the package.json file in the example
repo.

Let's begin.

#### Initialize

Create a folder (i.e. Example_Repository). Navigate into the folder, and
initialize for git:

```bash
mkdir Example_Repository
cd Example_Repository
git init
```

In our case, initialize our Node.js project:

```bash
npm init -y
npm install print # specific to our example, this creates the node_modules folder with print inside it
```

Create an `index.js` file that carries out the intent of your project. In our
case, it unnecessarily uses the `print` package to print a simple template
string.

Add a `.gitignore` file and add `node_modules` or `/node_modules` so that git
won't track the folder. If you aren't using a Node.js project, just create any
old file and add it to your `.gitignore` file to test.

#### Committing our Changes

We've made changes to the repository, let's add and commit them:

```bash
git status # preview state of tracked files (unadded, added, modified, renamed, deleted, etc.)
git add . # add all changes (can also add specific folders/files)
git status # verify we added all of the changes (unnecessary, but good practice)
git commit -m "project initialized"
```

#### Linking to GitHub and Push

Follow the instructions in section [Push an Existing Repository from the Command Line](#push-an-existing-repository-from-the-command-line).

You can refresh the page on GitHub and view that the files have been pushed up
(without the node_modules folder assuming you're testing with a Node.js
project).

### Best Practices

#### Merging

TODO

#### Commits

The backbone of git is commits. Whenever you use the `git commit` command, you
are fixing a comment, a description, of the changes being commited. The log of
commits (viewable through `git log`) store the history of the repository.

Best practice is to commit often. If this is the first commit of the project,
you can be a bit loose on this rule so as to get a foundation moving, but once
the project is established commits should happen frequently.

Create a new file? Track it with `git add` and commit it with its intended
purpose: `git commit -m "initial login page commit"`. Add a new feature? Add and
`git commit -m "added profile picture to profile page"`.

**Commit messages should be 80 characters or less**. Longer descriptions can be
incorporated by not using the `-m` flag, which will create a temporary instance
of the commit in `vim`, a command line text editor that you can research using.

You don't necessarily need to push after every commit. You can just keep
committing important changes locally and push once you are ready to share the
changes/new feature with everyone else who has access to your repository.

#### Branching

A really powerful tool in git is the ability to create branches. The `main` or
`master` or `v1.0.0` or whatever you name it branch is the default branch used
by GitHub or clones/forks of your repository. It is encouraged to have more than
just this branch if rolling out a repository for production or working in a
team.

In the instance of others actually using your code base as a dependency in their
projects, whenever you change the main branch you change the code they use. Or
if this is a deployed app, this will be what your users see. So while
developing, use a `development` branch and maybe incorporate a `testing` or
`staging` branch so you can make changes and test changes without affecting
the end users on your main branch.

`git branch` will list branches in your repository while
`git branch <branch_name>` creates a branch. To navigate between branches, use
`git checkout`.

So say I want to create a development branch, I would use either of the
following options:

```bash
git branch development
git checkout development
# begin making changes
```

```bash
git checkout -b development
```

You will need to commit changes before checking out other branches so as not to
lose progress.
