# import setuptools

# with open("README.md", "r", encoding="utf-8") as f:
#     long_description=f.read()

# __version__="0.0.0"

# REPO_NAME = "Text-Summarizer-project"
# AUTHOR_USER_NAME = "sidd9981"
# SRC_REPO= "textSummerizer"
# AUTHOR_EMAIL="sidd.thir@gmail.com"

# setuptools.setup(
#     name=SRC_REPO,
#     version=__version__,
#     author=AUTHOR_USER_NAME,
#     author_email=AUTHOR_EMAIL,
#     description="A small python package for NLP app",
#     Long_description=long_description,
#     Long_description_content="text/markdown",
#     url=f"https:github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
#     project_urls={
#         "Bug_Tracker": f"https:github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
#     },
#     package_dir={"":"src"},
#     packages=setuptools.find_packages(where=src)
# )

from setuptools import setup, find_packages

setup(
    name="your_project_name",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
)
