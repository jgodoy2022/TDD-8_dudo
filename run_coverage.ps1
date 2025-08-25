$env:PYTHONPATH = (Get-Location).Path
pytest --cov=src --cov-report=term-missing