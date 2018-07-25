#!/usr/bin/env bash
pycodestyle --max-line-length=100 src
pycodestyle --max-line-length=120 tests
