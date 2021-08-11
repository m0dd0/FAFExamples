import adsk.core, adsk.fusion, adsk.cam, traceback

from .fusion_addin_framework import fusion_addin_framework as faf

addin = None


def create_inputs(event_args: adsk.core.CommandCreatedEventArgs):
    event_args.command.commandInputs.addBoolValueInput("boolInputId", "my input", True)


def say_hi(event_args: adsk.core.CommandEventArgs):
    adsk.core.Application.get().userInterface.messageBox("hi")


def say_changed(event_args: adsk.core.InputChangedEventArgs):
    adsk.core.Application.get().userInterface.messageBox("input changed")


def say_ending(event_args: adsk.core.CommandCreatedEventArgs):
    adsk.core.Application.get().userInterface.messageBox("ending")


def run(context):
    try:
        global addin
        addin = faf.FusionAddin()
        ws = faf.Workspace(parent=addin, id="FusionSolidEnvironment")
        tab = faf.Tab(parent=ws, id="SolidTab")
        panel = faf.Panel(parent=tab, id="SolidCreatePanel")
        control = faf.Control(parent=panel, isPromoted=True)
        cmd = faf.AddinCommand(
            parent=control,
            name="my command",
            onExecute=say_hi,
            onCommandCreated=create_inputs,
            onInputChanged=say_changed,
            onDestroy=say_ending,
        )

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