import os

from templateframework.metadata import Metadata

def run(metadata: Metadata = None):
	inputs = metadata.all_inputs()
	os.system(f'git clone https://github.com/42Paris/minilibx-linux.git mlx && \
	   			sudo apt-get update && sudo apt-get install xorg libxext-dev zlib1g-dev libbsd-dev && \
	   			make -C ./mlx && bash ./mlx/test/run_tests.sh')
