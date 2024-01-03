from setuptools import setup, find_packages

requires = [
    "toolz",
    "uuid",
    "numpy",
]

dev_requires = ["pytest", "pytest-sugar"]

setup(
    name="movie-data-generator",
    version="0.1.0",
    description="Synthetic movie ratings data generation",
    author="Tobias Knuth",
    packages=find_packages(),
    install_requires=requires,
    extras_require={"dev": dev_requires},
)
