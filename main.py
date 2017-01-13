#!/usr/bin/env python

import logging as log

from lib.person import Person
from lib.organisation import Organisation
from lib.yamlad import YamlAD

log_format = "%(levelname)s: [%(filename)s:%(lineno)s - %(funcName)s() ] - %(message)s"
log.basicConfig(level=log.DEBUG, format=log_format)

org = Organisation("Praqma", "Praqma")
person = Person("ady",
                "andrey9kin",
                "Andrey",
                "Devyatkin",
                "andrey.a.devyatkin@gmail.com")
ad = YamlAD("/Users/andrey9kin/code/onboarding-as-code/ad")


ad.add_person(person)
ad.get_person(person.pid)

print person
