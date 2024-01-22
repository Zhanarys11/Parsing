# Инициализация папки OneRequests 
# для создания путого репозитория [local]
git init

# Добавление файлов в репозиторий [local]
git add .

# Создание коммита с сообщением OneRequests [local]
git commit -m "Парсил Kolesa"

# Подключаем нашу папку OneRequests к репозитории [local & global]
git remote add origin git@github.com:BAZAAR-ITC/KalesoKz.git

# Создание ветки для репозитория OneRequests [local]
git checkout -b zhanarys

# Отправка в репозиторию OneRequests [global]
git push -u origin zhanarys