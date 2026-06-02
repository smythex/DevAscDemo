#!/usr/bin/env python3
"""Basic scaffolded Python script."""

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="A basic Python script scaffold.")
    parser.add_argument("--name", default="World", help="Name to greet.")
    return parser.parse_args()


def main():
    args = parse_args()
    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
