import unittest

from app import load_balancer


class LoadBalancerAdd(unittest.TestCase):

    def test_add_url(self):
        lb = load_balancer.LoadBalancer(2)
        self.assertTrue(lb.register_url("url1"))
        self.assertTrue(lb.register_url("url2"))
        self.assertFalse(lb.register_url("url3"))


if __name__ == '__main__':
    unittest.main()
