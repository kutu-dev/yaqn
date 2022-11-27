from pathlib import Path
import tomllib
import exceptions

DEFAULT_CONFIG_PATH: Path = Path(Path.home(), 'config')
DEFAULT_NOTES_PATH: Path = Path(Path.home(), 'config') # TODO REALISTIC PATH

def init_config(custom_path: Path | None = None) -> Path:
    """
    Check if the config path and file exist and configure a custom path if it is given.
    """
    config_path: Path = DEFAULT_CONFIG_PATH

    if custom_path != None:
        config_path = custom_path

    if not config_path.exists() or not config_path.is_dir():
        config_path.mkdir()

    yaqn_path: Path = Path(config_path, 'yaqn')
    yaqn_file: Path = Path(yaqn_path, 'config.toml')

    if not yaqn_path.exists() or not yaqn_path.is_dir():
        yaqn_path.mkdir()

    if not yaqn_file.exists() or not yaqn_file.is_file():
        yaqn_file.touch()

    return yaqn_file

def check_config(config_path: Path) -> None:
    """
    Check if the config file is valid
    """
    with open(config_path, 'rb') as config:
        # Check if the config is a valid toml file
        try:
            tomllib.load(config)
        except tomllib.TOMLDecodeError:
            regenerate_config(config_path)

        # Check if the config is following the expected structure
        loaded_config: dict = tomllib.load(config)
        match loaded_config:
            case {'notes_path': str()}:
                pass
            case _:
                regenerate_config(config_path)


def regenerate_config(config_path: Path) -> None:
    """
    Rewrite the config file with all the defaults.
    """
    with open(config_path, 'w') as config:
        config.write(f'notes_path = \'{DEFAULT_NOTES_PATH}\'')

def read_config(custom_path: Path | None = None) -> Path:
    """
    Read the config file, check it and repair it if is necessary.
    """
    config_path: Path = init_config(custom_path)
    check_config(config_path)

    with open(config_path, 'rb') as config:
        return tomllib.load(config)['notes_path']