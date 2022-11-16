#!/bin/bash

set -eu

cd /opt
python -m src.main --test ${1}
