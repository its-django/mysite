#!/usr/bin/env python
# encoding: utf-8

import logging

from django.db import transaction

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@transaction.atomic
def transfer_money(_from, _to, quota):
    try:
        _from.money = _from.money - quota
        if _from.money < 0:
            raise ValueError("超額提領!")
        _from.save()
        _to.money = _to.money + quota
        if _to.money > 100000:
            raise ValueError("超額儲存!")
        _to.save()
    except ValueError as e:
        logger.error("金額操作錯誤, 訊息:<{}>".format(e))
    except Exception as e:
        logger.error("其他錯誤，訊息:<{}>".format(e))
