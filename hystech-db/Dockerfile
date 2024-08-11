# Use the official PostgreSQL image as the base image
FROM postgres:latest

# Set the environment variables for PostgreSQL
ENV POSTGRES_DB=postgres
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres

# Expose the default PostgreSQL port
EXPOSE 5432

# Copy any custom SQL scripts to the docker-entrypoint-initdb.d directory
# COPY init.sql /docker-entrypoint-initdb.d/

# Start the PostgreSQL server
CMD ["postgres"]