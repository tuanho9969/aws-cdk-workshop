#!/usr/bin/env python3

from aws_cdk import core

from cdk_python_workshop.cdk_python_workshop_stack import CdkPythonWorkshopStack


app = core.App()
CdkPythonWorkshopStack(app, "cdk-python-workshop")

app.synth()
