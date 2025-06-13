import logging
import knime.extension as knext

LOGGER = logging.getLogger(__name__)


@knext.node(
    name="My Template Node",
    node_type=knext.NodeType.LEARNER,
    icon_path="../icons/icon.png",
    category="/",
)
@knext.input_table(name="Input Data", description="We read data from here")
@knext.output_table(name="Output Data", description="Whatever the node has produced")
class TemplateNode:
    """Short one-line description of the node.
    Long description of the node.
    Can be multiple lines.
    """

    param_0 = knext.IntParameter(
        label="Param 1",
        description="",
        default_value=1,
    )

    param_1 = knext.IntParameter(
        label="Param 1",
        description="",
        default_value=1,
        is_advanced=True,
        min_value=0,  # The "show advanced settings" button will show up if this is None
    )

    # If there is a non-number parameter that is advanced, the "show advanced settings" button shows up
    # param_2 = knext.StringParameter(
    #     label="Param 2",
    #     description="",
    #     default_value="default",
    #     is_advanced=True,
    # )

    def configure(self, configure_context, input_schema_1):
        return input_schema_1

    def execute(self, exec_context, input_1):
        return input_1
