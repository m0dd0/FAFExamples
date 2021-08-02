import adsk.core, adsk.fusion, adsk.cam, traceback

from .fusion_addin_framework import fusion_addin_framework as faf


# specify position of addin
addin = None


def say_hi(event_args: adsk.core.CommandEventArgs):
    adsk.core.Application.get().userInterface.messageBox("hi")


def run(context):
    global addin
    addin = faf.FusionAddin()
    ws = faf.Workspace(parent=addin, id="FusionSolidEnvironment")
    tab = faf.Tab(parent=ws, id="SolidTab")
    panel = faf.Panel(parent=tab, id="SolidCreatePanel")
    control = faf.Control(parent=panel, isPromoted=True)
    cmd = faf.AddinCommand(parent=control, onExecute=say_hi, name="my command")


def stop(context):
    addin.stop()
