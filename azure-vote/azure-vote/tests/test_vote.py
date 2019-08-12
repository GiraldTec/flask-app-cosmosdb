import pytest
import math

def vote_one():
   num = 25
   assert math.sqrt(num) == 5

def vote_two():
   num = 25
   assert math.sqrt(num) == 5

def failed_vote():
   num = 25
   assert math.sqrt(num) == 5

def connect_source():
   num = 25
   assert math.sqrt(num) == 5

def transact_perf():
   num = 25
   assert math.sqrt(num) == 5

def code_coverage():
   assert 2*20 == 40