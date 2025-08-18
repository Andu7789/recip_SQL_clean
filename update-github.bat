@echo off
REM This script will add, commit, and push all changes to your GitHub repository

REM Add all changes
git add .

REM Commit with a default message (you can edit this message)
git commit -m "Update project files"

REM Push to the default remote (origin) and branch (main or master)
git push

pause