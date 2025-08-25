#!/bin/bash
echo "=== KNIME Workflow Execution Summary ==="

# Get workflow information
if [ -f "/home/knime/workflow-info.env" ]; then
    . /home/knime/workflow-info.env
    WORKFLOW_NAME=$(basename "$WORKFLOW_DIR")
    echo "Executed Workflow: $WORKFLOW_NAME"
    echo "Workflow Location: $WORKFLOW_DIR"
else
    echo "⚠ WARNING: Could not determine which workflow was executed"
    WORKFLOW_NAME="Unknown"
fi

echo ""

if [ -f "/home/knime/workflow-console.log" ]; then
    echo "Log file found, analyzing execution..."
    LOG_FILE="/home/knime/workflow-console.log"

    echo "Workflow Status:"
    if grep -q "Workflow executed sucessfully" "$LOG_FILE" || grep -q "Workflow execution done" "$LOG_FILE"; then
        echo "✓ SUCCESS: Workflow completed successfully"
    elif grep -q "ERROR" "$LOG_FILE"; then
        echo "✗ FAILED: Workflow execution failed"
    else
        echo "? UNKNOWN: Could not determine workflow status"
    fi
    
    echo ""
    echo "Node Execution Summary:"
    # Count nodes that finished execution
    EXECUTED_NODES=$(grep -c "End execute" "$LOG_FILE" 2>/dev/null || echo "0")
    echo "- Nodes executed: $EXECUTED_NODES"
    
    # List executed nodes with timing
    echo "- Executed nodes:"
    grep "End execute" "$LOG_FILE" | sed 's/.*: /  /' | sed 's/ End execute/ completed in/' || echo "  None found"
    
    echo ""
    echo "Execution Timing:"
    # Extract workflow execution time
    WORKFLOW_TIME=$(grep "Workflow execution done" "$LOG_FILE" | sed -n 's/.*Finished in \([^)]*\).*/\1/p' || echo "Unknown")
    echo "- Total workflow time: $WORKFLOW_TIME"
    
    # Extract start and end times
    START_TIME=$(grep "Executing workflow" "$LOG_FILE" | head -1 | cut -d' ' -f1-2 2>/dev/null || echo "Unknown")
    END_TIME=$(grep "Workflow execution done" "$LOG_FILE" | tail -1 | cut -d' ' -f1-2 2>/dev/null || echo "Unknown")
    echo "- Started: $START_TIME"
    echo "- Completed: $END_TIME"
    
    echo ""
    echo "Issues Summary:"
    # Count errors and warnings
    ERROR_COUNT=$(grep -c ": ERROR :" "$LOG_FILE" 2>/dev/null || echo "0")
    WARN_COUNT=$(grep -c ": WARN :" "$LOG_FILE" 2>/dev/null || echo "0")
    echo "- Errors: $ERROR_COUNT"
    echo "- Warnings: $WARN_COUNT"
    
    # Show first error if any
    if [ "$ERROR_COUNT" -gt 0 ]; then
        echo ""
        echo "First Error:"
        grep ": ERROR :" "$LOG_FILE" | head -1 | sed 's/^/  /'
    fi
    
    # Show first warning if any
    if [ "$WARN_COUNT" -gt 0 ]; then
        echo ""
        echo "First Warning:"
        grep ": WARN :" "$LOG_FILE" | head -1 | sed 's/^/  /'
    fi
    
    echo ""
    echo "Summary:"
    echo "- Workflow: $WORKFLOW_NAME"
    echo "- Log file location: $LOG_FILE"
    echo "- Log file size: $(du -h "$LOG_FILE" | cut -f1)"
else
    echo "⚠ WARNING: No log file found at expected location"
    echo "Checking for alternative log locations..."
    find /home/knime -name "*.log" -type f 2>/dev/null | head -10
fi
echo "============================================"
