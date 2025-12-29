#!/usr/bin/env bash

set -euo pipefail

sudo chown -R "$(whoami):" /home/vscode/.cache

nix profile add nixpkgs#nix-direnv
mkdir -p ~/.config/direnv
echo "source ~/.nix-profile/share/nix-direnv/direnvrc" >> ~/.config/direnv/direnvrc

nix develop --command uv run manage.py migrate

direnv allow
