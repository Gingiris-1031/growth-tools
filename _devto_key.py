"""Single source for the dev.to API key. No secret lives in this file.
Reads DEVTO_API_KEY from the environment, falling back to the gitignored
~/.config/gingiris/secrets.env. Rotate the key in that one file only."""
import os


def devto_key():
    k = os.environ.get("DEVTO_API_KEY")
    if k:
        return k
    p = os.path.expanduser("~/.config/gingiris/secrets.env")
    if os.path.exists(p):
        for line in open(p):
            line = line.strip()
            if line.startswith("DEVTO_API_KEY="):
                v = line.split("=", 1)[1].strip()
                if v:
                    return v
    raise SystemExit(
        "DEVTO_API_KEY not set. Add it to ~/.config/gingiris/secrets.env "
        "(DEVTO_API_KEY=...) or export it in the environment."
    )
