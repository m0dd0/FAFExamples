import adsk.core, adsk.fusion, adsk.cam, traceback

from .fusion_addin_framework import fusion_addin_framework as faf


# Addin at a very custom position
addin = None


def say_hi(event_args: adsk.core.CommandEventArgs):
    adsk.core.Application.get().userInterface.messageBox("hi")


def run(context):
    try:
        global addin
        addin = faf.FusionAddin()
        # its not possible to create a custom workspace so the Design Workspace is used
        ws = faf.Workspace(parent=addin, id="FusionSolidEnvironment")
        # passing the "random" as an id will generate an UUID, it would be also possible
        # to use a custom id like "MySuperCustomId1234"
        tab = faf.Tab(parent=ws, id="random", name="my tab")
        panel = faf.Panel(parent=tab, id="random", name="my panel")
        control = faf.Control(parent=panel, isPromoted=True, isPromotedByDefault=True)
        cmd = faf.AddinCommand(
            parent=control, onExecute=say_hi, name="my command", resourceFolder="cubes"
        )
    except:
        print("except")


def stop(context):
    addin.stop()
