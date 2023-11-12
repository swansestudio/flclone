# flclone

**flclone.py** is a Python script for converting audio files to FLAC format and cloning the creation and modification timestamps from the source file. 
This can be particularly useful for archiving purposes when you want to retain the original file's creation and modification data.

## Usage

```
python flclone.py source_file [timedonor_file]
```

- `source_file`: The audio file you want to convert to FLAC.
- `timedonor_file` (optional): If provided, the creation and modification timestamps will be cloned from this file. If not provided, timestamps will be taken from the source file.

## Example

```
python flclone.py audio.wav
```

This command converts the `audio.wav` file to FLAC and retains its original creation and modification timestamps.

```
python flclone.py audio.aif timestamp.txt
```
This command converts the `audio.aif` file to FLAC and clones the creation and modification timestamps from `timestamp.txt`.
```
python flclone.py audio.wav timestamp.wav
```
This command converts the `audio.wav` file to FLAC and clones the creation and modification timestamps from `timestamp.wav`.

Using the timestamp from another file can be useful in cases where you’ve edited the source file but still want to retain the timestamp from when it was recorded. 
This can also apply if you’ve re-recorded a new file, but it’s important to maintain the timestamp of the original file that was recorded in the past.



## Note

- Only handling up to two arguments is supported.
- Use the script responsibly and ensure compliance with the licenses of the audio files you are converting.

# flclone Installation Guide

Before using **flclone.py**, you need to ensure that you have Python and the necessary library installed on your system. Here are the steps:

## Step 1: Install Python

You can download Python from the official website: https://www.python.org/downloads/. Make sure to add Python to your PATH during the installation process.

## Step 2: Install the Required Library

**flclone.py** requires the `pydub` library. You can install it using pip, which is a package manager for Python. Open your command prompt or terminal and type the following command:

```python
pip install pydub
