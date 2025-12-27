# vscode-remote-try-django

## Getting Started

### Installation

Install the dependencies:

```sh
uv sync
```

Install the lefthook script:

```sh
uv run -m lefthook install
```

### Development

Start the development server:

```sh
uv run manage.py runserver
```

Your application will be available at `http://127.0.0.1:8000/`.
