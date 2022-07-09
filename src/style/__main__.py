import argparse
import shutil
import subprocess
from pathlib import Path


def _copy_setup(args) -> None:
    """Copy the default setup.cfg file to a user specified destination.

    If setup.cfg already exists in the destination, prompt the user
    for explicit permission to overwrite."""
    src = Path(__file__).parent.parent.parent / "setup.cfg"
    dst = Path(args.path) / "setup.cfg"
    print(f"src={src}\ndst={dst}")

    # if file exists in dst prompt user for manual override
    if dst.exists():
        if not _prompt(msg=f"{dst} exists... overwrite with {src}? (y/n) "):
            return None

    print(f"copying {src} to {dst}")
    shutil.copy2(src=src, dst=dst)


def _prompt(msg: str) -> bool:
    ans = {"y": True, "n": False}
    r = input(msg)
    if r in ans:
        return ans[r]
    else:
        _prompt(msg)


def _style(args):
    """Execute autoformatters and linters in the required order."""
    prgms = ["isort", "black", "flake8"]
    for p in prgms:
        print("=" * 30, p, "=" * 30)
        subprocess.run([p, args.path])


def cli():
    parser = argparse.ArgumentParser(description="Code style.")

    parser.add_argument(
        "path",
        default=".",
        nargs="?",
        help="The file or directory to perform code styling.",
    )
    parser.add_argument(
        "--init",
        action="store_true",
        help="Initialize a new project with the default setup.cfg.",
    )
    args = parser.parse_args()
    print(args)

    if args.init:
        _copy_setup(args)
        return None

    _style(args)


if __name__ == "__main__":

    cli()
