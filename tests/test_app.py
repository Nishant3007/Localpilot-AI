import unittest,tempfile,os,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import server
class AppTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();server.DB=Path(self.tmp.name)/'test.db';server.init()
 def tearDown(self):self.tmp.cleanup()
 def test_seed(self):
  with server.conn() as c:
   self.assertEqual(c.execute('SELECT COUNT(*) FROM menu').fetchone()[0],16)
   self.assertGreater(c.execute('SELECT COUNT(*) FROM sales').fetchone()[0],100)
 def test_metrics_are_reconciled(self):
  m=server.metric_data(1,30)
  self.assertGreater(m['revenue'],0)
  self.assertAlmostEqual(m['revenue']-m['estimated_ingredient_cost'],m['estimated_contribution'])
  self.assertEqual(sum(round(x['revenue']*100) for x in m['series']),round(m['revenue']*100))
 def test_demo_is_labeled(self):self.assertTrue(server.metric_data(1)['is_demo'])
 def test_no_data_for_other_business(self):self.assertEqual(server.metric_data(999)['orders'],0)
 def test_password_hash(self):
  import hashlib,hmac
  with server.conn() as c:r=c.execute('SELECT * FROM users').fetchone()
  self.assertTrue(hmac.compare_digest(hashlib.pbkdf2_hmac('sha256',b'demo12345',bytes.fromhex(r['salt']),240000).hex(),r['password_hash']))
if __name__=='__main__':unittest.main()
