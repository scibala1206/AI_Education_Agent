# Use the official Node.js image as the base image
#FROM node:18 AS builder
#FROM alpine:3.20
FROM node:22 AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code to the container
COPY . .

# Build the Vite application
RUN npm run build

# Use a lightweight server to serve the built files
FROM nginx:stable-alpine AS production

# Copy the built files from the builder stage to the Nginx web root
COPY --from=builder /app/dist /usr/share/nginx/html

# Expose the default Nginx port
EXPOSE 80

# Start Nginx when the container runs
CMD ["nginx", "-g", "daemon off;"]
