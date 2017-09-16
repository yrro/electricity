#!/bin/bash

set -eu

python3 generate.py
gnuplot plot &
