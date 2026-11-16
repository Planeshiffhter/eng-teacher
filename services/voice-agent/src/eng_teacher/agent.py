"""Stable CLI entrypoint; implementation lives in runtime.agent.

Retaining this module keeps the installed console script and declared entrypoint
usable after relocation, without an installation step during organization work.
"""

from .runtime.agent import main

if __name__ == "__main__":
    main()
