import adsk.core, adsk.fusion, adsk.cam, traceback

from .fusion_addin_framework import fusion_addin_framework as faf


# Addin with multiple connected handlers
cmd = None


def create_inputs(event_args: adsk.core.CommandCreatedEventArgs):
    event_args.command.commandInputs.addBoolValueInput("boolInputId", "my input", True)


def say_hi(event_args: adsk.core.CommandEventArgs):
    adsk.core.Application.get().userInterface.messageBox("hi")


def say_changed(event_args: adsk.core.InputChangedEventArgs):
    adsk.core.Application.get().userInterface.messageBox("input changed")


def say_by(event_args: adsk.core.CommandCreatedEventArgs):
    adsk.core.Application.get().userInterface.messageBox("by")


def run(context):
    try:
        global cmd
        cmd = faf.AddinCommand(
            name="my command",
            onExecute=say_hi,
            onCommandCreated=create_inputs,
            onInputChanged=say_changed,
            onDestroy=say_by,
        )
        # it is not necessary to use the "on"-prefix, the code below is equivalent
        # cmd = faf.AddinCommand(
        #     name="my command",
        #     execute=say_hi,
        #     commandCreated=create_inputs,
        #     inputChanged=say_changed,
        #     destroy=say_by,
        # )

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
