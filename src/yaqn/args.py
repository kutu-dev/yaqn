import config
from pathlib import Path
from argparse import ArgumentParser, Namespace
from gui import Gui

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

if args.custom_config_path is not None:
    custom_config_path: Path = Path(args.custom_config_path)

    if not custom_config_path.exists() or not custom_config_path.is_dir():
        print('[ ERROR ] Invalid custom config path, returning to default...')
        custom_config_path = None

config_data: dict[str, any] = config.read_config(custom_config_path)

gui: Gui = Gui(config_data['notes_path'], config_data['extension'])
