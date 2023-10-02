from typing import List
from setuptools import setup


def get_requires(**kwargs) -> List[str]:
    with open("./requirements.txt", **kwargs) as f:
        txt: str = f.read()
        return txt.splitlines()


setup(
    name="gitpk",
    version="2023.10.02",
    description="A CLI tool to clone a Git repo, remove the .git directory, and zip the content.",
    author="rmc8",
    author_email="k@rmc-8.com",
    url="https://github.com/rmc8/gitpk",
    packages=["gitpk"],
    install_requires=get_requires(),
    entry_points={
        "console_scripts": [
            "gitpk = gitpk.__init__:clone_and_zip",
        ]
    }
)
