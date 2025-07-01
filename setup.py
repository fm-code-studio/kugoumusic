from setuptools import setup, find_packages

setup(
    name="kugoumusic",
    version="0.1.0",
    author="fm-studio",
    description="酷狗音乐调用",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['pyautogui'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)