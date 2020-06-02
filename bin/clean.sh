#!/bin/bash

find . -name __pycache__ | xargs rm -rf
rm -rf build
rm -rf src/scikit-pk.egg-info
rm -rf .pytest_cache