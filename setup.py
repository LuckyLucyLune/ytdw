from setuptools import setup, find_packages

setup(
    name='cut_video',
    version='1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='Download and cut a YouTube video to a specific time range',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cut_video = cut_video:main'
        ]
    },
    install_requires=[
        'pytube',
        'moviepy'
    ]
)
