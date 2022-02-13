from pathlib import Path

# BACKEND
BASE_DIR_B: Path = Path(__file__).parent
STATIC_PATH_B: Path = BASE_DIR_B.joinpath('static')
TEMPLATES_PATH_B: Path = BASE_DIR_B.joinpath('templates')

# FRONTEND
IMAGES_PATH_F: Path = Path('images')
BOOKS_PATH_F: Path = IMAGES_PATH_F.joinpath('books')

