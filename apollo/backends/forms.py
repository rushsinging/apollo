# -*- coding: utf-8 -*-

import voluptuous

ukey = {
    voluptuous.Required('ukey'): voluptuous.Match(r'^[0-9a-zA-Z]{8}$'),
}

nickname = {
    voluptuous.Required('nickname'): voluptuous.All(
        voluptuous.Coerce(unicode), voluptuous.Length(max=20))
}
