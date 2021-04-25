# -*- coding: utf-8 -*-
import simplejson
import re
import datetime

# no JSON.stringigy in Python
SEP = "!!-_-____-_-!!"

class JS:
    def __init__(self, js_code: str):
        self.js_code = "%s%s%s" % (SEP, js_code, SEP)

    def replace(self, pattern: str, repl: str):
        self.js_code = re.sub(pattern, repl, self.js_code)
        return self


def _json_dump_default(o: object):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()
    if isinstance(o, JS):
        return o.replace("\\n|\\t", "").replace(r"\\n", "\n").replace(r"\\t", "\t").js_code
    return o


def json_dump_to_js(options: object):
    return re.sub(
        '"?%s"?' % SEP,
        "",
        simplejson.dumps(options, indent=2, default=_json_dump_default, ignore_nan=True)
    )
