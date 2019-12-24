#!/usr/bin/env python

import dataset
import tabulate

db = dataset.connect("sqlite:///db.sqlite3")

print(
    """
Domains
=======
"""
)

print(
    tabulate.tabulate(
        [(row["domain"], row["expected_price"]) for row in db["domains"].find()],
        headers=["domain", "expected_price"],
    )
)


print(
    """
DNS Records
===========
"""
)

print(
    tabulate.tabulate(
        [
            (row["domain"], row["type"], row["name"], row["value"])
            for row in db["records"].find()
        ],
        headers=["domain", "type", "name", "value"],
    )
)
