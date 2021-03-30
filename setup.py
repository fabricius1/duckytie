from distutils.core import setup


setup(
    name="duckytie",
    packages=["duckytie"],
    version="0.2.5",
    license="MIT",
    description="Make your program read texts aloud with our say() function.",
    author="Fabricio Brasil",
    author_email="fabriciusbr@gmail.com",
    url="https://github.com/fabricius1/duckytie",
    download_url="https://github.com/fabricius1/duckytie/archive/refs/tags/v_0.2.5.tar.gz",
    keywords=["text", "audio", "converter", "say", "function",
              "duckytie", "module"],
    install_requires=[
        "gtts",
        "pygame",
        "pydub",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
