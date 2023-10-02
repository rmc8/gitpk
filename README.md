# gitpk

## Description

`gitpk` is a simple yet powerful command-line tool. It clones a Git repository, automatically removes the `.git` directory, and then compresses the remaining content into a ZIP archive. To use the tool, all you need to do is specify the Git repository's URL and the desired name for the resulting ZIP file.

## Installation

`gitpk` is developed in Python. Use pip for installation.

```bash
pip install git+https://github.com/rmc8/gitpk.git
```

## Usage

The basic usage is as follows:

```bash
gitpk [repository_url] [output_zip_name]
```

-   `repository_url`: The URL of the Git repository you want to clone.
-   `output_zip_name`: The name you want for the resulting ZIP file. This is optional. If not specified, the repository's name will be used.

Example:

```bash
gitpk https://github.com/user/repo.git output_archive
```

If an invalid URL is provided, the tool will give an error message.

## Requirements

-   Python 3
-   Git

## Development

Clone the repository and install the necessary dependencies.

```bash
git clone https://github.com/rmc8/gitpk.git
cd gitpk
pip install -r requirements.txt
```

## License

For details, please refer to the [LICENSE](LICENSE) file.
