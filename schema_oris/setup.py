import setuptools


with open("README.md", "r") as rf:
    long_description = rf.read()

setuptools.setup(
    name="schema_oris",
    version="0.0.2",
    author="mal_mel",
    author_email="olegsvetovidov@gmail.com",
    description="Generate marshmallow schema from dataclass",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mal-mel/kts_homeworks/tree/main/schema_oris",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
