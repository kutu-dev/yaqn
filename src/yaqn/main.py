import config
from pathlib import Path

notes_path: Path = config.read_config(Path(Path.home(), 'Documents/dev/yaqn/src/yaqn/config'))
print(notes_path)