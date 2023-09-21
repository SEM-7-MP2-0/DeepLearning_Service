# DeepLearning_Service

- Get Started

```
virtualenv env
.\env\Scripts\activate.ps1
pip install -r requirements.txt
```

- Getting the configuration ready

Copy the .env.example file at the same location and save as .env
```
cp .env.example .env
```

- Hook install
```
pre-commit install --hook-type pre-commit --hook-type pre-push
```

- Hook run command
```
pre-commit run --all-files
```

- Lint

```
pylint $(git ls-files '*.py')
flake8 $(git ls-files '*.py')
```

- Format
```
black .
```

- Spin Docker container for development
```
 docker compose -f .\docker-compose-dev.yml up
```

- Remove chache and build
```
docker compose -f .\docker-compose-dev.yml up --build --remove-orphans --force-recreate
```
