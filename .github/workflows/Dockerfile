# Define the base image
FROM public.ecr.aws/i0n0z6j1/knime-full:5.6.0-nightly

# Path inside the image where the local update site will be copied
ARG LOCAL_UPDATE_SITE_PATH=/home/knime/local-update-site
ARG LOCAL_UPDATE_SITE_SRC=local-update-site
ENV LOCAL_UPDATE_SITE_SRC=${LOCAL_UPDATE_SITE_SRC}

# Define the list of update sites and features
# Add the local update site (copied into the image) to the list of update sites via file:// URL
# Ensure the local update site is present in the build context under ./local-update-site
ENV KNIME_UPDATE_SITES="file://${LOCAL_UPDATE_SITE_PATH}, https://update.knime.com/community-contributions/trusted/5.6, https://update.knime.com/analytics-platform/nightly/5.6.1"

# Install features from the update sites
# Allow overriding via build-arg; fallback to a sensible default matching knime.yml (group_id + ".features." + name)
ARG KNIME_FEATURES_ARG
ENV KNIME_FEATURES="${KNIME_FEATURES_ARG:-org.tutorial.features.first_extension.feature.group}"

# Install CA Certificates
USER root
RUN  apt-get update && \ 
apt-get install -y ca-certificates chromium-browser && \ 
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
