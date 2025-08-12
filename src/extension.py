import logging
import knime.extension as knext

LOGGER = logging.getLogger(__name__)


@knext.parameter_group("Custom header")
class CustomHeader:
    key = knext.StringParameter("Key", "Key of the header.")
    value = knext.StringParameter("Value", "Value of the header.")


@knext.node(
    name="My Template Node",
    node_type=knext.NodeType.LEARNER,
    icon_path="../icons/icon.png",
    category="/",
)
@knext.input_table(name="Input Data", description="We read data from here")
# @knext.input_table(name="Tutorial: Input Data 2", description="We also read data from here") ### Tutorial step 11: Uncomment to create a new input port
@knext.output_table(name="Output Data", description="Whatever the node has produced")
class TemplateNode:
    """Short one-line description of the node.
    Long description of the node.
    Can be multiple lines.
    """

    custom_headers = knext.ParameterArray(
        parameters=CustomHeader(),
        button_text="Add header",
        array_title="Header",
        label="Custom headers",
        description="Any custom headers to include in requests to the API.",
        since_version="0.1.0",
        is_advanced=True,
    )

    ### Tutorial step 10: Uncomment all of the following parameters and the 'is_numeric' method to create your first dialogue ###
    # (Restart KAP and drag&drop the node again from the node repository to let changes take effect)
    # some_param = knext.IntParameter("Some Int Parameter", "The answer to everything", 42, min_value=0)

    # another_param = knext.StringParameter("Some String parameter", "The classic placeholder", "foobar")

    # double_param = knext.DoubleParameter("Double Parameter", "Just for test purposes", 3.0)

    # boolean_param = knext.BoolParameter("Boolean Parameter", "also just for testing", True)

    # column_param = knext.ColumnParameter()

    # def is_numeric(column):  # Filter columns visible in the column_param for numeric ones
    #     return (
    #         column.ktype == knext.double()
    #         or column.ktype == knext.int32()
    #         or column.ktype == knext.int64()
    #     )

    # column_param = knext.ColumnParameter(label="label", description="description", port_index=0, column_filter=is_numeric)

    def configure(self, configure_context, input_schema_1):
        # def configure(self, configure_context, input_schema_1, input_schema_2):  ### Tutorial step 11: Uncomment to configure the new port (and comment out the previous configure header)
        return input_schema_1
        ### Tutorial step 12: Uncomment the following to adjust to the changes we do in this step in the execute method (and comment out the previous return statement)
        # return input_schema_1.append(knext.Column(knext.double(), "column2"))
        ### Tutorial step 13: Uncomment to set a warning for the configuration, which will be shown in the workflow
        # configure_context.set_warning("This is a warning during configuration")

    def execute(self, exec_context, input_1):
        # def execute(self, exec_context, input_1, input_2):  ### Tutorial step 11: Uncomment to accept the new port (and comment out the previous execute header)
        return input_1
        ### Tutorial step 12: Uncomment the following lines to work with the new port (and comment out the previous return statement)
        # input_1_pandas = input_1.to_pandas() # Transform the input table to some processable format (pandas or pyarrow)
        # input_2_pandas = input_2.to_pandas()
        # input_1_pandas['column2'] = input_1_pandas['column1'] + input_2_pandas['column1']
        # return knext.Table.from_pandas(input_1_pandas)
        ### Tutorial step 13: Uncomment the following line to use the parameters from the configuration dialogue (and comment out the previous return statement)
        # input_1_pandas['column2'] = input_1_pandas['column2'] + self.double_param
        # LOGGER.warning(self.double_param) # Tutorial step 14: Logging some warning to the console
        # exec_context.set_warning("This is a warning") # Tutorial step 14: Set a warning to be shown in the workflow
        # return knext.Table.from_pandas(input_1_pandas) ### Tutorial step 13: Uncomment
