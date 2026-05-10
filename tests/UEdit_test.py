import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.lib.UEdit.main import UEditApp


def test_loads_existing_file(tmp_path: Path):
    test_file = tmp_path / "sample.txt"
    test_file.write_text("hello world", encoding="utf-8")

    app = UEditApp(str(test_file))

    assert app.file_content == "hello world"
    assert app.filepath == test_file


def test_missing_file_exits(tmp_path: Path):
    missing_file = tmp_path / "missing.txt"

    with pytest.raises(SystemExit) as exc:
        UEditApp(str(missing_file))

    assert exc.value.code == 1


def test_action_save_writes_file(tmp_path: Path):
    test_file = tmp_path / "save.txt"
    test_file.write_text("old text", encoding="utf-8")

    app = UEditApp(str(test_file))

    class MockEditor:
        text = "new text"

    class MockFooter:
        def __init__(self):
            self.message = ""

        def update(self, message):
            self.message = message

    app.editor = MockEditor()
    app.footer_widget = MockFooter()

    app.action_save()

    assert test_file.read_text(encoding="utf-8") == "new text"
    assert "Saved save.txt" in app.footer_widget.message
