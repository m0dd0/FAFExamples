import adsk.core, adsk.fusion, adsk.cam, traceback

from .fusion_addin_framework import fusion_addin_framework as faf

cmd = None


def say_hi(event_args: adsk.core.CommandEventArgs):
    adsk.core.Application.get().userInterface.messageBox("hi")


def run(context):
    try:
        global cmd
        cmd = (
            faf.Workspace()
            .tab()
            .panel()
            .dropdown()
            .dropdown()
            .dropdown()
            .dropdown()
            .control()
            .addinCommand(execute=say_hi)
        )
    except:
        adsk.core.Application.get().userInterface.messageBox(
            "Failed:\n{}".format(traceback.format_exc())
        )


def stop(context):
    try:
        cmd.addin.stop()
    except:
        adsk.core.Application.get().userInterface.messageBox(
            "Failed:\n{}".format(traceback.format_exc())
        )
