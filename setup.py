from setuptools import setup, find_packages

setup(
    name="embers_client",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas",
        "numpy",
    ],
    author="Koichi Higashi",
    author_email="khigashi@nig.ac.jp",
    description="A client package for the EMBERS Database API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/khigashi1987/EMBERS_CLIENT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
