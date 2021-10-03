import json
import sys
import os

try:
    from setuptools import setup
except ImportError:
    print('Error: this package requires setuptools to install; try `pip install setuptools`', file=sys.stderr)
    sys.exit(1)

script_path = os.path.dirname(os.path.realpath(__file__))


def get_metadata() -> dict:
    metadata = {}
    with open(os.path.join(script_path, 'metadata.json'), 'r') as metadata_file:
        metadata.update(json.load(metadata_file))
    with open(os.path.join(script_path, 'requirements.txt'), 'r') as requirements_file:
        # Parses only trivial requirements.txt
        requirements = []
        for line in requirements_file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            requirements.append(line)
        metadata['install_requires'] = requirements
    return metadata


setup(**get_metadata())
