#!/usr/bin/env python3
import json
import sys

import yaml

config = json.load(sys.stdin)

stack = config.get("stack")
tests = config.get("tests")
docker = config.get("docker")
lint = config.get("lint")
deploy = config.get("deploy")


# ----------------------------
# Helpers
# ----------------------------


def step(name, run=None, uses=None, with_block=None):
    s = {"name": name}
    if run:
        s["run"] = run
    if uses:
        s["uses"] = uses
    if with_block:
        s["with"] = with_block
    return s


# ----------------------------
# Node pipeline
# ----------------------------


def generate_node():
    steps = [
        step("Checkout", uses="actions/checkout@v4"),
        step("Install deps", run="npm install"),
    ]

    if tests:
        steps.append(step("Install jest", run="npm install --save-dev jest"))
        steps.append(step("Run tests", run="jest"))

    if lint:
        steps.append(step("Install lint", run="npm install -D @biomejs/biome"))
        steps.append(step("Lint", run="npx biome check ."))

    if docker:
        steps.append(step("Docker build", run="docker build -t app ."))
        steps.append(step("Docker run", run="docker run app"))

    if deploy:
        steps.append(step("Deploy", run="npm publish"))

    return steps


# ----------------------------
# Python pipeline
# ----------------------------


def generate_python():
    steps = [
        step("Checkout", uses="actions/checkout@v4"),
        step("Install deps", run="pip install -r requirements.txt"),
    ]

    if tests:
        steps.append(step("Install pytaest", run="pip install pytest"))
        steps.append(step("Run tests", run="pytest"))

    if lint:
        steps.append(step("Install ruff", run="pip install ruff"))
        steps.append(step("Lint", run="ruff check ."))

    if docker:
        steps.append(step("Docker build", run="docker build -t app ."))
        steps.append(step("Docker run", run="docker run app"))

    if deploy:
        steps.append(step("Build app", run="pyinstaller --onefile app.py"))

    return steps


# ----------------------------
# Golang pipeline
# ----------------------------


def generate_go():
    steps = [
        step("Checkout", uses="actions/checkout@v4"),
        step("Install deps", run="go mod tidy"),
    ]

    if tests:
        steps.append(step("Run tests", run="go test -v"))

    if lint:
        steps.append(step("Lint", run="go fmt ./..."))

    if docker:
        steps.append(step("Docker build", run="docker build -t app ."))
        steps.append(step("Docker run", run="docker run -it app"))

    if deploy:
        steps.append(step("Build", run="go build -o app ."))

    return steps


# ----------------------------
# Engine
# ----------------------------


def generate_steps():
    if stack == "node":
        return generate_node()
    if stack == "python":
        return generate_python()
    if stack == "go":
        return generate_go()
    return []


def build_pipeline():
    steps = generate_steps()

    return {
        "name": "CI",
        "on": ["push", "pull_request"],
        "jobs": {"build": {"runs-on": "ubuntu-latest", "steps": steps}},
    }


# ----------------------------
# Output
# ----------------------------

pipeline = build_pipeline()
print(yaml.dump(pipeline, sort_keys=False))
