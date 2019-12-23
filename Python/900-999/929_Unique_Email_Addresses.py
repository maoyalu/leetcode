import unittest


def solution(emails):

    # ********** Attempt 1 - 2019/09/20  ********** 

    email_list = set()
    for email in emails:
        local, domain = email.split('@')
        if '+' in local:
            local = local[:local.index('+')]
        email_list.add(local.replace('.', '') + '@' + domain)
    return len(email_list)


class TestSolution(unittest.TestCase):
    def test1(self):
        emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
        answer = 2
        self.assertEqual(solution(emails), answer)


if __name__ == "__main__":
    unittest.main()