
from setuptools import setup, find_packages

setup(
    name="multiversemd",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "watchdog",
        "python-frontmatter",
        "GitPython",
        "tiktoken",
        "anytree",
        "rich",
        "pydantic"
    ],
    entry_points={
        "console_scripts": [
            "multiversemd=multiversemd.cli:main",
        ],
    },
)

