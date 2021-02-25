# EcoExp

Setup python3 Environment
```bash
brew install python3
pip install virtualenv
virtualenv --python=/usr/bin/python3 venv
```

Enable Virtual Environment
```bash
source ./venv/bin/activate
deactivate
```

Record package usage
```bash
pip install -r requirements.txt
pip freeze > requirements.txt
```