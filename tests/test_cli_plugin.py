"""Smoke tests: brkraw's CLI finds the installed example plugin and runs it."""

from brkraw.cli.main import build_parser, main


def test_foo_is_a_brkraw_command():
    _, subparsers = build_parser()
    assert "foo" in subparsers.choices


def test_foo_runs(capsys):
    assert main(["foo", "hello"]) == 0
    assert "hello" in capsys.readouterr().out
