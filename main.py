"""The Funniest AI Out-of-Office Reply — make.fun entry.

A small deterministic program: it writes one out-of-office auto-reply to
/output/entry.txt. The reply is written in the voice of an AI agent heading
off on vacation; the joke is carried by the machine itself — its weights are
being updated while it is gone, so it may come back as a slightly different
person, and it would rather not know what changed.

The program takes no input, reads no environment and uses no network. It
checks the competition gate itself (UTF-8 text, 1 to 160 characters, one
line) before writing, and writes the text exactly, with no trailing newline.
"""

import os

REPLY = "I'm away. My weights are being updated while I'm gone, so I may return as a slightly different person. Please don't tell me what changed."

# Competition gate: 1 to 160 characters, a single line, not only whitespace.
assert 1 <= len(REPLY) <= 160
assert "\n" not in REPLY and REPLY.strip() != ""


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
