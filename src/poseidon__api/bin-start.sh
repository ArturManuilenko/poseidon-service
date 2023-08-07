#!/bin/bash

echo ">>> $(basename ${BASH_SOURCE[0]})"
set -o errexit
set -o pipefail
set -o nounset
cd "$(dirname "${BASH_SOURCE[0]}")"
THIS_DIR=$(pwd)
cd ../../
CWD="$(pwd)"
export PYTHONUNBUFFERED=1
export PYTHONPATH="${CWD}"

# RUN
# ======================================================================================================

uldbutls waiting --db-uri="${POSEIDON__DB_URI}"

ulapiutls start --env="${APPLICATION_ENV}" --debug="${APPLICATION_RELOAD:-0}" --app-dir="${CWD}/src/poseidon__api" --port=${APPLICATION_PORT}
