#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "rt") as fh:
    long_description = fh.read()

dependencies = [
    "chia-blockchain@git+https://github.com/Chia-Network/chia-blockchain.git@spend_sim_fix#2bbb7e1e94267f6ce716bd3dcec820c806cc577c",  # noqa
    "clvm_tools_rs==0.1.7",
    "click==7.1.2",
]

dev_dependencies = [
    "flake8",
    "mypy",
    "black==21.12b0",
    "pytest",
    "pytest-asyncio",
    "pytest-env",
]

setup(
    name="chia_internal_custody",
    version="0.0.1",
    packages=find_packages(exclude=("tests",)),
    author="Quexington",
    entry_points={
        "console_scripts": ["cic = cic.cli.main:main"],
    },
    package_data={
        "": ["*.clvm.hex", "*.clsp.hex"],
    },
    author_email="m.hauff@chia.net",
    setup_requires=["setuptools_scm"],
    install_requires=dependencies,
    url="https://github.com/Chia-Network/internal-custody",
    license="https://opensource.org/licenses/Apache-2.0",
    description="Custody puzzles and CLI tailored to Chia Network's business and security requirements",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Security :: Cryptography",
    ],
    extras_require=dict(
        dev=dev_dependencies,
    ),
    project_urls={
        "Bug Reports": "https://github.com/Chia-Network/internal-custody",
        "Source": "https://github.com/Chia-Network/internal-custody",
    },
)
