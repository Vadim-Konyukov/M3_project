from setuptools import setup, find_packages

setup(
    name="m3_project",  # Имя вашего пакета
    version="0.1.0",  # Версия вашего пакета
    author="Vadim Konyukov",  # Ваше имя
    author_email="vfdimka375@gmail.com", # Ваш email
    description="Проект, основанный на модулях m3-core и Objectpack",  # Краткое описание
    long_description=open("README.md").read(),  # Описание из README.md
    long_description_content_type="text/markdown",
    url="https://github.com/Vadim-Konyukov/m3_project.git",  # URL репозитория или проекта
    packages=find_packages(),  # Автоматический поиск и включение всех пакетов
    install_requires=[
        "django==2.2.2",
        "m3-django-compat==1.9.2",
        "m3-objectpack==2.2.47",
    ]