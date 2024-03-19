from time import sleep
from typing import Iterable
from requests import request as http_request
from requests.exceptions import ConnectionError
from yandex_metrika_logs_api.exceptions import YandexMetrikaConfigError, YandexMetrikaApiError, YandexMetrikaClientError


class YandexMetrika:
    def __init__(self, app_token: str, **kwargs) -> None:
        self.__app_token = app_token
        self._api_endpoint = 'https://api-metrika.yandex.net/management/v1/counter/{counter_id}'
        self._request_latency = kwargs.get('request_latency', 10)  # Базовая задержка между запросами API
        self.counter_id = kwargs.get('counter_id', None)

    def _make_request(self, http_method: str, url: str, params: dict, headers: dict):
        """
        Общая функция отправки запросов к API.
        :param http_method: Метод запроса.
        :param url: Конечная точка запроса.
        :param params: Параметры запросы.
        :param headers: Заголовки запроса.
        :return:
        """
        # Параметры для регулирования скорости выполнения повторных запросов на скачивание файла.
        retry_count = 0

        headers.update({
            'Authorization': f'OAuth {self.__app_token}',
            'Content-Type': 'application/x-yametrika+json'
        })

        while True:
            try:
                response = http_request(http_method, url=url, params=params, headers=headers)
                # Принудительная обработка ответа в кодировке UTF-8
                response.encoding = 'utf-8'

                if response.status_code == 200:
                    return response
                elif response.status_code in (201, 202):
                    # Увеличение задержки с каждой неудачной попыткой
                    retry_count += 1
                    latency_time = self._request_latency * 2 ** retry_count
                    sleep(latency_time)
                    if latency_time >= 1200:
                        # Сбрасываем счётчик, если время ожидания больше 20 минут
                        retry_count = 0
                else:
                    raise YandexMetrikaApiError(response.text)
            except ConnectionError:
                raise YandexMetrikaClientError(ConnectionError)

    def log_evaluate(self, date_from: str, date_to: str, fields: Iterable[str], source: str, counter_id: str = None):
        """
        Оценивает возможность создания запроса логов по его примерному размеру.
        :param date_from: Первый день периода в формате YYYY-MM-DD.
        :param date_to: Последний день периода в формате YYYY-MM-DD.
        :param fields: Список полей.
        :param source: Источник логов: hits/visits.
        :param [Optional] counter_id: Идентификатор счётчика Яндекс.Метрики.
        :return:
        """
        metrika_id = counter_id or self.counter_id
        if metrika_id is None:
            raise YandexMetrikaConfigError('Не указан идентификатор счётчика Яндекс.Метрики.')

        url = '/'.join((self._api_endpoint.format(counter_id=metrika_id), 'logrequests', 'evaluate'))
        params = {
            'date1': date_from,
            'date2': date_to,
            'fields': ','.join(fields),
            'source': source
        }
        headers = {}

        response = self._make_request('GET', url, params, headers)
        return response.json()

    def log_request(self, date_from: str, date_to: str, fields: Iterable[str], source: str, counter_id: str = None):
        """
        Создаёт запрос логов.
        :param date_from: Первый день периода в формате YYYY-MM-DD.
        :param date_to: Последний день периода в формате YYYY-MM-DD.
        :param fields: Список полей.
        :param source: Источник логов: hits/visits.
        :param [Optional] counter_id: Идентификатор счётчика Яндекс.Метрики.
        :return:
        """
        metrika_id = counter_id or self.counter_id
        if metrika_id is None:
            raise YandexMetrikaConfigError('Не указан идентификатор счётчика Яндекс.Метрики.')

        url = '/'.join((self._api_endpoint.format(counter_id=metrika_id), 'logrequests'))
        params = {
            'date1': date_from,
            'date2': date_to,
            'fields': ','.join(fields),
            'source': source
        }
        headers = {}

        response = self._make_request('POST', url, params, headers)
        return response.json()

    def log_status(self, request_id: str, counter_id: str = None):
        """
        Возвращает информацию о запросе логов.
        :param request_id: Идентификатор запроса логов.
        :param [Optional] counter_id: Идентификатор счётчика Яндекс.Метрики.
        :return:
        """
        metrika_id = counter_id or self.counter_id
        if metrika_id is None:
            raise YandexMetrikaConfigError('Не указан идентификатор счётчика Яндекс.Метрики.')

        url = '/'.join((self._api_endpoint.format(counter_id=metrika_id), 'logrequest', request_id))
        params = {}
        headers = {}

        response = self._make_request('GET', url, params, headers)
        return response.json()

    def log_download(self, request_id: str, part_number: int, counter_id: str = None):
        """
        Загружает часть подготовленных логов обработанного запроса.
        :param request_id: Идентификатор запроса логов.
        :param part_number: Номер части подготовленных логов обработанного запроса.
        :param [Optional] counter_id: Идентификатор счётчика Яндекс.Метрики.
        :return:
        """
        metrika_id = counter_id or self.counter_id
        if metrika_id is None:
            raise YandexMetrikaConfigError('Не указан идентификатор счётчика Яндекс.Метрики.')

        url = '/'.join((
            self._api_endpoint.format(counter_id=metrika_id),
            'logrequest', request_id, 'part', str(part_number), 'download'
        ))
        params = {}
        headers = {}

        response = self._make_request('GET', url, params, headers)
        return response.text

    def log_clean(self, request_id: str, counter_id: str = None):
        """
        Очищает подготовленные для загрузки логи обработанного запроса.
        :param request_id: Идентификатор запроса логов.
        :param [Optional] counter_id: Идентификатор счётчика Яндекс.Метрики.
        :return:
        """
        metrika_id = counter_id or self.counter_id
        if metrika_id is None:
            raise YandexMetrikaConfigError('Не указан идентификатор счётчика Яндекс.Метрики.')

        url = '/'.join((self._api_endpoint.format(counter_id=metrika_id), 'logrequest', request_id, 'clean'))
        params = {}
        headers = {}

        response = self._make_request('POST', url, params, headers)
        return response.json()

    def log_cancel(self, request_id: str, counter_id: str = None):
        """
        Отменяет ещё не обработанный запрос логов.
        :param request_id: Идентификатор запроса логов.
        :param [Optional] counter_id: Идентификатор счётчика Яндекс.Метрики.
        :return:
        """
        metrika_id = counter_id or self.counter_id
        if metrika_id is None:
            raise YandexMetrikaConfigError('Не указан идентификатор счётчика Яндекс.Метрики.')

        url = '/'.join((self._api_endpoint.format(counter_id=metrika_id), 'logrequest', request_id, 'cancel'))
        params = {}
        headers = {}

        response = self._make_request('POST', url, params, headers)
        return response.json()
