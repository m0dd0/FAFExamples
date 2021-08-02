import adsk.core, adsk.fusion, adsk.cam, traceback

from .fusion_addin_framework import fusion_addin_framework as faf

addin = None


def say_hi(event_args: adsk.core.CommandEventArgs):
    adsk.core.Application.get().userInterface.messageBox("hi")


def run(context):
    global addin
    addin = faf.FusionAddin()
    ws = faf.Workspace(parent=addin, id="FusionSolidEnvironment")

    solid_tab = faf.Tab(parent=ws, id="SolidTab")
    tools_tab = faf.Tab(parent=ws, id="ToolsTab")

    solid_panel = faf.Panel(parent=solid_tab, id="SolidCreatePanel")
    addin_panel = faf.Panel(parent=tools_tab, id="SolidScriptsAddinsPanel")

    control_1 = faf.Control(parent=solid_panel, isPromoted=True)
    control_2 = faf.Control(parent=addin_panel, isPromoted=True)

    # this command has two parental controls and can therfore be acticated from
    # different postions in the UI
    cmd = faf.AddinCommand(
        parent=[control_1, control_2], onExecute=say_hi, name="my command"
    )


def stop(context):
    addin.stop()
