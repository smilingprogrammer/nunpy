import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nunpy",
    author="nunpy",
    author_email="abdulsoburoyewale@gmail.com",
    description="To remember few lines of code",
    keywords="nunp, nun, nunpy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tomchen/example_pypi_package",
    project_urls={
        "Documentation": "https://github.com/smilingprogrammer/nunpy",
        "Bug Reports": "https://github.com/smilingprogrammer/nunpy",
        "Source Code": "https://github.com/smilingprogrammer/nunpy",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    extras_require={
        "dev": ["check-manifest"],
    }
    # ,
    # install_requires=["requests", "requests-html", "lxml_html_clean"],
)
