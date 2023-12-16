import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

required = ["paho-mqtt", "packaging"]

setuptools.setup(
    name="pybambu",
    version="1.0.0",
    author="Greg Hesp",
    author_email="greg.hesp+pybambulab@gmail.com",
    description="A python library to connect to the Bambu Lab X1C over MQTT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/greghesp/pybambu",
    install_requires=required,
    REQUIRED=required,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)