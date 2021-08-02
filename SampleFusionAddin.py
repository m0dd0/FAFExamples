import adsk.core, adsk.fusion, adsk.cam, traceback
from .fusion_addin_framework import fusion_addin_framework as faf

addin = None


def say_hi(event_args: adsk.core.CommandEventArgs):
    adsk.core.Application.get().userInterface.messageBox("hi")


def run(context):
    global addin
    addin = faf.FusionAddin()

    # access the attributes and methods of the workspace instance
    ws = faf.Workspace(parent=addin, id="FusionSolidEnvironment")
    print(ws.parent)
    print(ws.addin)
    print(ws.isActive)
    print(ws.name)
    print(ws.objectType)
    print(ws.productType)
    print(ws.resourceFolder)
    print(ws.toolClipFilename)
    ws.activate()
    # ...

    tab = faf.Tab(parent=ws, id="SolidTab")
    print(tab.parent)
    print(tab.id)
    print(tab.index)
    print(tab.isActive)
    print(tab.name)
    print(tab.objectType)
    tab.activate()
    # ...

    panel = faf.Panel(parent=tab, id="SolidCreatePanel")
    print(panel.parent)
    print(panel.controls)
    print(panel.id)
    print(panel.isValid)
    print(panel.isVisible)
    print(panel.name)
    print(panel.indexWithinTab("SolidTab"))
    # ...

    button = faf.Control(parent=panel, isPromoted=True)
    print(button.parent)
    print(button.commandDefinition)
    print(button.id)
    print(button.isPromoted)
    button.isPromoted = False
    button.isPromotedByDefault = False
    print(button.isVisible)
    print(button.objectType)
    print(button.parent)
    # ...

    cmd = faf.AddinCommand(parent=button, onExecute=say_hi, name="my command")
    print(cmd.parent)
    print(cmd.controlDefinition)
    print(cmd.isVisible)
    print(cmd.id)
    print(cmd.isNative)
    print(cmd.resourceFolder)
    # ...


def stop(context):
    addin.stop()