import requests
from bs4 import BeautifulSoup

# 1. Спрашиваем адрес сайта
url = input("Введи ссылку на сайт (с https://): ")

# 2. ПРОФЕССИОНАЛЬНЫЙ ВОПРОС: спрашиваем, что именно нужно собрать
print("\n--- НАСТРОЙКА ПАРСИНГА ---")
print("1 - Собрать только текстовые заголовки")
print("2 - Собрать только интернет-ссылки")
print("3 - Собрать вообще ВСЁ")
choice = input("Выбери режим (введи цифру 1, 2 или 3): ")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

print("\nПодключаюсь к сайту...")
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 3. Открываем файл для записи результата
with open("smart_result.txt", mode="w", encoding="utf-8") as file:
    # ЕСЛИ ВЫБРАЛИ ЗАГЛОВКИ ИЛИ ВСЁ
    if choice == "1" or choice == "3":
        headlines = soup.find_all(["h1", "h2", "h3"])
        file.write("=== НАЙДЕННЫЕ ЗАГЛОВКИ ===\n")
        for tag in headlines:
            text = tag.text.strip()
            if text:
                file.write(f"[{tag.name}] {text}\n")

    # ЕСЛИ ВЫБРАЛИ ССЫЛКИ ИЛИ ВСЁ
    if choice == "2" or choice == "3":
        links = soup.find_all("a")
        file.write("\n=== НАЙДЕННЫЕ ССЫЛКИ ===\n")
        for link in links:
            href = link.get("href")
            text = link.text.strip() or "[Нет текста]"
            if href and not str(href).startswith("#"):
                file.write(f"{text} -> {href}\n")

print("\n Готово! Проверь файл 'smart_result.txt' в PyCharm.")
