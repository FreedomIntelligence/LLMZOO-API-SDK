from setuptools import setup

setup(
    name='llmzoo',
    version='0.1.8',    
    description='A example Python package',
    url='https://github.com/FreedomIntelligence/LLMZOO-API-SDK',
    author='Benyou Wang',
    author_email='wangbenyou@cuhk.edu.cn',
    license='BSD 2-clause',
    packages=['llmzoo'],
    package_data = { '': ['ip.config']},
    zip_safe=False,
    include_package_data=True,
    install_requires=[
                        # 'mpi4py>=2.0',
                      'requests',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
