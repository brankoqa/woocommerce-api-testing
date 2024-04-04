#!/bin/bash

# Check if the number of arguments provided is valid
if [ $# -ne 1 ] && [ $# -ne 2 ]; then
    echo "Usage: $0 <env_url> [pytest.mark]"
    exit 1
fi

# Exporting some variables
export ENV_URL="$1"

# Run tests using pytest
if [ $# -eq 1 ]; then
    # If only one argument is provided, run all tests
    if pytest ; then
        echo "All tests for env '$1' passed successfully!"
    else
        echo "Tests for env '$1' failed or not run."
        exit 1
    fi
else
    # If two arguments are provided, run tests with the specified marker
    if pytest -m "$2"; then
        echo "Tests for env '$1' and pytest.mark '$2' passed successfully!"
    else
        echo "Tests for env '$1' and pytest.mark '$2' failed or not run."
        exit 1
    fi
fi
