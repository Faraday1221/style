import setuptools

full = ["isort", "black", "flake8"]

setuptools.setup(
    name="style",
    version="0.0.0",
    entry_points={
        "console_scripts": ["style=src.style.__main__:cli"],
    },
    install_requires=["isort", "black", "flake8"],
    python_requires=">=3.6",
)
