from setuptools import setup , find_packages , Extension

setup(
    name='myspkmeanssp' ,
    version='0.1.0' ,
    author= "AvivDori" ,
    
    author_email="doripardess@mail.tau.ac.il" ,
    description= "spkmeans C - api" ,
    install_requires= ['invoke'] , 
    packages= find_packages(where = '.', exclude=()) ,
    license= 'GPL-2' , 
    classifiers= [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)' , 
        'Natural Language :: English' ,
        'Programming Language :: Python :: 3 :: Only' , 
    ] ,
    ext_modules= [
        Extension(
            'myspkmeanssp' ,
            ['spkmeansmodule.c' , 'spkmeans.c'] ,
        ) ,
    ]
)