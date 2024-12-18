# Use the official Nginx image as a parent image
FROM nginx:latest

# Copy static content from your site into the container
COPY . /usr/share/nginx/html

# Copy a custom nginx.conf if needed
# COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80 to be accessible from outside
# EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
