from setuptools import setup, find_packages
import re


def get_requirements(file_path: str) -> list[str]:
    """Return validated requirements from a requirements file.

    - Strips BOMs and whitespace
    - Ignores blank lines and comments
    - Ignores editable markers like '-e .' and pip option lines
    - Validates requirement format using `packaging` when available,
      otherwise falls back to a conservative regex and raises on failure.
    """
    requirements: list[str] = []
    try:
        from packaging.requirements import Requirement as _PackReq
    except Exception:
        _PackReq = None

    simple_re = re.compile(r"^[A-Za-z0-9_.+-]+(\[.*\])?(\s*(?:[<>=!~]=?).+)?$")

    with open(file_path, encoding="utf-8") as f:
        for raw in f:
            line = raw.strip().lstrip('\ufeff')
            if not line or line.startswith('#'):
                continue
            if line.startswith('-e') or line.startswith('- e'):
                # editable installs should not be listed in requirements
                continue
            if line.startswith('--'):
                # pip options
                continue

            # Validate format
            if _PackReq is not None:
                try:
                    _PackReq(line)
                except Exception as exc:
                    raise ValueError(f"Invalid requirement '{line}': {exc}")
            else:
                if not simple_re.match(line):
                    raise ValueError(
                        "Invalid requirement '{0}': cannot validate because 'packaging' "
                        "is not installed; also failed basic regex check.".format(line)
                    )

            requirements.append(line)

    return requirements


setup(
    name='mlproject',
    version='3.13.9',
    author='jathinreddy3515',
    author_email='kjathin498@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)