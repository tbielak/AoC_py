@echo off
attrib -r -h .vs
rd /s .vs /q
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"
