#!/bin/bash

read -p "Enter commit message: " msg

git pull origin main
git add .
git commit -m "$msg"
git push origin main
