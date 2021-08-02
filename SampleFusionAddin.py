import adsk.core, adsk.fusion, adsk.cam, traceback

from .fusion_addin_framework import fusion_addin_framework as faf


# Addin with many connected handlers
cmd = None


def create_inputs(event_args: adsk.core.CommandCreatedEventArgs):
    event_args.command.commandInputs.addBoolValueInput("boolInputId", "my input", True)


def say_hi(event_args: adsk.core.CommandEventArgs):
    adsk.core.Application.get().userInterface.messageBox("hi")


def run(context):
    try:
        global cmd
        cmd = faf.AddinCommand(
            name="my command", onExecute=say_hi, onCommandCreated=create_inputs
        )
        # it is not necessary to use the "on"-prefix, the line below is equivalent
        # cmd = faf.AddinCommand(name="my command", execute=say_hi, created=create_inputs )

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
