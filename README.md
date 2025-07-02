# TestingCodex

This repository contains a simple command line todo list application.

## mytodolist

`mytodolist.py` is a basic CLI for managing tasks stored in `tasks.json`.

### Usage

```
python mytodolist.py add "Buy milk"
python mytodolist.py list
python mytodolist.py done 1
python mytodolist.py delete 1
```

Tasks persist in `tasks.json` so they survive between runs.
