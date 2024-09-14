Установите зависимости: pip install -r requirements.txt

Запустите тест E2E UI: python test_e2e_ui.py

Создайте файл .env в каталоге github_api и укажите свои данные:
GITHUB_USERNAME=your_github_username
GITHUB_TOKEN=your_github_token
REPO_NAME=repo-name

Запуститe тест GitHub Api: python test_api.py