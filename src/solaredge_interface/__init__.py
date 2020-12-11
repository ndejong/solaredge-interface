# -*- coding: utf8 -*-
# Copyright (c) 2020 Nicholas de Jong

__title__ = "solaredge-interface"
__author__ = "Nicholas de Jong <contact@nicholasdejong.com>"
__version__ = '0.2.1'
__license__ = "MIT"

__env_api_key__ = 'SOLAREDGE_API_KEY'
__env_site_id__ = 'SOLAREDGE_SITE_ID'
__env_output_format__ = 'SOLAREDGE_OUTPUT_FORMAT'

__output_format_default__ = 'json'

__config_file_user__ = '~/.solaredge-interface'
__config_file_system__ = '/etc/solaredge-interface'
__config_section_name__ = 'solaredge-interface'

__solaredge_api_baseurl__ = 'https://monitoringapi.solaredge.com'
__http_request_timeout__ = 10
__http_request_user_agent__ = '{}/{}'.format(__title__, __version__)
