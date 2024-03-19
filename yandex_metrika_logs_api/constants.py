class LogRequestSource(object):
    """Источник логов."""
    HITS = 'hits'  # просмотры
    VISITS = 'visits'  # визиты


class LogRequestStatus(object):
    """Статус запроса."""
    PROCESSED = 'processed'  # обработан
    CANCELED = 'canceled'  # отменён
    PROCESSING_FAILED = 'processing_failed'  # ошибка при обработке
    CREATED = 'created'  # создан
    CLEANED_BY_USER = 'cleaned_by_user'  # очищен пользователем
    CLEANED_AUTOMATICALLY = 'cleaned_automatically_as_too_old'  # очищен автоматически
    AWAITING_RETRY = 'awaiting_retry'  # не удалось выполнить запрос, ожидает автоматического перезапуска


class AttributionModel(object):
    """
    Модели атрибуции.
    https://yandex.ru/support/metrica/reports/attribution-model.html
    """
    # первый источник
    FIRST = 'first'
    # последний источник
    LAST = 'last'
    # последний значимый источник
    LASTSIGN = 'lastsign'
    # последний переход из Директа
    LAST_YANDEX_DIRECT_CLICK = 'last_yandex_direct_click'
    # первый источник с учётом визитов со всех устройств посетителя
    CROSS_DEVICE_FIRST = 'cross_device_first'
    # последний источник с учётом визитов со всех устройств посетителя
    CROSS_DEVICE_LAST = 'cross_device_last'
    # последний значимый источник с учётом визитов со всех устройств посетителя
    CROSS_DEVICE_LAST_SIGNIFICANT = 'cross_device_last_significant'
    # последний переход из Директа с учётом визитов со всех устройств посетителя
    CROSS_DEVICE_LAST_YANDEX_DIRECT_CLICK = 'cross_device_last_yandex_direct_click'
    # автоматическая атрибуция
    AUTOMATIC = 'automatic'
