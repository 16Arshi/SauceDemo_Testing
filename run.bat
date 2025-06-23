@echo off
call venv\scripts\activate
python -m pytest -v -m "sanity or regression"
pause