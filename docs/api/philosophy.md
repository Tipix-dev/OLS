# OLS Philosophy

OLS (Open Linux Shell) is designed to improve the terminal experience while staying close to the traditional Unix philosophy.

OLS does not try to replace the shell. Instead, it provides a consistent and friendly set of tools that make terminal workflows easier and more predictable.

---

## 1. Everything must be logged

OLS records important actions in logs.

This allows users to:

* trace what happened
* detect errors (`EE`)
* debug problems quickly

Logging makes the system transparent and easier to maintain.

---

## 2. Simple and friendly tools

OLS commands are designed to be easy to use and consistent.

Principles:

* minimal unnecessary flags
* consistent help commands (`--help` and `hp`)
* predictable command behaviour

Users should be able to understand tools quickly without memorizing complex syntax.

---

## 3. Designed for pipelines

OLS tools follow the Unix pipeline model.

Commands support standard streams:

* `stdin`
* `stdout`
* `stderr`

This allows them to integrate naturally with common Linux tools such as:

```
grep
awk
sort
uniq
```

---

## 4. Internet-first packages

OLS downloads packages from the Internet.

However:

* packages are downloaded **once**
* they can be used **offline afterwards**

This provides both flexibility and reliability.
