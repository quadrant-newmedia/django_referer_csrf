import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django_referer_csrf",
    version="0.0.0",
    author="Alex Fischer",
    author_email="alex@quadrant.net",
    description="TODO",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="TODO - github repo",
    packages=['django_referer_csrf', 'django_referer_csrf.tests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["Django>=2.2,<3.1"],
)