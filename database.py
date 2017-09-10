#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import os
from util import logging

class DB(object):
  def __init__(self):
    import redis

    self.__r = redis.StrictRedis(host='localhost', port=6379, db=0)

  def set(self, key, value, ttl=60, namespace=None):
    if self.__r:
      _key = key if namespace is None else '{}:{}'.format(namespace, key)
      self.__r.setex(_key, ttl, pickle.dumps(value))

  def get(self, key, namespace=None):
    _key = key if namespace is None else '{}:{}'.format(namespace, key)
    value = self.__r.get(_key) if self.__cache else None
    return pickle.loads(value) if value else None

