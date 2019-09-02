import setuptools

# setup(
#     name='adaptive_boxes',
#     version='0.1',
#     scripts=['adabox']
# )

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="adaptive-boxes",
    version="0.0.1",
    author="Juan Francisco Chango",
    author_email="jnfran92@gmail.com",
    description="Python package for rectangular decomposition of 2D scenes/binary images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jnfran92/adaptive-boxes",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
