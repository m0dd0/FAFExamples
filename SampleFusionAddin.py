import adsk.core, adsk.fusion, adsk.cam, traceback

from .fusion_addin_framework import fusion_addin_framework as faf

addin = None


def say_hi(even_args: adsk.core.CommandEventArgs):
    adsk.core.Application.get().userInterface.messageBox("hi")


def run(context):
    try:
        global addin
        addin = faf.FusionAddin()
        workspace = faf.Workspace(addin)
        tab = faf.Tab(workspace, id="ToolsTab")
        panel = faf.Panel(tab, id="SolidScriptsAddinsPanel")
        # use a checkbox instead of a button
        control = faf.Control(panel, controlType="checkbox")
        cmd = faf.AddinCommand(control, name="my checkbox command", execute=say_hi)
    except:
        adsk.core.Application.get().userInterface.messageBox(
            "Failed:\n{}".format(traceback.format_exc())
        )


def stop(context):
    try:
        addin.stop()
    except:
        adsk.core.Application.get().userInterface.messageBox(
            "Failed:\n{}".format(traceback.format_exc())
        )
