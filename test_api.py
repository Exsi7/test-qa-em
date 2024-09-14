import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение переменных окружения
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('REPO_NAME')
API_URL = 'https://api.github.com/user/repos'

# Проверка наличия необходимых переменных окружения
if not all([GITHUB_USERNAME, GITHUB_TOKEN, REPO_NAME]):
    raise ValueError('Недостаточно данных для выполнения теста. Убедитесь, что все переменные окружения установлены.')

def create_repo():
    """Создание нового публичного репозитория на GitHub."""
    response = requests.post(
        API_URL,
        json={'name': REPO_NAME, 'private': False},
        auth=(GITHUB_USERNAME, GITHUB_TOKEN)
    )
    response.raise_for_status()
    return response.json()

def check_repo_exists():
    """Проверка наличия репозитория в списке репозиториев пользователя."""
    response = requests.get(
        f'https://api.github.com/user/repos',
        auth=(GITHUB_USERNAME, GITHUB_TOKEN)
    )
    response.raise_for_status()
    repos = response.json()
    return any(repo['name'] == REPO_NAME for repo in repos)

def delete_repo():
    """Удаление репозитория с GitHub."""
    response = requests.delete(
        f'https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}',
        auth=(GITHUB_USERNAME, GITHUB_TOKEN)
    )
    response.raise_for_status()

def test_github_api():
    # Создание репозитория
    print("Создание репозитория...")
    create_repo()
    print("Репозиторий создан.")

    # Проверка наличия репозитория
    print("Проверка наличия репозитория...")
    if check_repo_exists():
        print("Репозиторий найден.")
    else:
        raise AssertionError("Репозиторий не найден.")
    
    # Удаление репозитория
    print("Удаление репозитория...")
    delete_repo()
    print("Репозиторий удален.")

if __name__ == '__main__':
    test_github_api()