import nz_mps
import nose
from nose.tools import *


with app.test_client() as c:
    resp = c.get('/mps')
    assertEquals(resp.status_code, 200)
