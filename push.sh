# Инициализация папки OneRequests 
# для создания путого репозитория [local]
git init

# Добавление файлов в репозиторий [local]
git add .

# Создание коммита с сообщением OneRequests [local]
git commit -m "Мы дописали проект OneRequests"

# Подключаем нашу папку OneRequests к репозитории [local & global]
git remote add origin git@github.com:Zhanarys11/Parsing.git

# Создание ветки для репозитория OneRequests [local]
# git checkout -b zhanarys

# Отправка в репозиторию OneRequests [global]
git push -u origin master