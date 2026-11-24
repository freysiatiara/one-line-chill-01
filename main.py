"""One Line, One Chill — a single sentence of horror.

Writes the entry line to the output file the grader reads.
Standard library only; no network, no secrets, no temp files.
"""

import os

ENTRY = (
    "My daughter's new drawing shows our family eating dinner, "
    "and I'm the one standing outside the window watching us eat."
)


def resolve_output_path():
    """Resolve where entry.txt goes.

    ENTRY_OUTPUT wins; then OUTPUT_DIR / MAKEFUN_OUTPUT_DIR;
    then /output/entry.txt when /output exists (the sandbox);
    otherwise a file next to this script — never the bare cwd.
    """
    explicit = os.environ.get("ENTRY_OUTPUT")
    if explicit:
        return explicit
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "entry.txt")


def main():
    # Gate check, mirroring the scorer: 1-200 chars, not only whitespace.
    if not ENTRY.strip() or len(ENTRY) > 200:
        raise ValueError("entry text fails the 1-200 character gate")
    path = resolve_output_path()
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")
    os.chmod(path, 0o644)
    # Read-back check: the file on disk must be byte-identical to the
    # intended entry, otherwise the submission would be silently wrong.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != ENTRY + "\n":
            raise ValueError("read-back mismatch: entry.txt does not match ENTRY")


if __name__ == "__main__":
    main()
