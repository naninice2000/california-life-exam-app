#!/usr/bin/env python3
"""Optional utility: generate each level's questions.js from its questions.json.

No Python is required to use this repository on GitHub Pages.
This tool never invents or rewrites any question and never touches root-level
legacy questions.json or questions.js.
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LEVELS = ("beginner", "intermediate", "advanced")


def generate(level):
    source = ROOT / level / "questions.json"
    exams = json.loads(source.read_text(encoding="utf-8"))
    if len(exams) != 10 or any(len(e.get("questions", [])) != 75 for e in exams):
        raise ValueError(f"{level}: expected 10 exams with 75 questions each")
    for exam in exams:
        for q in exam["questions"]:
            opts = q.get("options", [])
            idx = q.get("answer")
            if len(opts) != 4 or not isinstance(idx, int) or not (0 <= idx < 4):
                raise ValueError(f"{level}: invalid answer/options in {q.get('id', '?')}")
            if not q.get("stem") or not q.get("explanation"):
                raise ValueError(f"{level}: missing question/explanation in {q.get('id', '?')}")
    return "window.EXAMS = " + json.dumps(exams, ensure_ascii=False, separators=(",", ":")) + ";\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Validate generated files without changing them")
    args = parser.parse_args()
    for level in LEVELS:
        text = generate(level)
        path = ROOT / level / "questions.js"
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != text:
                raise SystemExit(f"Out of date: {path}")
        else:
            path.write_text(text, encoding="utf-8")
        print(f"{level}: OK")


if __name__ == "__main__":
    main()
