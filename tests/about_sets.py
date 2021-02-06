import unittest

__ = "-=> FILL ME IN! <=-"


class AboutSets(unittest.TestCase):

    def test_sets_make_keep_lists_unique(self):
        highlanders = [
            'MacLeod', 'Ramirez', 'MacLeod', 'Matunas',
            'MacLeod', 'Malcolm', 'MacLeod'
        ]

        there_can_only_be_only_one = set(highlanders)

        self.assertEqual(__, there_can_only_be_only_one)

    def test_empty_sets_have_different_syntax_to_populated_sets(self):
        self.assertEqual(__, {1, 2, 3})
        self.assertEqual(__, set())

    def test_creating_sets_using_strings(self):
        self.assertEqual(__, {'12345'})
        self.assertEqual(__, set('12345'))

    def test_convert_the_set_into_a_list_to_sort_it(self):
        self.assertEqual(__, sorted(set('12345')))

    def test_set_have_arithmetic_operators(self):
        scotsmen = {'MacLeod', 'Wallace', 'Willie'}
        warriors = {'MacLeod', 'Wallace', 'Leonidas'}

        self.assertEqual(__, scotsmen - warriors)
        self.assertEqual(__, scotsmen | warriors)
        self.assertEqual(__, scotsmen & warriors)
        self.assertEqual(__, scotsmen ^ warriors)

    def test_we_can_query_set_membership(self):
        self.assertEqual(__, 127 in {127, 0, 0, 1})
        self.assertEqual(__, 'cow' not in set('apocalypse now'))

    def test_we_can_compare_subsets(self):
        # Note that whitespace between parentheses
        # is ignored in python so we can let our
        # parameters span multiple lines for readability.

        self.assertEqual(
            __,
            set('cake') <= set('cherry cake')
        )
        self.assertEqual(
            __,
            set('cake').issubset(set('cherry cake'))
        )
        self.assertEqual(
            __,
            set('cake') > set('pie')
        )
