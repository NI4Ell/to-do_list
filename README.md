# To-Do List

## Описание проекта
To-Do List — это приложение для управления задачами, написанное на языке Python. Оно позволяет пользователям создавать, редактировать и удалять задачи, а также отмечать их как выполненные.

## Установка
Для установки проекта выполните следующие шаги:

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/NI4Ell/to-do_list.git
    ```

2. Перейдите в директорию проекта:
    ```bash
    cd to-do_list
    ```

3. Установите необходимые зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## Использование
Для запуска приложения выполните следующую команду:

```bash
uvicorn src.main:app --reload
```

### Основные функции
- **Создание задачи**: Позволяет создавать новые задачи и добавлять их в список.
- **Редактирование задачи**: Возможность редактировать существующие задачи.
- **Удаление задачи**: Удаление задачи из списка.
- **Отметка выполнения задачи**: Отметка задачи как выполненной.
