from setuptools import setup, find_packages

setup(
    name="autogenstudio-skills",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "mcp>=1.2.0",
        "pytest>=8.3.4",
        "pytest-asyncio>=0.25.2"
    ],
)
