# MH-bot [![Python application](https://github.com/MomHackers/MH-bot/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/MomHackers/MH-bot/actions/workflows/python-app.yml)

Бот с /пуп ами, упоминанием Sublime - редактора кода, и многим другим.

## Using VKBottle <img alt="GitHub Workflow Status" src="https://img.shields.io/github/workflow/status/timoniq/vkbottle/CI?style=flat-square"> <img alt="PyPI" src="https://img.shields.io/pypi/v/vkbottle?color=green&label=PyPI&style=flat-square">


# Зависимости:

```shell
pip install -r requirements.txt
```

# Получение токена: 
Заходим в группу ВК -> Управление -> раздел Настройки -> Работа с API
Здесь нужно получить свой токен. Создать ключ, указываем права доступа.

#### Куда этот токен вставлять?
Токен хранится в переменной окружения под названием `vk_token`


- **Сложный способ:**
В консоли прописываем `export vk_token=<ваш токен>` 

- **Легкий способ:**
В пайчарме в конфигурации запуска (Run/Debug Configurations) указываем Environment variables:
![image](https://user-images.githubusercontent.com/48297437/124184824-cba48700-dac2-11eb-9611-d5ace99862f5.png)
Тык справа: ![image](https://user-images.githubusercontent.com/48297437/124184926-eecf3680-dac2-11eb-9e59-d5f6bf676ecb.png)

