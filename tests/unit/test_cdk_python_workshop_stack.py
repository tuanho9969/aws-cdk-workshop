import json
import pytest

from aws_cdk import core
from cdk-python-workshop.cdk_python_workshop_stack import CdkPythonWorkshopStack


def get_template():
    app = core.App()
    CdkPythonWorkshopStack(app, "cdk-python-workshop")
    return json.dumps(app.synth().get_stack("cdk-python-workshop").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
