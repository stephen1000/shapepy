import setuptools

with open("readme.md", "r") as f:
    long_description = f.read()

dev_req = [
    "black==20.8b1",
    "pylint==2.6.0",
]

test_req = ["pytest==5.4.3", "pytest-asyncio==0.14.0", "pytest-cov==2.10.1"]

setuptools.setup(
    name="shapepy",
    version="0.0.1",
    author="Stephen Lowery",
    author_email="author@example.com",
    description="A Python tool for programatically defining structures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    package_dir={"": "src"},
    packages=setuptools.find_packages("src"),
    entry_points={"console_scripts": ["shapepy = shapepy.cli:handle"]},
    install_requires=[
        "python-dotenv==0.15.0",
    ],
    extras_require={"dev": test_req + dev_req, "test": test_req,},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
