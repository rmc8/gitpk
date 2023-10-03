import os
import re
import time
import shutil
import subprocess
from typing import Optional, List

import fire


class InvalidRepoURL(Exception):
    """Exception raised when an invalid repository URL is provided."""
    pass


def validate_repo_url(url: str) -> bool:
    pattern = re.compile(
        r'https?://(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)(\.git)?')
    return bool(pattern.match(url))


def run_command(command: List[str]):
    try:
        result = subprocess.run(
            command, check=True,
            text=True, capture_output=True,
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        return


def clone_and_pack(repo_url: str, output_zip_name: Optional[str] = None):
    if not validate_repo_url(repo_url):
        raise InvalidRepoURL(
            f"The provided URL '{repo_url}' does not seem to be a valid git repository URL.")
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    if output_zip_name is None:
        output_zip_name: str = repo_name
    run_command(["git", "clone", repo_url])
    time.sleep(3)
    try:
        shutil.rmtree(os.path.join(repo_name, ".git"))
    except PermissionError as e:
        print(e)
        
    shutil.make_archive(output_zip_name, "zip", repo_name)
    shutil.rmtree(repo_name)


def main():
    fire.Fire(clone_and_pack)


if __name__ == "__main__":
    main()
