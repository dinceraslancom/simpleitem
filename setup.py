from setuptools import setup, find_packages

requires = ['PyYAML>=5.3.1']

with open("README.rst", "r", encoding="utf8") as f:
    readme = f.read()

setup(
    name='simpleitem',
    version='0.0.1',
    package_dir={'simpleitem': 'simpleitem'},
    author="Dincer Aslan",
    author_email="dinceraslan.com@gmail.com",
    description="A simple simple item",
    long_description=readme,
    long_description_content_type='text/x-rst',
    url="https://github.com/dinceraslancom/simpleitem",
    project_urls={
        'Source': 'https://github.com/dinceraslancom/simpleitem',
    },
    install_requires=requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.0",
)
