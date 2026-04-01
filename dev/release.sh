#!/bin/bash

export PATH=/usr/bin:/usr/local/bin:$PATH

REPO_DIR="/home/artem/my_dir/projects/Bash/OLS"
cd "$REPO_DIR" || exit 1

TAG="v0.5.0"
git tag -f "$TAG"

git push origin main
git push origin dev
git push origin "$TAG" --force

