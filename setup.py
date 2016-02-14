from setuptools import setup

install_requires = []
if platform.system() == 'Windows':
    install_requires += [
        'comtypes',
    ]
   
setup(name='tts',
      version='0.01',
      description='A simple TTS wrapper',
      url='http://github.com/DeepHorizons/tts',
      author='Joshua Milas',
      author_email='josh.milas@gmail.com',
      license='MIT',
      packages=['tts'],
      install_requires=install_requires,
      zip_safe=False)
