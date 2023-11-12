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
python flclone.py audio.mp3 timestamp.txt
```

This command converts the `audio.mp3` file to FLAC and clones the creation and modification timestamps from `timestamp.txt`.

## Note

- Only handling up to two arguments is supported.
- Use the script responsibly and ensure compliance with the licenses of the audio files you are converting.

