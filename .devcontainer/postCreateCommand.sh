#!/usr/bin/env bash

set -euo pipefail

git config --global --add safe.directory /workspaces/vscode-remote-try-django

sudo chown -R "$(whoami):" /home/vscode/.cache

curl -LsSf https://astral.sh/uv/install.sh | sh

uv sync

uvx pre-commit install
