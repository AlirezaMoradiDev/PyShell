# Python Linux Commands

A collection of Linux command-line utilities reimplemented in Python. The goal of this project is to understand how common Unix tools work by recreating their core functionality from scratch using Python.

## Implemented Commands

| Command | Description |
|--------|-------------|
| `head` | Display the first lines or bytes of a file. |
| `tail`  | Display the last lines or bytes of a file. |
| `wc`   | Count lines, words, bytes, and characters in files. |

More commands will be added over time.

## Project Structure

```text
.
├── exceptions/
├── head.py
├── tail.py
├── wc.py
└── README.md
```

## Goals

- Learn how classic Unix utilities are implemented.
- Practice file I/O and stream processing.
- Improve Python programming skills.

## Usage
### `head`

```bash
python head.py <file>
```
Display the first 10 lines (default):

```bash
python head.py example.txt
```

### `wc`

```bash
python wc.py <file>
```

Examples:

```bash
python wc.py example.txt
```

```bash
python wc.py -l
```

```bash
python wc.py example.txt -c
```

## Features

- Command-line interface
- Designed to closely match the behavior of the original Linux commands

## Planned Commands

- [ ] `cat`
- [ ] `sort`
- [ ] `uniq`
- [ ] `grep`
- [ ] `cut`
- [ ] `tr`
- [ ] `tee`
- [ ] `paste`
- [ ] `nl`
- [ ] `tac`
- [ ] `basename`
- [ ] `dirname`

## Why?

Reimplementing Unix tools is an excellent way to learn:

- Text processing
- File handling
- Standard input/output
- Command-line argument parsing

## License

This project is licensed under the MIT License.