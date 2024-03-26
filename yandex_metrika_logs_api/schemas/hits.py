from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional


def fill_clickhouse_schema(field_type: str):
    return {
        'field_type': field_type
    }


class _FK(BaseModel):
    """
    Общие поля для просмотров.
    """
    counter_id: Optional[int] = Field(
        default=None,
        alias='ym:pv:counterID',
        description='Номер счётчика.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt32')
        }
    )
    watch_id: Optional[int] = Field(
        default=None,
        alias='ym:pv:watchID',
        description='Идентификатор просмотра.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt64')
        }
    )
    watch_datetime: Optional[datetime] = Field(
        default=None,
        alias='ym:pv:dateTime',
        description='Дата и время события (в часовом поясе счётчика).',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('DateTime')
        }
    )


class PageViewSchema(_FK):
    """
    Основная информация о просмотре страницы.
    """
    watch_date: Optional[date] = Field(
        default=None,
        alias='ym:pv:date',
        description='Дата события.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('Date')
        }
    )
    title: Optional[str] = Field(
        default=None,
        alias='ym:pv:title',
        description='Заголовок страницы.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    url: Optional[str] = Field(
        default=None,
        alias='ym:pv:URL',
        description='Адрес страницы.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    referer: Optional[str] = Field(
        default=None,
        alias='ym:pv:referer',
        description='Реферер.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    is_page_view: Optional[int] = Field(
        default=None,
        alias='ym:pv:isPageView',
        description='Просмотр страницы. Принимает значение 0, если хит не нужно учитывать как просмотр.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt8')
        }
    )
    is_turbo_page: Optional[int] = Field(
        default=None,
        alias='ym:pv:isTurboPage',
        description='Просмотр совершён с Турбо-страницы. Возможные значения: 1 — да, 0 — нет.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt8')
        }
    )
    is_turbo_app: Optional[int] = Field(
        default=None,
        alias='ym:pv:isTurboApp',
        description='Просмотр совершён с Турбо-сервиса. Возможные значения: 1 — да, 0 — нет.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt8')
        }
    )


class PVParamsSchema(_FK):
    """Параметры просмотра страницы."""
    parsed_params_key1: Optional[list] = Field(
        default=None,
        alias='ym:pv:parsedParamsKey1',
        description='Параметры просмотра, ур. 1.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('Array(String)')
        }
    )
    parsed_params_key2: Optional[list] = Field(
        default=None,
        alias='ym:pv:parsedParamsKey2',
        description='Параметры просмотра, ур. 2.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('Array(String)')
        }
    )
    parsed_params_key3: Optional[list] = Field(
        default=None,
        alias='ym:pv:parsedParamsKey3',
        description='Параметры просмотра, ур. 3.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('Array(String)')
        }
    )
    parsed_params_key4: Optional[list] = Field(
        default=None,
        alias='ym:pv:parsedParamsKey4',
        description='Параметры просмотра, ур. 4.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('Array(String)')
        }
    )
    parsed_params_key5: Optional[list] = Field(
        default=None,
        alias='ym:pv:parsedParamsKey5',
        description='Параметры просмотра, ур. 5.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('Array(String)')
        }
    )
    parsed_params_key6: Optional[list] = Field(
        default=None,
        alias='ym:pv:parsedParamsKey6',
        description='Параметры просмотра, ур. 6.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('Array(String)')
        }
    )
    parsed_params_key7: Optional[list] = Field(
        default=None,
        alias='ym:pv:parsedParamsKey7',
        description='Параметры просмотра, ур. 7.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('Array(String)')
        }
    )
    parsed_params_key8: Optional[list] = Field(
        default=None,
        alias='ym:pv:parsedParamsKey8',
        description='Параметры просмотра, ур. 8.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('Array(String)')
        }
    )
    parsed_params_key9: Optional[list] = Field(
        default=None,
        alias='ym:pv:parsedParamsKey9',
        description='Параметры просмотра, ур. 9.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('Array(String)')
        }
    )
    parsed_params_key10: Optional[list] = Field(
        default=None,
        alias='ym:pv:parsedParamsKey10',
        description='Параметры просмотра, ур. 10.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('Array(String)')
        }
    )


class PVUTMSchema(_FK):
    """UTM-метки."""
    utm_campaign: Optional[str] = Field(
        default=None,
        alias='ym:pv:UTMCampaign',
        description='UTM Campaign.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    utm_source: Optional[str] = Field(
        default=None,
        alias='ym:pv:UTMSource',
        description='UTM Source.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    utm_medium: Optional[str] = Field(
        default=None,
        alias='ym:pv:UTMMedium',
        description='UTM Medium.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    utm_term: Optional[str] = Field(
        default=None,
        alias='ym:pv:UTMTerm',
        description='UTM Term.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    utm_content: Optional[str] = Field(
        default=None,
        alias='ym:pv:UTMContent',
        description='UTM Content.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )


class PVTrafficSourceSchema(_FK):
    """Источники трафика."""
    last_traffic_source: Optional[str] = Field(
        default=None,
        alias='ym:pv:lastTrafficSource',
        description='Источник трафика.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    last_search_engine: Optional[str] = Field(
        default=None,
        alias='ym:pv:lastSearchEngine',
        description='Поисковая система (детально).',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    last_search_engine_root: Optional[str] = Field(
        default=None,
        alias='ym:pv:lastSearchEngineRoot',
        description='Поисковая система.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    last_adv_engine: Optional[str] = Field(
        default=None,
        alias='ym:pv:lastAdvEngine',
        description='Рекламная система.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    last_social_network: Optional[str] = Field(
        default=None,
        alias='ym:pv:lastSocialNetwork',
        description='Социальная сеть.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    last_social_network_profile: Optional[str] = Field(
        default=None,
        alias='ym:pv:lastSocialNetworkProfile',
        description='Страница социальной сети, с которой был переход.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    recommendation_system: Optional[str] = Field(
        default=None,
        alias='ym:pv:recommendationSystem',
        description='Переход из рекомендательных систем.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    messenger: Optional[str] = Field(
        default=None,
        alias='ym:pv:messenger',
        description='Переход из мессенджера.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )


class PVAdvSchema(_FK):
    """Рекламные и маркетинговые данные."""
    from_mark: Optional[str] = Field(
        default=None,
        alias='ym:pv:from',
        description='Метка from.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    has_gclid: Optional[int] = Field(
        default=None,
        alias='ym:pv:hasGCLID',
        description='Наличие GCLID.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt8')
        }
    )
    gclid: Optional[str] = Field(
        default=None,
        alias='ym:pv:GCLID',
        description='GCLID.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    openstat_ad: Optional[str] = Field(
        default=None,
        alias='ym:pv:openstatAd',
        description='Openstat Ad.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    openstat_campaign: Optional[str] = Field(
        default=None,
        alias='ym:pv:openstatCampaign',
        description='Openstat Campaign.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    openstat_service: Optional[str] = Field(
        default=None,
        alias='ym:pv:openstatService',
        description='Openstat Service.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    openstat_source: Optional[str] = Field(
        default=None,
        alias='ym:pv:openstatSource',
        description='Openstat Source.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )


class PVBrowserDeviceSchema(_FK):
    """Информация о браузере и устройстве."""
    browser: Optional[str] = Field(
        default=None,
        alias='ym:pv:browser',
        description='Браузер.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    browser_major_version: Optional[int] = Field(
        default=None,
        alias='ym:pv:browserMajorVersion',
        description='Major-версия браузера.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt16')
        }
    )
    browser_minor_version: Optional[int] = Field(
        default=None,
        alias='ym:pv:browserMinorVersion',
        description='Minor-версия браузера.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt16')
        }
    )
    browser_country: Optional[str] = Field(
        default=None,
        alias='ym:pv:browserCountry',
        description='Страна браузера.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    browser_language: Optional[str] = Field(
        default=None,
        alias='ym:pv:browserLanguage',
        description='Язык браузера.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    browser_engine: Optional[str] = Field(
        default=None,
        alias='ym:pv:browserEngine',
        description='Движок браузера.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    browser_engine_major_version: Optional[int] = Field(
        default=None,
        alias='ym:pv:browserEngineVersion1',
        description='Major-версия движка браузера.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt16')
        }
    )
    browser_engine_minor_version: Optional[int] = Field(
        default=None,
        alias='ym:pv:browserEngineVersion2',
        description='Minor-версия движка браузера.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt16')
        }
    )
    browser_engine_build_version: Optional[int] = Field(
        default=None,
        alias='ym:pv:browserEngineVersion3',
        description='Build-версия движка браузера.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt16')
        }
    )
    browser_engine_revision_version: Optional[int] = Field(
        default=None,
        alias='ym:pv:browserEngineVersion4',
        description='Revision-версия движка браузера.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt16')
        }
    )
    client_timezone: Optional[int] = Field(
        default=None,
        alias='ym:pv:clientTimeZone',
        description='Разница между часовым поясом пользователя и UTC (в минутах).',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt16')
        }
    )
    client_id: Optional[int] = Field(
        default=None,
        alias='ym:pv:clientID',
        description='Анонимный идентификатор пользователя в браузере (first-party cookies).',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt64')
        }
    )
    counter_user_id_hash: Optional[int] = Field(
        default=None,
        alias='ym:pv:counterUserIDHash',
        description='Идентификатор посетителя (в рамках одного браузера), с помощью которого производится подсчёт '
                    'уникальных посетителей сайта в интерфейсе Метрики.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt64')
        }
    )
    cookie_enabled: Optional[int] = Field(
        default=None,
        alias='ym:pv:cookieEnabled',
        description='Наличие Cookie.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt8')
        }
    )
    javascript_enabled: Optional[int] = Field(
        default=None,
        alias='ym:pv:javascriptEnabled',
        description='Наличие JavaScript.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt8')
        }
    )
    device_category: Optional[str] = Field(
        default=None,
        alias='ym:pv:deviceCategory',
        description='Тип устройства. Возможные значения: 1 — десктоп, 2 — мобильные телефоны, 3 — планшеты, 4 — TV.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    mobile_phone: Optional[str] = Field(
        default=None,
        alias='ym:pv:mobilePhone',
        description='Производитель устройства.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    mobile_phone_model: Optional[str] = Field(
        default=None,
        alias='ym:pv:mobilePhoneModel',
        description='Модель устройства.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    operating_system: Optional[str] = Field(
        default=None,
        alias='ym:pv:operatingSystem',
        description='Операционная система (детально).',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    operating_system_root: Optional[str] = Field(
        default=None,
        alias='ym:pv:operatingSystemRoot',
        description='Группа операционных систем.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    physical_screen_height: Optional[int] = Field(
        default=None,
        alias='ym:pv:physicalScreenHeight',
        description='Физическая высота.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt16')
        }
    )
    physical_screen_width: Optional[int] = Field(
        default=None,
        alias='ym:pv:physicalScreenWidth',
        description='Физическая ширина.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt16')
        }
    )
    screen_colors: Optional[int] = Field(
        default=None,
        alias='ym:pv:screenColors',
        description='Глубина цвета.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt8')
        }
    )
    screen_format: Optional[str] = Field(
        default=None,
        alias='ym:pv:screenFormat',
        description='Соотношение сторон.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    screen_height: Optional[int] = Field(
        default=None,
        alias='ym:pv:screenHeight',
        description='Логическая высота.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt16')
        }
    )
    screen_width: Optional[int] = Field(
        default=None,
        alias='ym:pv:screenWidth',
        description='Логическая ширина.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt16')
        }
    )
    screen_orientation: Optional[str] = Field(
        default=None,
        alias='ym:pv:screenOrientation',
        description='Ориентация экрана.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    window_client_height: Optional[int] = Field(
        default=None,
        alias='ym:pv:windowClientHeight',
        description='Высота окна.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt16')
        }
    )
    window_client_width: Optional[int] = Field(
        default=None,
        alias='ym:pv:windowClientWidth',
        description='Ширина окна.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt16')
        }
    )
    network_type: Optional[str] = Field(
        default=None,
        alias='ym:pv:networkType',
        description='Тип соединения.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )


class PVGeoSchema(_FK):
    """Географическая информация."""
    region_city: Optional[str] = Field(
        default=None,
        alias='ym:pv:regionCity',
        description='Город (английское название).',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    region_country: Optional[str] = Field(
        default=None,
        alias='ym:pv:regionCountry',
        description='Страна (ISO).',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    region_city_id: Optional[int] = Field(
        default=None,
        alias='ym:pv:regionCityID',
        description='ID города.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt32')
        }
    )
    region_country_id: Optional[int] = Field(
        default=None,
        alias='ym:pv:regionCountryID',
        description='ID страны.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt32')
        }
    )
    ip_address: Optional[str] = Field(
        default=None,
        alias='ym:pv:ipAddress',
        description='IP адрес.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )


class PVBehaviorSchema(_FK):
    """Поведенческие сигналы."""
    artificial: Optional[int] = Field(
        default=None,
        alias='ym:pv:artificial',
        description='Искусственный хит, переданный с помощью функций hit(), event() и пр.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt8')
        }
    )
    page_charset: Optional[str] = Field(
        default=None,
        alias='ym:pv:pageCharset',
        description='Кодировка страницы сайта.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    link: Optional[int] = Field(
        default=None,
        alias='ym:pv:link',
        description='Переход по ссылке.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt8')
        }
    )
    download: Optional[int] = Field(
        default=None,
        alias='ym:pv:download',
        description='Загрузка файла.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt8')
        }
    )
    not_bounce: Optional[int] = Field(
        default=None,
        alias='ym:pv:notBounce',
        description='Специальное событие "неотказ" (для точного показателя отказов).',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt8')
        }
    )
    http_error: Optional[str] = Field(
        default=None,
        alias='ym:pv:httpError',
        description='Код ошибки.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    goals_id: Optional[list] = Field(
        default=None,
        alias='ym:pv:goalsID',
        description='Номера целей, достигнутых в данном просмотре.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('Array(UInt32)')
        }
    )
    share_service: Optional[str] = Field(
        default=None,
        alias='ym:pv:shareService',
        description='Кнопка "Поделиться", имя сервиса.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    share_url: Optional[str] = Field(
        default=None,
        alias='ym:pv:shareURL',
        description='Кнопка "Поделиться", URL.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    share_title: Optional[str] = Field(
        default=None,
        alias='ym:pv:shareTitle',
        description='Кнопка "Поделиться", заголовок страницы.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('String')
        }
    )
    iframe: Optional[int] = Field(
        default=None,
        alias='ym:pv:iFrame',
        description='Просмотр из iframe.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt8')
        }
    )


class HitGlobalSchema(
    PVParamsSchema,
    PVBehaviorSchema,
    PVAdvSchema,
    PVTrafficSourceSchema,
    PVUTMSchema,
    PVGeoSchema,
    PVBrowserDeviceSchema,
    PageViewSchema
):
    """Все поля просмотров."""
    pass
