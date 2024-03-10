from setuptools import setup, find_packages

# Ler descrição longa do README.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Ler requisitos do requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="nome_do_pacote",  # Substitua pelo nome real do seu pacote
    version="0.0.1",  # Atualize a versão conforme você desenvolve
    author="Seu Nome Completo",  # Substitua pelo seu nome completo
    author_email="seu_email@exemplo.com",  # Substitua pelo seu email
    description="Uma curta descrição do seu pacote Python para processamento de imagens.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seu_usuario/seu_repositório_github",  # Substitua pelo seu link real
    packages=find_packages(exclude=["tests*"]),  # Excluir diretórios de teste
    install_requires=requirements,
    python_requires=">=3.8",  # Atualize se seu pacote requer uma versão diferente do Python
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)