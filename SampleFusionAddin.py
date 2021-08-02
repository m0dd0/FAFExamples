import adsk.core, adsk.fusion, adsk.cam, traceback

from .fusion_addin_framework import fusion_addin_framework as faf


# specify position of addin dotted style
cmd = None


def say_hi(event_args: adsk.core.CommandEventArgs):
    adsk.core.Application.get().userInterface.messageBox("hi")


def run(context):
    global cmd
    cmd = (
        faf.FusionAddin()
        .workspace(id="FusionSolidEnvironment")
        .tab(id="SolidTab")
        .panel(id="SolidCreatePanel")
        .control(isPromoted=True)
        .addinCommand(onExecute=say_hi, name="my command")
    )


def stop(context):
    cmd.addin.stop()
