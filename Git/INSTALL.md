# Git Installation

Follow the steps below for your operating system and then check the installation
by running

```bash
git --version
```

You may need to restart your terminal after installation first.

## Windows

The git installer can be found on the official website for
[git](https://git-scm.com/download/win).

If using the installer, on the `Components` page whether or not you would like
Git GUI is up to you, but I would recommend installing `Git Bash` as I
personally prefer the bash shell over cmd or PowerShell and find it more suited
for development.

Also, use the bundled SSH which will come in handy later. Everything else can be
left default.

If you'd like to use a package management system like MacOS and Linux users, I
recommend taking a look at [Chocolatey](https://chocolatey.org/).

With chocolatey installed, installing git is as simple as

```bash
choco install git
```

## MacOS

If you use Xcode, there should be a binary shim of git at `usr/bin/git`. To
ensure you are using the latest version of git, it is still recommended to
install it with homebrew.

To check if you have homebrew installed, just enter into your terminal:

```bash
which brew
```

If not installed, you can install homebrew with the following command:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

With brew installed, run:

```bash
brew install git
```

This will install git to `usr/local/bin`, which by default should be a higher
priority in the `PATH` variable, thus causing your machine to use the brew
installation rather than the Xcode shim when `git` is called from the command
line.

To check this, run

```bash
echo "$PATH"
```

If `usr/local/bin` does not appear earlier than `usr/bin` in the `PATH`, then
look into adjusting your `PATH` variable to give `usr/local/bin` a higher
priority.
