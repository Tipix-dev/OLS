# tests/test_pipeline_generator.py

import importlib
import io
import json
import sys
from unittest.mock import patch

import pytest

MODULE_NAME = "src.lib.cicd_generator"  # замени если файл называется иначе


def load_module_with_config(config: dict):

    fake_stdin = io.StringIO(json.dumps(config))

    with patch.object(sys, "stdin", fake_stdin):
        if MODULE_NAME in sys.modules:
            del sys.modules[MODULE_NAME]

        return importlib.import_module(MODULE_NAME)


def test_python_pipeline_with_tests():
    config = {
        "stack": "python",
        "tests": True,
        "lint": False,
        "docker": False,
        "deploy": False,
    }

    mod = load_module_with_config(config)

    steps = mod.generate_python()

    step_names = [s["name"] for s in steps]

    assert "Install pytest" in step_names
    assert "Run tests" in step_names


def test_node_pipeline_with_lint():
    config = {
        "stack": "node",
        "tests": False,
        "lint": True,
        "docker": False,
        "deploy": False,
    }

    mod = load_module_with_config(config)

    steps = mod.generate_node()

    step_names = [s["name"] for s in steps]

    assert "Install lint" in step_names
    assert "Lint" in step_names


def test_go_pipeline_with_deploy():
    config = {
        "stack": "go",
        "tests": False,
        "lint": False,
        "docker": False,
        "deploy": True,
    }

    mod = load_module_with_config(config)

    steps = mod.generate_go()

    step_names = [s["name"] for s in steps]

    assert "Build" in step_names


def test_generate_steps_python():
    config = {
        "stack": "python",
        "tests": False,
        "lint": False,
        "docker": False,
        "deploy": False,
    }

    mod = load_module_with_config(config)

    steps = mod.generate_steps()

    assert isinstance(steps, list)
    assert len(steps) > 0


def test_build_pipeline_structure():
    config = {
        "stack": "python",
        "tests": True,
        "lint": True,
        "docker": False,
        "deploy": False,
    }

    mod = load_module_with_config(config)

    pipeline = mod.build_pipeline()

    assert pipeline["name"] == "CI"
    assert "jobs" in pipeline
    assert "build" in pipeline["jobs"]
    assert "steps" in pipeline["jobs"]["build"]


def test_unknown_stack_returns_empty_steps():
    config = {
        "stack": "rust",
        "tests": False,
        "lint": False,
        "docker": False,
        "deploy": False,
    }

    mod = load_module_with_config(config)

    steps = mod.generate_steps()

    assert steps == []
