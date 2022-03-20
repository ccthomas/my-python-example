import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="my_python_example",
    version="0.1.0",
    author="ccthomas",
    author_email="ccthom94@gmail.com",
    description="My Python Example",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ccthomas/my-python-example",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ]
)
