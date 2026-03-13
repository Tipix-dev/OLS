# Contributing to OLS

> This is your first step in the **OLS project**!
> We are glad that you have decided to contribute to our project.

## How to Contribute
1. **Report Issues**
    - Use GitHub Issues to report bugs, request features, or suggest improvements.
    - Provide clear steps to reproduce problems.
2. **Create your PR (Pull request)**
    - Fork the repository
    - Create local clone:
    ```Bash
    git clone git@github.com:<your name>/<your repository>.git
    ```
    - Create a new branch:
    ```Bash
    git checkout -b feature-name
    ```
    - commit your changes:
    ```
    git add .
    git commit -m "Fix: correct path handling in mkfile"
    ```
    - push your branch:
    ```
    git push origin feature-name
    ```

## Code Style

OLS follows a few simple principles:

- Avoid unnecessary flags and options
- Commands must be **pipeline-friendly**
- Use **stdin / stdout / stderr** correctly
- Add **clear logging** when actions are performed

General guidelines:

- Use meaningful variable names
- Keep functions small
- Comment non-obvious logic
- Follow existing project style

## Recommendations

- Do not start with complex parts of the project.
- Begin with the **README**, documentation, or other small improvements.
- If you know **Bash**, you can help improve helper scripts.

> All contributions are welcome — from small documentation fixes to new features.
> Thanks for helping make *OLS* better! 💚

