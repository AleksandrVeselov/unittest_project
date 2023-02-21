from utils import dicts
import unittest


class TestDicts(unittest.TestCase):
    def test_get_val(self):
        self.assertEqual(dicts.get_val({'vcs': 'mercurial'}, 'vcs'), 'mercurial')
        self.assertEqual(dicts.get_val({'vcs': 'mercurial'}, 'mercurial'), 'git')
        self.assertEqual(dicts.get_val({'vcs': 'mercurial'}, 'mercurial', 'bazaar'), 'bazaar')
        self.assertEqual(dicts.get_val({}, 'vsc'), 'git')
        self.assertEqual(dicts.get_val(['vsc', 'mercurial'], 'vsc'), 'git')