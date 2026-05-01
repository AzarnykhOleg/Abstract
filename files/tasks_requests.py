import requests


# Задание 1: Загрузка изображения
def download_image(image_url, save_path):
    """Скачивает изображение по URL и сохраняет на диск."""
    try:
        # Отправляем GET-запрос с проверкой SSL (verify=True по умолчанию)
        response = requests.get(image_url, verify=True, timeout=10)

        # Проверяем статус ответа (вызывает исключение при 4xx/5xx)
        response.raise_for_status()

        # Проверяем финальный URL после возможных редиректов
        print(f"Финальный URL после редиректов: {response.url}")

        # Сохраняем бинарное содержимое (.content для файлов)
        with open(save_path, 'wb') as file:
            file.write(response.content)

        print(f"Изображение успешно сохранено: {save_path}")
        print(f"Размер файла: {len(response.content)} байт")

    except requests.exceptions.HTTPError as e:
        # Обработка ошибок 4xx и 5xx
        print(f"Ошибка сервера: {e}")
        print(f"Статус код: {response.status_code}")
    except requests.exceptions.RequestException as e:
        # Обработка сетевых ошибок (DNS, таймаут, SSL и т.д.)
        print(f"Ошибка при выполнении запроса: {e}")


# Задание 2: Получение факта о кошках
def get_cat_fact():
    """Получает случайный факт о кошках с API."""
    api_url = "https://catfact.ninja/fact"

    try:
        response = requests.get(api_url, verify=True, timeout=10)
        response.raise_for_status()

        # Преобразуем JSON-ответ в словарь Python
        data = response.json()

        # Извлекаем текст факта
        fact_text = data.get('fact', 'Факт не найден в ответе')
        print(f"\nФакт о кошках: {fact_text}")
        print(f"Длина факта: {data.get('length', 'N/A')} символов")

    except requests.exceptions.HTTPError as e:
        print(f"Ошибка HTTP при получении факта: {e}")
    except requests.exceptions.JSONDecodeError:
        print("Ошибка: сервер вернул некорректный JSON")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка сети: {e}")


# === Запуск программы ===
if __name__ == "__main__":
    # Пример 1: Корректный URL изображения PNG (Wikimedia Commons)
    image_url = "https://img.freepik.com/free-photo/cute-kitten-sitting-looking-camera-surrounded-by-flowers-generated-by-artificial-intelligence_25030-66192.jpg?semt=ais_hybrid"

    print("=== Задание 1: Загрузка изображения ===")
    download_image(image_url, "cat_image.png")

    # Пример 2: Получение факта о кошках
    print("\n=== Задание 2: Факт о кошках ===")
    get_cat_fact()

    # Тест с некорректным URL (ошибка 404)
    print("\n=== Тест обработки ошибок ===")
    print("Пытаемся скачать с несуществующего URL (должна быть ошибка 404)...")
    download_image("https://httpbin.org/status/404", "error_test.png")