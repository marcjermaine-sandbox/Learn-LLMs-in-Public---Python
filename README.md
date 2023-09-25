# Learn LLMs in Public (Python)

## Installation

To setup the dependencies, use `make` tool:

```sh
make setup-dependencies
```

To test the pre-commit checks, use `make run-all-pre-commits`.

## Development

To enable `pre-commit` configurations and check commit message formatting using `commitizen`, run the following command:

```sh
make setup-dependencies-and-checks
```

Before making commits, Git will automatically perform several checks using pre-commit hooks, including:

Check YAML: Ensures that YAML files are well-formed and do not contain syntax errors.

Check for added large files: Prevents large files from being added to the repository, helping to keep the repository size manageable.

Black (Python code formatting): Enforces consistent code formatting according to the Black Python code formatter, promoting code readability and maintainability.

Isort (Python import sorting): Ensures that Python imports are correctly sorted for consistency and readability, aiding in code organization.

Flake8 (PEP8 Standards): Enforces adherence to PEP8 coding standards, promoting code consistency and readability by checking for style and formatting issues.

Trim trailing whitespace: Removes unnecessary trailing whitespace from files, improving code cleanliness and reducing potential issues.

Fix end-of-file markers (EOF): Ensures that files have consistent end-of-file markers, preventing inconsistencies in line endings that can lead to version control conflicts.

If one of the test above fails, the commit will not proceed. Before making commits, it is ideal to add your changelogs to staging and run all the checks.

```sh
git add changes.py
make run-all-precommits
```

In addition to these checks, the commitizen tool assists in composing standardized commit messages, ensuring clarity and consistency in your commit history. To use commitizen, run the following command:

```sh
git cz c
```
