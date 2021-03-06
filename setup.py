#!/usr/bin/python

from setuptools import setup, find_packages
from setuptools.command.test import test


class BufferedTestCommand(test):
    """Override setuptools's test command to buffer output."""
    def run_tests(self):
        self.test_args = ["-b"] + self.test_args
        test.run_tests(self)


setup(
    name="rollingpin",
    version="",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "Twisted>=13.1",
    ],
    extras_require={
        "autoscaler": [
            "txzookeeper",
        ],
    },
    cmdclass={
        "test": BufferedTestCommand,
    },
    test_suite="tests",
    entry_points={
        "console_scripts": [
            "rollout = rollingpin.main:main",
        ],

        "rollingpin.hostsource": [
            "mock = rollingpin.hostsources.mock:MockHostSource",
            "autoscaler = rollingpin.hostsources.autoscaler:AutoscalerHostSource",
        ],

        "rollingpin.transport": [
            "mock = rollingpin.transports.mock:MockTransport",
            "ssh = rollingpin.transports.ssh:SshTransport",
        ],
    },
)
