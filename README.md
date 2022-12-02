# YAQN - Yeet Another Quick Note
> A fast, easy and OOTB app for taking your notes made in Python.

<img src="./assets/app.png" alt="A screenshot of the app" width=542>

## Installation
```
> pip install yaqn  # Install from pypi
> yaqn --check # Run the app and generate the config file
```

## How to use
Run the `yaqn` command, it will open the app. To save the note and close the app itself just press `Ctrl + Enter`.

### Open with a keyboard shortcut
This can't be done automatically by `pip`, please use the correct for your OS:
_**Comming soon...**_

## Configuration
Your configuration file is saved by default in:
- Unix-like: `~/.config/yaqn/config.toml`
- Windows: `%AppData%\yaqn\config.toml`

### Custom config path
You can use your custom path for the config using `--config`:
```
> yaqn ---config /path/to/config/directory
```
### Check the config file integrity
The argument `--check` allows you to create, check and repair the config file, just run the command and it will analyze the config:
```
> yaqn --check
[ INFO ] Check mode -> Config checked and operative
```

### Configuration structure
An ordinary config file looks like this:
```
notes_path = '/path/to/notes/directory'
extension = 'md'
```
And this is its structure:
| Parameter | Description | 
| --- | --- |
| `notes_path` | Define the path to the directory the notes will be saved. |
| `extension` | Define the extension the notes will be saves. _Remember to **not** put `.` before the extension itself._ |