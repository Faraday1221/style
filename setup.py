import setuptools

setuptools.setup(
    name="style",
    version="0.0.0",
    entry_points={
        "console_scripts": ["style=style.__main__:cli"],
    },
    install_requires=["isort", "black", "flake8"],
    python_requires=">=3.6",
    package_dir={"": "src"},
    packages=["style"],
    package_data={"style": ["data/setup.cfg"]},
)
