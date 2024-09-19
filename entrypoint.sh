#!/bin/sh
set -e

if [ "$1" = "python" ] && [ "$2" = "db_ops.py" ]; then
    exec "$@"
elif [ "$1" = "backup" ] || [ "$1" = "restore" ]; then
    exec python db_ops.py "$@"
else
    flask db upgrade
    python seed.py
    exec python -m app
fi