#!/bin/bash

# Remove __pycache__ directories
git rm -r --cached chatbot_app/__pycache__/
git rm -r --cached image_app/__pycache__/
git rm -r --cached prompt_app/__pycache__/
git rm -r --cached vision_app/__pycache__/
git rm -r --cached web_app/__pycache__/

# Remove .DS_Store files
git rm --cached image_app/.DS_Store
git rm --cached prompt_app/.DS_Store
git rm --cached vision_app/.DS_Store
git rm --cached web_app/.DS_Store
git rm --cached .DS_Store 2>/dev/null

# Commit changes
git commit -m "Remove unnecessary files (pycache, DS_Store)"