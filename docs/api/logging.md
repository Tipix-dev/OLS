# Logging in OLS

Logging is a core part of OLS. Every important action performed by OLS tools is recorded so that users can understand what happened inside the system.

The goal of logging is transparency, debugging, and reproducibility.

---

## Why logging exists

Logging helps users:

* understand what a command actually did
* detect and investigate errors (`EE`)
* debug scripts and pipelines
* reproduce previous actions

OLS treats logs as a first-class feature, not as an afterthought.

---

## What is logged

OLS tools may log:

* executed commands
* errors and warnings
* package downloads
* installation steps
* environment initialization

The amount of information depends on the tool and verbosity level.

---

## Log format

Logs are designed to be both:

* human-readable
* machine-friendly

Example:

```
[INFO] downloading package core-utils
[OK] installation completed
[EE] failed to fetch package index
```

---

## Error codes

OLS uses short error markers to make logs easier to scan.

Common markers:

* `INFO` — informational message
* `WARN` — warning
* `EE` — error
* `PANIC` critical error

These markers allow quick filtering in pipelines:

```
cat log.txt | grep EE
```

---

## Philosophy of logging

OLS logging follows a few principles:

* logs must be predictable
* logs must be easy to read
* logs must work well with Unix pipelines

Logging should help users understand the system instead of hiding its behaviour.
