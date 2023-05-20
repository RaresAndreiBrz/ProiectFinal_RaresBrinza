import unittest

import HtmlTestRunner

from tests import Tests


class MyTestSuite(unittest.TestCase):

    def test_suite(self):
        smoketest = unittest.TestSuite()
        smoketest.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            report_title="Report_tests", report_name="Project tests", combine_reports=True
        )
        runner.run(smoketest)