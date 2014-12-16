#!/usr/bin/env python
# encoding: utf-8

import logging

from django.db import transaction

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@transaction.atomic
def transfer_money(_from, _to, quota):

    if _from.money < 15:
        raise ValueError("連手續費都付不起，請回吧!!")

    _from.money = _from.money - 15
    _from.save()

    sid = transaction.savepoint()

    try:
        _from.money = _from.money - quota
        if _from.money < 0:
            raise ValueError("超額提領!")
        _from.save()
        _to.money = _to.money + quota
        if _to.money > 100000:
            raise ValueError("超額儲存!")
        _to.save()
        transaction.savepoint_commit(sid)
    except ValueError as e:
        logger.error("金額操作錯誤, 訊息:<{}>".format(e))
        transaction.savepoint_rollback(sid)
    except Exception as e:
        logger.error("其他錯誤，訊息:<{}>".format(e))
        transaction.savepoint_rollback(sid)
