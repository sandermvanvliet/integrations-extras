# (C) Datadog, Inc. 2010-2016
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)

# stdlib
from nose.plugins.attrib import attr

# 3p

# project
from tests.checks.common import AgentCheckTest

instance = {
    'teamcity_url': 'localhost',
    'teamcity_user': 'test',
    'teamcity_pass': 'supersecret'
}


# NOTE: Feel free to declare multiple test classes if needed

@attr(requires='teamcity')
class TestTeamcity(AgentCheckTest):
    """Basic Test for teamcity integration."""
    CHECK_NAME = 'teamcity'
    TEAMCITY_CONFIG = {'teamcity_url': 'http://teammcity.local', 'teamcity_user': 'username', 'teamcity_pass': 'supersecret'}

    def test_check(self):
        self.load_check(self.TEAMCITY_CONFIG, {})

        # run your actual tests...
        self.check.load_config(self.TEAMCITY_CONFIG)

        self.assertEqual('http://teamcity.local', self.check.teamcity_url)
        self.assertEqual('username', self.check.teamcity_user)
        self.assertEqual('supersecret', self.check.teamcity_pass)
