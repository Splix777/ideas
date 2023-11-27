#nginx/Dockerfile

# Use the official Nginx base image
FROM nginx:latest

# Remove the default Nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# Set the working directory
WORKDIR /usr/share/nginx/html

# Copy the SSL certificates
COPY certificates/cert.pem /etc/nginx/cert.pem
COPY certificates/key.pem /etc/nginx/key.pem

# Copy the custom Nginx configuration
COPY default.conf /etc/nginx/conf.d/

# Expose ports (80 for HTTP and 443 for HTTPS)
EXPOSE 8080 8443

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]