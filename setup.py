from setuptools import setup
import platform

# Install comtypes if installing on windows
install_requires = ['comtypes; platform_system == "Windows"']

setup(name='tts',
      version='0.01',
      description='A simple TTS wrapper',
      url='http://github.com/DeepHorizons/tts',
      author='Joshua Milas',
      author_email='josh.milas@gmail.com',
      license='MIT',
      packages=['tts'],
      install_requires=install_requires,
      zip_safe=False,
)
