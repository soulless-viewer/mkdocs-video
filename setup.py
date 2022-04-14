from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

setup(
    name="mkdocs-video",
    version="1.3.0",
    author="Mikalai Lisitsa",
    author_email="mikalai.lisitsa@gmail.com",
    url="https://github.com/soulless-viewer/mkdocs-video",
    description="",
    long_description=readme,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(),
    install_requires=[
        "mkdocs>=1.1.0,<2"
    ],
    include_package_data=True,
    python_requires='>=3.6',
    entry_points={
        'mkdocs.plugins': [
            'mkdocs-video = mkdocs_video.plugin:Plugin',
        ]
    }

)
