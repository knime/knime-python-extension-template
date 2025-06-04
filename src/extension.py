import logging
import knime.extension as knext

LOGGER = logging.getLogger(__name__)


@knext.parameter_group(label="Model Parameters")
class TopGroup:
    top_k = knext.IntParameter(
        label="Top k",
        description="The number of top-k tokens to consider when generating text.",
        default_value=1,
        min_value=0,
        is_advanced=True,
    )

    max_new_tokens = knext.IntParameter(
        label="Max new tokens",
        description="""
        The maximum number of tokens to generate in the completion.

        The token count of your prompt plus *max new tokens* cannot exceed the model's context length.
        """,
        default_value=50,
        min_value=0,  # TODO Needs to be commented for the advanced params to be shown
        # is_advanced=True, # TODO Needs to be uncommented for the other advanced param to be shown
    )


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

    model_settings = TopGroup()

    def configure(self, configure_context, input_schema_1):
        return input_schema_1

    def execute(self, exec_context, input_1):
        return input_1
