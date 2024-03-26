from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, List


def fill_clickhouse_schema(field_type: str):
    return {
        'field_type': field_type
    }


class _FK(BaseModel):
    """
    Общие поля для визитов.
    """
    counter_id: Optional[int] = Field(
        default=None,
        alias='ym:s:counterID',
        description='Номер счётчика.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt32')
        }
    )
    visit_id: Optional[int] = Field(
        default=None,
        alias='ym:s:visitID',
        description='Идентификатор визита.',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('UInt64')
        }
    )
    visit_datetime: Optional[datetime] = Field(
        default=None,
        alias='ym:s:dateTime',
        description='Дата и время визита (в часовом поясе счётчика).',
        json_schema_extra={
            'clickhouse_schema': fill_clickhouse_schema('DateTime')
        }
    )


class SessionSchema(_FK):
    """
    Основная информация о визите.
    """
    visit_date: Optional[date] = Field(
        default=None,
        alias='ym:s:date',
        description='Дата визита.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Date')}
    )
    date_time_utc: Optional[datetime] = Field(
        default=None,
        alias='ym:s:dateTimeUTC',
        description='Дата и время события (в часовом поясе UTC+3).',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('DateTime')}
    )
    watch_ids: Optional[List[int]] = Field(
        default=None,
        alias='ym:s:watchIDs',
        description='Просмотры, которые были в данном визите. Ограничение массива — 500 просмотров.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(UInt64)')}
    )
    is_new_user: Optional[int] = Field(
        default=None,
        alias='ym:s:isNewUser',
        description='Первый визит посетителя.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('UInt8')}
    )
    start_url: Optional[str] = Field(
        default=None,
        alias='ym:s:startURL',
        description='Страница входа.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    end_url: Optional[str] = Field(
        default=None,
        alias='ym:s:endURL',
        description='Страница выхода.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    page_views: Optional[int] = Field(
        default=None,
        alias='ym:s:pageViews',
        description='Глубина просмотра (детально).',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Int32')}
    )
    visit_duration: Optional[int] = Field(
        default=None,
        alias='ym:s:visitDuration',
        description='Время на сайте (детально).',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('UInt32')}
    )
    bounce: Optional[int] = Field(
        default=None,
        alias='ym:s:bounce',
        description='Отказность.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('UInt8')}
    )
    referer: Optional[str] = Field(
        default=None,
        alias='ym:s:referer',
        description='Реферер.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    currency_id: Optional[str] = Field(
        default=None,
        alias='ym:s:<attribution>CurrencyID',
        description='Валюта.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )


class SBrowserDeviceSchema(_FK):
    client_id: Optional[int] = Field(
        default=None, alias='ym:s:clientID',
        description='Анонимный идентификатор пользователя в браузере (first-party cookies).',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('UInt64')}
    )
    counter_user_id_hash: Optional[int] = Field(
        default=None, alias='ym:s:counterUserIDHash',
        description='Идентификатор посетителя (в рамках одного браузера), с помощью которого производится подсчёт '
                    'уникальных посетителей сайта в интерфейсе Метрики.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('UInt64')}
    )
    network_type: Optional[str] = Field(
        default=None, alias='ym:s:networkType',
        description='Тип соединения.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    browser_language: Optional[str] = Field(
        default=None, alias='ym:s:browserLanguage',
        description='Язык браузера.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    browser_country: Optional[str] = Field(
        default=None, alias='ym:s:browserCountry',
        description='Страна браузера.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    client_time_zone: Optional[int] = Field(
        default=None, alias='ym:s:clientTimeZone',
        description='Разница между часовым поясом пользователя и UTC (в минутах).',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Int16')}
    )
    device_category: Optional[str] = Field(
        default=None, alias='ym:s:deviceCategory',
        description='Тип устройства. Возможные значения: 1 — десктоп, 2 — мобильные телефоны, 3 — планшеты, 4 — TV.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    mobile_phone: Optional[str] = Field(
        default=None, alias='ym:s:mobilePhone',
        description='Производитель устройства.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    mobile_phone_model: Optional[str] = Field(
        default=None, alias='ym:s:mobilePhoneModel',
        description='Модель устройства.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    operating_system_root: Optional[str] = Field(
        default=None, alias='ym:s:operatingSystemRoot',
        description='Группа операционных систем.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    operating_system: Optional[str] = Field(
        default=None, alias='ym:s:operatingSystem',
        description='Операционная система (детально).',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    browser: Optional[str] = Field(
        default=None, alias='ym:s:browser',
        description='Браузер.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    browser_major_version: Optional[int] = Field(
        default=None, alias='ym:s:browserMajorVersion',
        description='Major-версия браузера.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('UInt16')}
    )
    browser_minor_version: Optional[int] = Field(
        default=None, alias='ym:s:browserMinorVersion',
        description='Minor-версия браузера.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('UInt16')}
    )
    browser_engine: Optional[str] = Field(
        default=None, alias='ym:s:browserEngine',
        description='Движок браузера.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    browser_engine_major_version: Optional[int] = Field(
        default=None, alias='ym:s:browserEngineVersion1',
        description='Major-версия движка браузера.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('UInt16')}
    )
    browser_engine_minor_version: Optional[int] = Field(
        default=None, alias='ym:s:browserEngineVersion2',
        description='Minor-версия движка браузера.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('UInt16')}
    )
    browser_engine_build_version: Optional[int] = Field(
        default=None, alias='ym:s:browserEngineVersion3',
        description='Build-версия движка браузера.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('UInt16')}
    )
    browser_engine_revision_version: Optional[int] = Field(
        default=None, alias='ym:s:browserEngineVersion4',
        description='Revision-версия движка браузера.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('UInt16')}
    )
    cookie_enabled: Optional[int] = Field(
        default=None, alias='ym:s:cookieEnabled',
        description='Наличие Cookie.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('UInt8')}
    )
    javascript_enabled: Optional[int] = Field(
        default=None, alias='ym:s:javascriptEnabled',
        description='Наличие JavaScript.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('UInt8')}
    )
    screen_format: Optional[str] = Field(
        default=None, alias='ym:s:screenFormat',
        description='Соотношение сторон.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    screen_colors: Optional[int] = Field(
        default=None, alias='ym:s:screenColors',
        description='Глубина цвета.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('UInt8')}
    )
    screen_orientation: Optional[str] = Field(
        default=None, alias='ym:s:screenOrientation',
        description='Ориентация экрана.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    screen_width: Optional[int] = Field(
        default=None, alias='ym:s:screenWidth',
        description='Логическая ширина.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('UInt16')}
    )
    screen_height: Optional[int] = Field(
        default=None, alias='ym:s:screenHeight',
        description='Логическая высота.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('UInt16')}
    )
    physical_screen_width: Optional[int] = Field(
        default=None, alias='ym:s:physicalScreenWidth',
        description='Физическая ширина.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('UInt16')}
    )
    physical_screen_height: Optional[int] = Field(
        default=None, alias='ym:s:physicalScreenHeight',
        description='Физическая высота.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('UInt16')}
    )
    window_client_width: Optional[int] = Field(
        default=None, alias='ym:s:windowClientWidth',
        description='Ширина окна.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('UInt16')}
    )
    window_client_height: Optional[int] = Field(
        default=None, alias='ym:s:windowClientHeight',
        description='Высота окна.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('UInt16')}
    )


class SGeoSchema(_FK):
    ip_address: Optional[str] = Field(
        default=None,
        alias='ym:s:ipAddress',
        description='IP адрес.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    region_country: Optional[str] = Field(
        default=None,
        alias='ym:s:regionCountry',
        description='Страна (ISO).',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    region_city: Optional[str] = Field(
        default=None,
        alias='ym:s:regionCity',
        description='Город (английское название).',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    region_country_id: Optional[int] = Field(
        default=None,
        alias='ym:s:regionCountryID',
        description='ID страны.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('UInt32')}
    )
    region_city_id: Optional[int] = Field(
        default=None,
        alias='ym:s:regionCityID',
        description='ID города.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('UInt32')}
    )


class SUTMSchema(_FK):
    utm_campaign: Optional[str] = Field(
        default=None,
        alias='ym:s:<attribution>UTMCampaign',
        description='UTM Campaign.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    utm_content: Optional[str] = Field(
        default=None,
        alias='ym:s:<attribution>UTMContent',
        description='UTM Content.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    utm_medium: Optional[str] = Field(
        default=None,
        alias='ym:s:<attribution>UTMMedium',
        description='UTM Medium.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    utm_source: Optional[str] = Field(
        default=None,
        alias='ym:s:<attribution>UTMSource',
        description='UTM Source.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    utm_term: Optional[str] = Field(
        default=None,
        alias='ym:s:<attribution>UTMTerm',
        description='UTM Term.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )


class STrafficSourceSchema(_FK):
    traffic_source: Optional[str] = Field(
        default=None,
        alias='ym:s:<attribution>TrafficSource',
        description='Источник трафика.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    adv_engine: Optional[str] = Field(
        default=None,
        alias='ym:s:<attribution>AdvEngine',
        description='Рекламная система.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    referral_source: Optional[str] = Field(
        default=None,
        alias='ym:s:<attribution>ReferalSource',
        description='Переход с сайтов.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    search_engine_root: Optional[str] = Field(
        default=None,
        alias='ym:s:<attribution>SearchEngineRoot',
        description='Поисковая система.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    search_engine: Optional[str] = Field(
        default=None,
        alias='ym:s:<attribution>SearchEngine',
        description='Поисковая система (детально).',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    social_network: Optional[str] = Field(
        default=None,
        alias='ym:s:<attribution>SocialNetwork',
        description='Социальная сеть.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    social_network_profile: Optional[str] = Field(
        default=None,
        alias='ym:s:<attribution>SocialNetworkProfile',
        description='Группа социальной сети.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    recommendation_system: Optional[str] = Field(
        default=None,
        alias='ym:s:<attribution>RecommendationSystem',
        description='Переход из рекомендательных систем.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    messenger: Optional[str] = Field(
        default=None,
        alias='ym:s:<attribution>Messenger',
        description='Переход из мессенджера.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )


class SAdvSchema(_FK):
    direct_click_order: Optional[int] = Field(
        default=None,
        alias='ym:s:<attribution>DirectClickOrder',
        description='Кампания Яндекс.Директа.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('UInt32')}
    )
    direct_banner_group: Optional[int] = Field(
        default=None,
        alias='ym:s:<attribution>DirectBannerGroup',
        description='Группа объявлений.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('UInt32')}
    )
    direct_click_banner: Optional[str] = Field(
        default=None,
        alias='ym:s:<attribution>DirectClickBanner',
        description='Объявление Яндекс.Директа.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    direct_click_order_name: Optional[str] = Field(
        default=None,
        alias='ym:s:<attribution>DirectClickOrderName',
        description='Название кампании Яндекс.Директа.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    click_banner_group_name: Optional[str] = Field(
        default=None,
        alias='ym:s:<attribution>ClickBannerGroupName',
        description='Название группы объявлений.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    direct_click_banner_name: Optional[str] = Field(
        default=None,
        alias='ym:s:<attribution>DirectClickBannerName',
        description='Название объявления Яндекс.Директа.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    direct_phrase_or_cond: Optional[str] = Field(
        default=None,
        alias='ym:s:<attribution>DirectPhraseOrCond',
        description='Условие показа объявления.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    direct_platform_type: Optional[str] = Field(
        default=None,
        alias='ym:s:<attribution>DirectPlatformType',
        description='Тип площадки.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    direct_platform: Optional[str] = Field(
        default=None,
        alias='ym:s:<attribution>DirectPlatform',
        description='Площадка.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    direct_condition_type: Optional[str] = Field(
        default=None,
        alias='ym:s:<attribution>DirectConditionType',
        description='Тип условия показа объявления.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    # В ответе API говорится, что такого поля нет
    # has_gclid: Optional[int] = Field(
    #     default=None,
    #     alias='ym:s:<attribution>HasGCLID',
    #     description='Наличие метки GCLID.',
    #     json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('UInt8')}
    # )
    gclid: Optional[str] = Field(
        default=None,
        alias='ym:s:<attribution>GCLID',
        description='Метка GCLID.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    from_mark: Optional[str] = Field(
        default=None,
        alias='ym:s:from',
        description='Метка from.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    )
    # В ответе API говорится, что таких полей нет
    # openstat_ad: Optional[str] = Field(
    #     default=None,
    #     alias='ym:s:<attribution>OpenstatAd',
    #     description='Openstat Ad.',
    #     json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    # )
    # openstat_campaign: Optional[str] = Field(
    #     default=None,
    #     alias='ym:s:<attribution>OpenstatCampaign',
    #     description='Openstat Campaign.',
    #     json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    # )
    # openstat_service: Optional[str] = Field(
    #     default=None,
    #     alias='ym:s:<attribution>OpenstatService',
    #     description='Openstat Service.',
    #     json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    # )
    # openstat_source: Optional[str] = Field(
    #     default=None,
    #     alias='ym:s:<attribution>OpenstatSource',
    #     description='Openstat Source.',
    #     json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('String')}
    # )


class SEcommercePurchaseSchema(_FK):
    purchase_id: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:purchaseID',
        description='Идентификатор покупки.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    purchase_date_time: Optional[List[datetime]] = Field(
        default=None,
        alias='ym:s:purchaseDateTime',
        description='Дата и время покупки.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(DateTime)')}
    )
    purchase_affiliation: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:purchaseAffiliation',
        description='Магазин или филиал, в котором произошла транзакция.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    purchase_revenue: Optional[List[float]] = Field(
        default=None,
        alias='ym:s:purchaseRevenue',
        description='Общий доход или суммарная ценность транзакции.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(Float64)')}
    )
    purchase_tax: Optional[List[float]] = Field(
        default=None,
        alias='ym:s:purchaseTax',
        description='Сумма всех налогов, связанных с транзакцией.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(Float64)')}
    )
    purchase_shipping: Optional[List[float]] = Field(
        default=None,
        alias='ym:s:purchaseShipping',
        description='Стоимость доставки, связанная с транзакцией.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(Float64)')}
    )
    purchase_coupon: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:purchaseCoupon',
        description='Промокод, ассоциированный со всей покупкой целиком.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    purchase_currency: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:purchaseCurrency',
        description='Валюта транзакции.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    purchase_product_quantity: Optional[List[int]] = Field(
        default=None,
        alias='ym:s:purchaseProductQuantity',
        description='Количество товаров в покупке.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(Int64)')}
    )


class SEcommercePurchaseProductSchema(_FK):
    products_purchase_id: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:productsPurchaseID',
        description='Идентификатор покупки.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    products_id: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:productsID',
        description='Идентификатор или код купленного товара.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    products_name: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:productsName',
        description='Название купленного товара.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    products_brand: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:productsBrand',
        description='Бренд, к которому относится купленный товар.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    products_category: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:productsCategory',
        description='Категория, к которой относится купленный товар.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    products_category1: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:productsCategory1',
        description='Категория, к которой относится купленный товар, уровень 1.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    products_category2: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:productsCategory2',
        description='Категория, к которой относится купленный товар, уровень 2.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    products_category3: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:productsCategory3',
        description='Категория, к которой относится купленный товар, уровень 3.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    products_category4: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:productsCategory4',
        description='Категория, к которой относится купленный товар, уровень 4.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    products_category5: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:productsCategory5',
        description='Категория, к которой относится купленный товар, уровень 5.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    products_variant: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:productsVariant',
        description='Вариант купленного товара.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    products_position: Optional[List[int]] = Field(
        default=None,
        alias='ym:s:productsPosition',
        description='Позиция купленного товара в списке или коллекции.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(Int32)')}
    )
    products_price: Optional[List[float]] = Field(
        default=None,
        alias='ym:s:productsPrice',
        description='Цена купленного товара.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(Float64)')}
    )
    products_currency: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:productsCurrency',
        description='Валюта купленного товара.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    products_coupon: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:productsCoupon',
        description='Промокод, ассоциированный с купленным товаром.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    products_quantity: Optional[List[int]] = Field(
        default=None,
        alias='ym:s:productsQuantity',
        description='Количество купленных товаров.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(Int64)')}
    )
    products_list: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:productsList',
        description='Список, в который входят купленные товары, связанные с транзакцией.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    products_event_time: Optional[List[datetime]] = Field(
        default=None,
        alias='ym:s:productsEventTime',
        description='Дата и время покупки товара.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(DateTime)')}
    )
    products_discount: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:productsDiscount',
        description='Процент скидки на купленный товар.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )


class SEcommerceEventProductSchema(_FK):
    events_product_id: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:eventsProductID',
        description='Идентификатор или код товара.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    events_product_list: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:eventsProductList',
        description='Список, в который входят товары, связанные с транзакцией.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    events_product_brand: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:eventsProductBrand',
        description='Бренд, к которому относится товар.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    events_product_category: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:eventsProductCategory',
        description='Категория, к которой относится товар.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    events_product_category1: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:eventsProductCategory1',
        description='Категория, к которой относится товар, уровень 1.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    events_product_category2: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:eventsProductCategory2',
        description='Категория, к которой относится товар, уровень 2.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    events_product_category3: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:eventsProductCategory3',
        description='Категория, к которой относится товар, уровень 3.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    events_product_category4: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:eventsProductCategory4',
        description='Категория, к которой относится товар, уровень 4.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    events_product_category5: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:eventsProductCategory5',
        description='Категория, к которой относится товар, уровень 5.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    events_product_variant: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:eventsProductVariant',
        description='Вариант товара.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    events_product_position: Optional[List[int]] = Field(
        default=None,
        alias='ym:s:eventsProductPosition',
        description='Позиция товара в списке или коллекции.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(Int32)')}
    )
    events_product_price: Optional[List[float]] = Field(
        default=None,
        alias='ym:s:eventsProductPrice',
        description='Цена товара.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(Float64)')}
    )
    events_product_currency: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:eventsProductCurrency',
        description='Валюта товара.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    events_product_coupon: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:eventsProductCoupon',
        description='Промокод, ассоциированный с товаром.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    events_product_quantity: Optional[List[int]] = Field(
        default=None,
        alias='ym:s:eventsProductQuantity',
        description='Количество товаров.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(UInt64)')}
    )
    events_product_event_time: Optional[List[datetime]] = Field(
        default=None,
        alias='ym:s:eventsProductEventTime',
        description='Дата и время события.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(DateTime)')}
    )
    events_product_type: Optional[List[int]] = Field(
        default=None,
        alias='ym:s:eventsProductType',
        description='Тип события. Возможные значения: view_item_list — просмотр списка товара, click — клик по товару, '
                    'detail — просмотр карточки товара, add — добавление товара в корзину, purchase — покупка.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(UInt8)')}
    )
    events_product_discount: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:eventsProductDiscount',
        description='Процент скидки на товар.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    events_product_name: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:eventsProductName',
        description='Название товара.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )


class SEcommerceImpressionProductSchema(_FK):
    impressions_url: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:impressionsURL',
        description='URL страницы с товаром.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    impressions_date_time: Optional[List[datetime]] = Field(
        default=None,
        alias='ym:s:impressionsDateTime',
        description='Дата и время просмотра.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(DateTime)')}
    )
    impressions_product_id: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:impressionsProductID',
        description='Идентификатор просмотренного товара.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    impressions_product_name: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:impressionsProductName',
        description='Название просмотренного товара.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    impressions_product_brand: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:impressionsProductBrand',
        description='Бренд, к которому относится просмотренный товар.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    impressions_product_category: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:impressionsProductCategory',
        description='Категория, к которой относится просмотренный товар.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    impressions_product_category1: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:impressionsProductCategory1',
        description='Категория, к которой относится просмотренный товар, уровень 1.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    impressions_product_category2: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:impressionsProductCategory2',
        description='Категория, к которой относится просмотренный товар, уровень 2.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    impressions_product_category3: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:impressionsProductCategory3',
        description='Категория, к которой относится просмотренный товар, уровень 3.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    impressions_product_category4: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:impressionsProductCategory4',
        description='Категория, к которой относится просмотренный товар, уровень 4.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    impressions_product_category5: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:impressionsProductCategory5',
        description='Категория, к которой относится просмотренный товар, уровень 5.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    impressions_product_variant: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:impressionsProductVariant',
        description='Вариант просмотренного товара.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('AArray(String)')}
    )
    impressions_product_price: Optional[List[float]] = Field(
        default=None,
        alias='ym:s:impressionsProductPrice',
        description='Цена просмотренного товара.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(Float64)')}
    )
    impressions_product_currency: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:impressionsProductCurrency',
        description='Валюта просмотренного товара.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    impressions_product_coupon: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:impressionsProductCoupon',
        description='Промокод, ассоциированный с просмотренным товаром.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    impressions_product_list: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:impressionsProductList',
        description='Список, в который входят просмотренные товары, связанные с транзакцией.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    impressions_product_quantity: Optional[List[int]] = Field(
        default=None,
        alias='ym:s:impressionsProductQuantity',
        description='Количество просмотренных товаров.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(UInt64)')}
    )
    impressions_product_event_time: Optional[List[datetime]] = Field(
        default=None,
        alias='ym:s:impressionsProductEventTime',
        description='Дата и время просмотра товара. То же, что и ym:s:impressionsDateTime.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(DateTime)')}
    )
    impressions_product_discount: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:impressionsProductDiscount',
        description='Процент скидки на просмотренный товар.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )


class SParamsSchema(_FK):
    parsed_params_key1: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:parsedParamsKey1',
        description='Параметры визита, ур. 1.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    parsed_params_key2: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:parsedParamsKey2',
        description='Параметры визита, ур. 2.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    parsed_params_key3: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:parsedParamsKey3',
        description='Параметры визита, ур. 3.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    parsed_params_key4: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:parsedParamsKey4',
        description='Параметры визита, ур. 4.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    parsed_params_key5: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:parsedParamsKey5',
        description='Параметры визита, ур. 5.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    parsed_params_key6: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:parsedParamsKey6',
        description='Параметры визита, ур. 6.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    parsed_params_key7: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:parsedParamsKey7',
        description='Параметры визита, ур. 7.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    parsed_params_key8: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:parsedParamsKey8',
        description='Параметры визита, ур. 8.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    parsed_params_key9: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:parsedParamsKey9',
        description='Параметры визита, ур. 9.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    parsed_params_key10: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:parsedParamsKey10',
        description='Параметры визита, ур. 10.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )


class SGoalSchema(_FK):
    goals_id: Optional[List[int]] = Field(
        default=None,
        alias='ym:s:goalsID',
        description='Номера целей, достигнутых за данный визит.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(UInt32)')}
    )
    goals_serial_number: Optional[List[int]] = Field(
        default=None,
        alias='ym:s:goalsSerialNumber',
        description='Порядковые номера достижений цели с конкретным идентификатором.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(UInt32)')}
    )
    goals_date_time: Optional[List[datetime]] = Field(
        default=None,
        alias='ym:s:goalsDateTime',
        description='Время достижения каждой цели (в часовом поясе UTC+3).',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(DateTime)')}
    )
    goals_price: Optional[List[float]] = Field(
        default=None,
        alias='ym:s:goalsPrice',
        description='Ценность цели.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(Float64)')}
    )
    goals_order: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:goalsOrder',
        description='Идентификатор заказов.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    goals_currency: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:goalsCurrency',
        description='Идентификатор валюты.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )


class SCalltrackingSchema(_FK):
    offline_call_talk_duration: Optional[List[int]] = Field(
        default=None,
        alias='ym:s:offlineCallTalkDuration',
        description='Длительность звонка в секундах.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(UInt32)')}
    )
    offline_call_hold_duration: Optional[List[int]] = Field(
        default=None,
        alias='ym:s:offlineCallHoldDuration',
        description='Длительность ожидания звонка в секундах.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(UInt32)')}
    )
    offline_call_missed: Optional[List[int]] = Field(
        default=None,
        alias='ym:s:offlineCallMissed',
        description='Пропущен ли звонок.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(UInt32)')}
    )
    offline_call_tag: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:offlineCallTag',
        description='Произвольная метка.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    offline_call_first_time_caller: Optional[List[int]] = Field(
        default=None,
        alias='ym:s:offlineCallFirstTimeCaller',
        description='Первичный ли звонок.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(UInt32)')}
    )
    offline_call_url: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:offlineCallURL',
        description='URL, с которого был звонок (ассоциированная с событием страница).',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )


class SEcommercePromotionSchema(_FK):
    promotion_id: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:promotionID',
        description='Идентификатор или код промокампании.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    promotion_name: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:promotionName',
        description='Название промокампании.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    promotion_creative: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:promotionCreative',
        description='Название рекламного баннера.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    promotion_position: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:promotionPosition',
        description='Позиция рекламного баннера.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    promotion_creative_slot: Optional[List[str]] = Field(
        default=None,
        alias='ym:s:promotionCreativeSlot',
        description='Слот рекламного баннера.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(String)')}
    )
    promotion_event_time: Optional[List[datetime]] = Field(
        default=None,
        alias='ym:s:promotionEventTime',
        description='Дата и время события рекламной кампании.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(DateTime)')}
    )
    promotion_type: Optional[List[int]] = Field(
        default=None,
        alias='ym:s:promotionType',
        description='Тип события рекламной кампании: promoView — просмотр рекламного материала, promoClick — клик по '
                    'рекламному материалу.',
        json_schema_extra={'clickhouse_schema': fill_clickhouse_schema('Array(UInt8)')}
    )


class VisitGlobalSchema(
    SCalltrackingSchema,
    SEcommercePromotionSchema,
    SEcommerceImpressionProductSchema,
    SEcommerceEventProductSchema,
    SEcommercePurchaseProductSchema,
    SEcommercePurchaseSchema,
    SParamsSchema,
    SGoalSchema,
    SAdvSchema,
    STrafficSourceSchema,
    SUTMSchema,
    SGeoSchema,
    SBrowserDeviceSchema,
    SessionSchema
):
    """
    Все поля визитов.
    """
    pass
