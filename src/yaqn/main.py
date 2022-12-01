from . import config
from pathlib import Path
from argparse import ArgumentParser, Namespace
from .gui import Gui
import typing

def main() -> None:
    parser: ArgumentParser = ArgumentParser(
        prog='yaqn',
        description='A markdown quicknote app made in python and gtk.'
    )

    parser.add_argument(
        '-c',
        '--config',
        default=None,
        required=False,
        dest='custom_config_path',
        help='Set a custom path (absolute) to the config file.',
        type=str,
    )

    args: Namespace = parser.parse_args()

    # Check if the custom config path selected by the user is a dir
    custom_config_path: Path | None
    if args.custom_config_path is not None and Path(args.custom_config_path).is_dir():
        custom_config_path = Path(args.custom_config_path)
    else:
        custom_config_path = None

    config_data: dict[str, typing.Any] = config.read_config(custom_config_path)

    gui: Gui = Gui(config_data['notes_path'], config_data['extension'])
