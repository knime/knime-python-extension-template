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

    model_path = knext.LocalPathParameter(
        "Path to model", "The local file system path to the model."
    )

    def configure(self, configure_context, input_schema_1):
        return input_schema_1

    def execute(self, exec_context, input_1):
        return input_1
