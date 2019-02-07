import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

    name='movie_organizer',  

    version='1.0',

    scripts=['movie_organizer'] ,

    author="Ahmed Alrifai",

    author_email="ahmed.alrifai.97@gmail.com",

    description="Tool for organizing movies by IMDB rating.",

    long_description=long_description,

    long_description_content_type="text/markdown",

    url="https://github.com/ahmedalrifai/movie-organizer",

    packages=setuptools.find_packages(),

    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],

 )