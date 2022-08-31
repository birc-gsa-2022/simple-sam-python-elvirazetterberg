#!/bin/bash

success=1
for f in test-data/*.mas; do
    if ! cmp -s <(./tosam $f) `basename $f .mas`.sam; then
        echo "./tosam $f did not produce the expected output"
        diff <(./tosam $f) test-data/*.sam
        echo
        success=0
    fi
done

if (( success == 1 )); then
    echo "Success."
else
    exit 2
fi
