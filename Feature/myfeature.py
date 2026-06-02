#!/usr/bin/env python3

class MyFeature:
    """Basic feature example."""

    def __init__(self, name="MyFeature"):
        self.name = name

    def run(self, value):
        """Run the feature with a simple transformation."""
        return f"{self.name} processed {value}"


def feature_info():
    """Return info about the feature."""
    return {
        "name": "MyFeature",
        "description": "A basic Python feature example",
    }


def main():
    feature = MyFeature()
    result = feature.run("input data")
    print(result)
    print(feature_info())


if __name__ == "__main__":
    main()
    print("Welcome to DevAsc")
