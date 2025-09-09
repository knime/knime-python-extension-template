# Define the base image
FROM public.ecr.aws/i0n0z6j1/knime:5.7.0-nightly

# Path inside the image where the local update site will be copied
ARG LOCAL_UPDATE_SITE_PATH=/home/knime/local-update-site
ARG LOCAL_UPDATE_SITE_SRC
ENV LOCAL_UPDATE_SITE_SRC=${LOCAL_UPDATE_SITE_SRC}

# Define the list of update sites and features
# Add the local update site (copied into the image) to the list of update sites via file:// URL
# Ensure the local update site is present in the build context under ./local-update-site
ENV KNIME_UPDATE_SITES="file://${LOCAL_UPDATE_SITE_PATH}, https://update.knime.com/analytics-platform/nightly"

# Install features from the update sites
# Allow overriding via build-arg; fallback to a sensible default matching knime.yml (group_id + ".features." + name)
ARG KNIME_FEATURES_ARG
ENV KNIME_FEATURES="${KNIME_FEATURES_ARG:-org.tutorial.features.first_extension.feature.group}"

# Install CA Certificates
USER root
RUN  apt-get update && \ 
apt-get install -y ca-certificates chromium-browser unzip && \ 
update-ca-certificates && \ 
rm -rf /var/lib/apt/lists/*

USER knime

# Copy the local update site produced by the build into the image so it's available during installation
# The source folder can be overridden via --build-arg LOCAL_UPDATE_SITE_SRC=...
COPY --chown=knime:knime ${LOCAL_UPDATE_SITE_SRC} ${LOCAL_UPDATE_SITE_PATH}

# Execute extension installation script
RUN ./install-extensions.sh

# pre-start executor to improve startup time
RUN KNIME_EXECUTOR_CONNECTION_RETRIES=0 knime/knime -data /home/knime/knime-workspace -consolelog -nosplash -application com.knime.enterprise.slave.KNIME_REMOTE_APPLICATION; rm -rf /home/knime/knime-workspace

# Copy the demo workflow into the image
COPY --chown=knime:knime demo/ /home/knime/demo-workflow/

# Find and unzip the first .knwf file in the demo folder
RUN KNWF_FILE=$(find /home/knime/demo-workflow -name "*.knwf" -type f | head -1) && \
    if [ -z "$KNWF_FILE" ]; then \
        echo "ERROR: No .knwf file found in demo folder" && exit 1; \
    fi && \
    WORKFLOW_NAME=$(basename "$KNWF_FILE" .knwf) && \
    echo "Found workflow: $KNWF_FILE" && \
    echo "Extracting to: /home/knime/demo-workflow/$WORKFLOW_NAME" && \
    unzip "$KNWF_FILE" -d "/home/knime/demo-workflow/$WORKFLOW_NAME" && \
    echo "WORKFLOW_DIR=/home/knime/demo-workflow/$WORKFLOW_NAME" > /home/knime/workflow-info.env

# Copy the workflow analysis script
COPY --chown=knime:knime .github/scripts/analyze-workflow.sh /home/knime/analyze-workflow.sh
RUN chmod +x /home/knime/analyze-workflow.sh

# Run the demo workflow to test the extension
RUN . /home/knime/workflow-info.env && \
    echo "Running workflow from: $WORKFLOW_DIR" && \
    knime/knime -reset -consolelog -nosplash -application org.knime.product.KNIME_BATCH_APPLICATION -workflowDir="$WORKFLOW_DIR" > /home/knime/workflow-console.log 2>&1
