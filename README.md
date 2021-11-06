# test-task-fastapi
## General info
Данный проект создан в качестве тестового задания, с самим заданием можно ознакомиться [тут](https://disk.yandex.ru/d/VrqJcKmbPajQcg)

## Demonstration
[test-task-fastapi](https://test-task-fastapi.herokuapp.com/)

## How to run
Как запустить проект:
- Step 1: Убедитесь в том, что у вас установлен [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

- Step 2: Перейдите в папку, куда хотите склонировать репозиторий и введите в терминале команду: `git clone https://github.com/CookIsGood/test-task-fastapi.git`

- Step 3: Перейдите в папку с проектом введя в терминале команду `cd test-task-fastapi`, а также убедитесь в том, что у вас установлены [Python 3.8](https://www.python.org/downloads/) и [PostgreSQL](https://www.postgresql.org/download/)

- Step 4: Создайте виртуальное окружение и введите в терминале команду `pip install -r requirements.txt` для того, чтобы установить зависимости

- Step 5: Создайте следующие переменные окружения:
	- `TTF_DATABASE_URL` - Url подключения к PostgreSQL, например: postgresql://postgres:12345@localhost/tested-base-fastapi

- Step 6: Запустите проект с помощью команды в терминале `python start.py`
	
Как запустить проект с помощью docker:
- Step 1: Убедитесь в том, что у вас установлен [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

- Step 2: Перейдите в папку, куда хотите склонировать репозиторий и введите команду в терминале: `git clone https://github.com/CookIsGood/test-task-fastapi.git`

- Step 3: Перейдите в папку с проектом введя в терминале команду `cd test-task-fastapi`, а также убедитесь в том, что у вас установлен [docker](https://docs.docker.com/engine/install/) и [docker-compose](https://docs.docker.com/compose/install/)

- Step 4: Введите в терминале следующую команду: `docker-compose up --build test-task-fastapi`