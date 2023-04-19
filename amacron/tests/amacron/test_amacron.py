'''
Created on 31-Jan-2020

@author: a4yadav
'''
import unittest

from amacron.amacron import AmacronConverter


class TestAmacronConverter(unittest.TestCase):

    def test_amacron_to_cron(self):
        test_cases = {
            'every minute': '* * * * *',
            'every 15 minute': '*/15 * * * *',
            'every hour': '0 */1 * * *',
            'every 5 hours': '0 */5 * * *',
            'every 3 days': '0 0 */3 * *',
            'every month': '0 0 1 */1 *',
            'every 6 months': '0 0 1 */6 *',
            'every min from 10:00': '00/1 10 * * *',
            'every 10 mins at 15:00': '00/10 15 * * *',
            'every hour from 10:00': '00 10/1 * * *',
            'every 3 hours from 10:00 to 12:00': '00 10-12/3 * * *',
            'every 5 days at 06:00': '00 06 */5 * *',
            'every month from 12:00': '00 12 * */1 *',
            'every 6 months from 10:00': '00 10 * */6 *',
            'first of every week': '0 0 * * 1',
            'first of every week at 12:00': '00 12 * * 1',
            'first of every month': '0 0 1 * *',
            'first of every 2 months': '0 0 1 */2 *',
            'first of every month from 10:30 to 12:00': '30 10-12 1 * *',
            'first of every 2 month at 06:30': '30 06 1 */2 *',
            'at 23rd minute': '23 * * * *',
            'every hour at 45th minute': '45 */1 * * *',
            'every 5 hours at 22nd min': '22 */5 * * *',
            'every day at 2nd hour': '0 2 */1 * *',
            'every 5 days at 45th minute': '45 * */5 * *',
            'every 2 months at 12th min': '12 * * */2 *',
            'every month at 12th minute': '12 * * */1 *',
            'every month at 9th hour': '0 9 * */1 *',
            'every month at 6th day': '0 0 6 */1 *',
            'every monday': '0 0 */1 * 1',
            'every thursday at 12th min': '12 * * * 4',
            'every tuesday from 12:00': '00 12 */1 * 2',
            'every day from 04:30': '30 04 */1 * *'
        }

        for amacron, expected in test_cases.items():
            actual = AmacronConverter().convert(amacron)
            self.assertEqual(actual, expected, amacron)

    def test_amacron_to_cron_for_failing_cases(self):
        invalid_expr = "Expression not supported by 'amacron'. Try 'amacron --language' for view language support."
        test_cases = {
            'every 5 days from 13:00 12:00': invalid_expr,
            'every 11 hours at 21st hour': invalid_expr,
        }

        for amacron, expected in test_cases.items():
            actual = AmacronConverter().convert(amacron)
            self.assertEqual(actual, expected)
