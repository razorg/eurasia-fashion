# -*- coding: utf-8 -*-
from tipfy.sessions import SessionMiddleware
"""App configuration."""

config = {
    'tipfy' : {
        'middleware': [
            SessionMiddleware(),
            'tipfy.ext.i18n.I18nMiddleware',
        ],
        'auth_store_class': 'tipfy.auth.MultiAuthStore',
        'apps_installed' : ['apps.eurasia-fashion']
    },
    'tipfyext.jinja2' : {
        'environment_args' : {
            'extensions' : ['jinja2.ext.i18n',]
        }
    },
    'tipfy.i18n' : {
        'locale':'en_US',
        'locale_request_lookup':[('cookies','lang')],
        'cookie_name':'lang'
    },
    'tipfy.sessions' : {
        'secret_key' : 'fafa81\xe5Y\x86b\xd56.#m\xa1\r#\xb7%\x93\xcc+\xc3\xb9\xeb\x97p>\xa7\x87\x83\xac\xeef\xe9\x96\x06\x7f\x1a<\xbf|<\xac\x853\x97\x96\x9e1\xd8\xad-\xc7hL\x1d~/9\xc1'
    }
}
