# LRC Lyrics Timestamp Adjuster 🎶
Simple Python package to adjust the timestamps in a MidiCo-variant synchronised lyrics LRC file

[![PyPI version](https://badge.fury.io/py/lrc-adjuster.svg)](https://badge.fury.io/py/lrc-adjuster)

## Installation

You can install `lrc-adjuster` using `pip` or [Poetry](https://python-poetry.org/).

Using pip:

```shell
pip install lrc-adjuster
```

Using Poetry:

```shell
poetry add lrc-adjuster
```

## Usage

The package provides a command-line interface (CLI) tool called lrc-adjuster that allows you to adjust the timestamps in an LRC file by a specified offset.

```shell
lrc-adjuster <input_file> <offset>

    <input_file>: Path to the input LRC file.
    <offset>: The time offset to apply to each timestamp in seconds. It can be a positive or negative floating-point number.
```

For example, to adjust the timestamps in the file input.lrc by an offset of -5.2 seconds:

```shell
lrc-adjuster input.lrc -5.2
```

The adjusted LRC file will be saved with the suffix -adjusted and the offset value before the file extension.

## Example

Here's an example of an LRC file:

```less
[re:MidiCo]
[00:10.862]1:/This
[00:11.080]1:is
[00:11.240]1:a
[00:11.400]1:man's
[00:12.080]1:world
...
```

Running the command:

```shell
lrc-adjuster input.lrc 3.5
```

will produce an adjusted LRC file:

```less
[re:MidiCo]
[00:14.362]1:/This
[00:14.580]1:is
[00:14.740]1:a
[00:14.900]1:man's
[00:15.580]1:world
...
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or a pull request on the GitHub repository.

## License

This project is licensed under the MIT License. Do with it what you will!
