#!/bin/bash

# This script will help delete unnecessary files from the repository
# Run this script locally after cloning the repository

# Remove __pycache__ directories
find . -type d -name "__pycache__" -exec rm -rf {} +

# Remove .DS_Store files
find . -name ".DS_Store" -delete

# Remove other unnecessary files
find . -name "*.pyc" -delete
find . -name "*.pyo" -delete
find . -name "*.pyd" -delete
find . -name ".pytest_cache" -exec rm -rf {} +
find . -name ".coverage" -delete
find . -name "htmlcov" -exec rm -rf {} +
find . -name ".tox" -exec rm -rf {} +
find . -name ".nox" -exec rm -rf {} +
find . -name ".hypothesis" -exec rm -rf {} +
find . -name ".egg-info" -exec rm -rf {} +
find . -name "*.egg" -delete
find . -name "*.so" -delete
find . -name "*.pyd" -delete
find . -name "*.dll" -delete
find . -name "*.exe" -delete

echo "Cleanup completed!"