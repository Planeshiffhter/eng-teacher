"""Stable CLI entrypoint; implementation lives in runtime.agent.

Retaining this module keeps the installed console script and declared entrypoint
pointing to an available module after relocation, without changing packaging.
Application execution is intentionally deferred during organization work.
"""

from .runtime.agent import main

if __name__ == "__main__":
    main()
