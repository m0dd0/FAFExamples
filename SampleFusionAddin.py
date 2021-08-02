import adsk.core, adsk.fusion, adsk.cam, traceback

from .fusion_addin_framework import fusion_addin_framework as faf


def run(context):
    try:
        adsk.core.Application.get().userInterface.messageBox("hi")
    except:
        adsk.core.Application.get().userInterface.messageBox(
            "Failed:\n{}".format(traceback.format_exc())
        )


def stop(context):
    try:
        pass
    except:
        adsk.core.Application.get().userInterface.messageBox(
            "Failed:\n{}".format(traceback.format_exc())
        )
