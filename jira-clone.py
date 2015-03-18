#!/usr/bin/python

"""
(Relatively) Easily clone a JIRA project.

Requires the JIRA CLI - https://bobswift.atlassian.net/wiki/display/ACLI/Atlassian+CLI+Family+of+Tools

Wraps `jira.sh` to ensure _all_ the Project aspects we want cloned are cloned.

In great need of some refactoring and care and attention, but does the job.
"""

import os
import subprocess
import sys


JIRA_CLI_SCRIPT = "./jira.sh"  # TODO argparse / change to the path of your `jira.sh`
JIRA_SERVER = os.environ["JIRA_SERVER"]
JIRA_USERNAME = os.environ["JIRA_USERNAME"]
JIRA_PASSWORD = os.environ["JIRA_PASSWORD"]


JIRA = [
    JIRA_CLI_SCRIPT,
    "--server",
    JIRA_SERVER,
    "--user",
    JIRA_USERNAME,
    "--password",
    JIRA_PASSWORD,
]

BASE_PROJECT = "pandora"
NEW_PROJECT_NAME = sys.argv[1]  # TODO argparse

# TODO Fetch these based on BASE_PROJECT
BASE_ISSUE_TYPE_SCHEME = "PANDORA: Simple Issue Tracking Issue Type Scheme"
BASE_WORKFLOW_SCHEME = "PANDORA: Simple Issue Tracking Workflow Scheme"
BASE_FIELD_CONFIGURATION_SCHEME = "Pandora"
BASE_ISSUE_TYPE_SCREEN_SCHEME = "PANDORA: Simple Issue Tracking Issue Type Screen Scheme"


print subprocess.check_output(JIRA + [
    "--action",
    "cloneProject",
    "--project",
    BASE_PROJECT,
    "--toProject",
    NEW_PROJECT_NAME,
])

print subprocess.check_output(JIRA + [
    "--action",
    "updateProject",
    "--project",
    NEW_PROJECT_NAME,
    "--issueTypeScheme",
    BASE_ISSUE_TYPE_SCHEME,
    "--workflowScheme",
    BASE_WORKFLOW_SCHEME,
    "--fieldConfigurationScheme",
    BASE_FIELD_CONFIGURATION_SCHEME,
    "--issueTypeScreenScheme",
    BASE_ISSUE_TYPE_SCREEN_SCHEME,
    "--lead",
    JIRA_USERNAME,
])
