# Парсер книг с сайта tululu.org

Этот код сделан для для получения данных из книг с сайта https://tululu.org, а также скачивания книг и изображений 

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Аргументы

Есть два способа запуска программы: базовый, при котором используются базовые значения от 1 до 10.

И с аргументами `--start_id 4` (ваше значение) и `--end_id 23` (ваше значение), при котором вы можете сами выбрать, с какой по какую книгу получать информацию.
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).