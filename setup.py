from distutils.core import setup


setup(
    name="duckytie",
    packages=["duckytie"],
    version="0.1",
    license="MIT",  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description="Make your program read texts aloud with our say() function.",
    author="Fabricio Brasil",                   # Type in your name
    author_email="fabriciusbr@gmail.com",      # Type in your E-Mail
    url="https://github.com/fabricius1/duckytie",
    #   download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
    keywords=["text", "audio", "converter", "say", "function",
              "duckytie", "module"],
    install_requires=[
        "gtts",
        "pygame",
        "pydub",
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Development Status :: 3 - Alpha",
        # Define that your audience are developers
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",   # Again, pick a license
        # Specify which pyhton versions that you want to support
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
