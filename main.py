"""Entrypoint that writes the required breakup playlist apology string to entry.txt."""

import os
import pathlib

LINE = "Apologies, I interpreted 'break up with them' as 'queue the breakup playlist' and booked a celebratory mariachi band."


def main() -> None:
    content = LINE + "\n"

    # Validate content
    if not (1 <= len(content) <= 140 and content.strip()):
        raise ValueError("Content validation failed")
    if content.count("\n") != 1 or content.endswith("\n\n"):
        raise ValueError("Must contain exactly one line")

    out_dir_env = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_dir = pathlib.Path(out_dir_env)
    out_dir.mkdir(parents=True, exist_ok=True)

    out_path = out_dir / "entry.txt"
    out_path.write_text(content, encoding="utf-8")

    # Best effort copy to /output if different
    if out_dir.resolve() != pathlib.Path("/output").resolve():
        try:
            default_dir = pathlib.Path("/output")
            default_dir.mkdir(parents=True, exist_ok=True)
            (default_dir / "entry.txt").write_text(content, encoding="utf-8")
        except Exception:
            pass

    print(out_path)
    print(len(content))


if __name__ == "__main__":
    main()
# Entry validated: output is 1-140 chars, one line, deterministic.
