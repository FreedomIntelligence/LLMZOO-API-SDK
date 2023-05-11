from setuptools import setup

setup(
    name='llmzoo',
    version='0.1.5',    
    description='A example Python package',
    url='https://github.com/FreedomIntelligence/LLMZOO-API-SDK',
    author='Benyou Wang',
    author_email='wangbenyou@cuhk.edu.cn',
    license='BSD 2-clause',
    packages=['llmzoo'],
    data_files = [("config", ["config/ip.config"])],
    package_data = {'llmzoo': ['config/ip.config']}
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