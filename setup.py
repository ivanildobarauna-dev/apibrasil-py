from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    readme = fh.read()

setup(
    name='apigratis-sdk-python',
    version='1.1.7',
    author='APIBRASIL',
    author_email='contato@apibrasil.com.br',
    description=u'Transforme seus projetos em soluções inteligentes com nossa API...',
    long_description_content_type="text/markdown",
    url='https://github.com/APIBrasil/apigratis-sdk-python',
    packages=find_packages(),
    license='MIT License',
    python_requires='>=3.2',
    long_description=readme,
    keywords='whatsapp api, apibrasil, cnpj, sms, cep, consulta, api, brasil, gratis, free, whatsapp, apiwhatsapp, apigratis, apifree',
    install_requires=['requests'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
