import unittest
import pandas as pd
import knime.extension as knext
import knime.extension.testing as ktest
from pandas.testing import assert_frame_equal

from src.extension import TemplateNode


class TestTemplateNode(unittest.TestCase):
    """Simple, runnable examples for the minimal TemplateNode."""

    def test_configure_pass_through(self):
        # Given an input schema with two columns...
        schema = knext.Schema.from_columns(
            [
                knext.Column(knext.int64(), "Integers"),
                knext.Column(knext.double(), "Doubles"),
            ]
        )

        node = TemplateNode()
        config_context = ktest.TestingConfigurationContext()

        # When configure is called, the minimal node returns the same schema.
        output_schema = node.configure(config_context, schema)
        self.assertEqual(schema, output_schema)

    def test_execute_pass_through(self):
        # Given a simple input table...
        input_df = pd.DataFrame(
            {
                "Test": [1, 2, 3, 4],
                "Test Strings": ["asdf", "foo", "bar", "baz"],
            }
        )

        node = TemplateNode()
        input_table = knext.Table.from_pandas(input_df)
        exec_context = ktest.TestingExecutionContext()

        # When executed, the minimal node returns the input unchanged.
        output_table = node.execute(exec_context, input_table)
        output_df = output_table.to_pandas()

        assert_frame_equal(input_df, output_df, check_dtype=False)


if __name__ == "__main__":
    unittest.main()
